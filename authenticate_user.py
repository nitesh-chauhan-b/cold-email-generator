import streamlit as st
import google_auth_oauthlib as auth
import pickle
import os
import json
import pandas as pd
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Adding / Initializing session login variable

if "LOGIN_STATUS" not in os.environ:
    os.environ["LOGIN_STATUS"] = "0"

if os.path.exists("JSON_data/user_account.json"):
    with open("JSON_data/user_account.json", "r") as file:
        user_account = json.load(file)
        os.environ["LOGIN_STATUS"] = user_account["login_status"]

#UI Components
# # Creating a empty container
container = st.empty()
sub_container = container.container()

#login for cloud
def login_callback():
    SCOPES = ["https://mail.google.com/"]

    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": st.secrets.client_id,
                "client_secret": st.secrets.client_secret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token"
            }
        },
        scopes=SCOPES
    )

    if os.environ.get("STREAMLIT_DEPLOYED"):  # Set this in your cloud environment
        # Headless OAuth (Cloud)
        auth_url, _ = flow.authorization_url(prompt='consent')
        st.info("Please click the link below to authorize access to your Gmail account:")
        st.markdown(f"[Authorize here]({auth_url})")

        code = st.text_input("Paste the authorization code here:")

        if code:
            flow.fetch_token(code=code)
            credentials = flow.credentials

            # Save token
            json_token = credentials.to_json()
            with open("JSON_data/token.json", "w") as file:
                file.write(json_token)

            st.session_state.credentials = credentials
            st.success("Your Authentication has been successfully done.")

            with open("JSON_data/user_account.json", "w") as file:
                json.dump({"login_status": "1"}, file)

    else:
        # Local OAuth (Localhost)
        credentials = flow.run_local_server(port=8080)
        json_token = credentials.to_json()
        with open("JSON_data/token.json", "w") as file:
            file.write(json_token)

        st.session_state.credentials = credentials
        st.success("Your Authentication has been successfully done.")

        with open("JSON_data/user_account.json", "w") as file:
            json.dump({"login_status": "1"}, file)

# Defining login function
# def login_callback():
#     credentials = auth.get_user_credentials(
#         scopes=["https://mail.google.com/"],
#         client_id=st.secrets.client_id,
#         client_secret=st.secrets.client_secret
#     )
#
#     # For storing the credentials for the user
#     st.session_state.credentials = credentials
#
#     # Getting the token file after getting the permissions from the user.
#     json_token = credentials.to_json()
#
#     # Saving the JSON file token
#     with open("JSON_data/token.json", "w") as file:
#         file.write(json_token)
#
#     # Storing the user_credentials in pickle file for secrecy
#     # with open("token.pkl", "wb") as file:
#     #     pickle.dump(json_token, file)
#
#     st.success("Your Authentication has been successfully done.")
#
#     # st.session_state.is_login = True
#     os.environ["LOGIN_STATUS"] = "1"
#
#     with open("JSON_data/user_account.json", "w") as file:
#         user_account = {}
#         user_account["login_status"] = "1"
#         json.dump(user_account, file)


# Logout Function
def logout_callback():
    st.session_state.is_login = False
    st.success("You Have Successfully Logged Out.")
    os.environ["LOGIN_STATUS"] = "0"

    # Removing the token file when user logs out from application
    if os.path.exists("JSON_data/token.json"):
        os.remove("JSON_data/token.json")

    # Removing user_account file.
    if os.path.exists("JSON_data/user_account.json"):
        os.remove("JSON_data/user_account.json")

    if os.path.exists("resource/company_portfolio.csv"):
        os.remove("resource/company_portfolio.csv")

# Function to get company details
def get_company_details():
    login_status = int(os.environ["LOGIN_STATUS"])

    if login_status == 1:
        # For getting details from the user
        sub_container.title("Company Details")

        #Assining Empty data
        company_name =False
        company_exp =False
        company_des = False
        user_name = False
        user_position = False
        company_email = False

        # Checking if the user has already provided company_info
        if os.path.exists("JSON_data/user_account.json"):
            with open("JSON_data/user_account.json", "r") as file:
                # converting it into json
                user_account = json.load(file)

                # print(type(user_account))

            # print("Stored File", user_account)
            comp_details = ["user_name","user_position","company_name","company_field_experience","company_description"]
            if "company_name" in user_account:

                # Getting user details
                user_name = sub_container.text_input("Enter Your Name",value=user_account["user_name"])

                user_position = sub_container.text_input("Your Position",value=user_account["user_position"])

                company_name = sub_container.text_input("Enter Company Name", value=user_account["company_name"])

                company_email = sub_container.text_input("Enter Company Contact Email",value=user_account['company_email'])

                company_exp = sub_container.text_input("How Long the Company have been in the industry?",
                                                       value=user_account["company_field_experience"])

                company_des = sub_container.text_area("Enter Company Description",
                                                      value=user_account["company_description"])

            else:

                #Getting user details
                user_name = sub_container.text_input("Enter Your Name")

                user_position = sub_container.text_input("Your Position")

                company_name = sub_container.text_input("Enter Company Name")

                company_email = sub_container.text_input("Enter Company Contact Email")

                company_exp = sub_container.text_input("How Long the Company have been in the industry?")

                company_des = sub_container.text_area("Enter Company Description")

        submit_btn = sub_container.button("Save")

        if submit_btn:
            if user_name:
                user_account["user_name"] = user_name
            else:
                st.error("Please Provide Your Name")

            if user_position:
                user_account["user_position"] = user_position
            else:
                st.error("Please Provide Your Position")

            if company_name:
                user_account["company_name"] = company_name
            else:
                st.error("Please Provide Company Name")

            if company_email:
                user_account["company_email"] = company_email
            else:
                st.error("Please Provide Company Contact Email")

            if company_exp:
                user_account["company_field_experience"] = company_exp
            else:
                st.error("Please Provide Company Industry Experience")

            if company_des:
                user_account["company_description"] = company_des
            else:
                st.error("Please Provide Company Description Which will be used for Email Generation")

            if company_name and company_des and company_exp and user_name and user_position and company_email:
                # Storing the Company Info in JSON File
                with open("JSON_data/user_account.json", "r") as file:
                    user_account_data = json.load(file)

                    # Writing the company details to file
                    user_account_data["company_name"] = user_account["company_name"]
                    user_account_data["company_field_experience"] = user_account["company_field_experience"]
                    user_account_data["company_description"] = user_account["company_description"]
                    user_account_data["user_name"] = user_account["user_name"]
                    user_account_data["user_position"] = user_account["user_position"]
                    user_account_data["company_email"] = user_account["company_email"]

                    with open("JSON_data/user_account.json", "w") as file:
                        json.dump(user_account_data, file)

                st.success("Your Information have been successfully stored!")

            # print(user_account_data)


def get_company_portfolio():

    #Allowing user to upload file

    sub_container.header("Company Portfolio")

    uploaded_file= sub_container.file_uploader("Choose a CSV File For Company Portfolio (Optional)")

    upload_message = False

    #Checking the status of file upload
    with open("JSON_data/user_account.json", "r") as file:
        user_account = json.load(file)
        if "company_portfolio_status" in user_account:
            portfolio_status = int(user_account["company_portfolio_status"])

            if portfolio_status==1:
                upload_message="Your Have Stored Portfolio."

    if upload_message:
        sub_container.write(upload_message)

    if uploaded_file is not None:

        #Reading a CSV File
        company_portfolio = pd.read_csv(uploaded_file)

        #Empty container
        empty_sub = sub_container.empty()
        empty_sub.write(company_portfolio)

        #Allowing user to upload this file
        upload_btn = sub_container.button("Upload File")

        if upload_btn:
            #Saving this CSV File for further use
            company_portfolio.to_csv("resource/company_portfolio.csv",index=False)

            #For Maintaining Company Portfolio upload status
            with open("JSON_data/user_account.json","r") as file:
                user_account = json.load(file)

                #Storing Portfolio Uploaded Status
                user_account["company_portfolio_status"] = "1"

                #Saving user account file
                with open("JSON_data/user_account.json","w") as file:
                    json.dump(user_account,file)
                    empty_sub.success("Your Company Portfolio has been uploaded successfully!")


login_status = int(os.environ["LOGIN_STATUS"])

if login_status != 1:
    st.title("Login With Google")
    st.button("Login With Google", on_click=login_callback, type="primary")

else:
    get_company_details()
    get_company_portfolio()
    st.button("Logout", on_click=logout_callback)