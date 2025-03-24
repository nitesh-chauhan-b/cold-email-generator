import streamlit as st
import google_auth_oauthlib as auth
import pickle
import os

# Adding / Initializing session login variable

if "LOGIN_STATUS" not in os.environ:
    os.environ["LOGIN_STATUS"] = "0"


# Defining login function
def login_callback():
    credentials = auth.get_user_credentials(
        scopes=["https://mail.google.com/"],
        client_id=st.secrets.client_id,
        client_secret=st.secrets.client_secret
    )

    # For storing the credentials for the user
    st.session_state.credentials = credentials

    # Getting the token file after getting the permissions from the user.
    json_token = credentials.to_json()

    # Saving the JSON file token
    with open("token.json","w") as file:
        file.write(json_token)

    # Storing the user_credentials in pickle file for secrecy
    # with open("token.pkl", "wb") as file:
    #     pickle.dump(json_token, file)

    st.success("Your Authentication has been successfully done.")

    # st.session_state.is_login = True
    os.environ["LOGIN_STATUS"] = "1"
#Logout Function
def logout_callback():
    st.session_state.is_login = False
    st.success("You Have Successfully Logged Out.")
    os.environ["LOGIN_STATUS"] = "0"

    #Removing the token file when user logs out from application
    if os.path.exists("token.json"):
        os.remove("token.json")

#Function to get company details
def get_company_details():
    login_status = int(os.environ["LOGIN_STATUS"])
    if login_status==1:
        # Creating a empty container
        container = st.empty()

        company_info = {}
        sub_container = container.container()

        # For getting details from the user
        sub_container.title("Company Details")

        company_name = sub_container.text_input("Enter Company Name", )

        company_exp = sub_container.text_input("How Long the Company have been in the industry?")

        company_des = sub_container.text_input("Enter Company Desciption")

        submit_btn = sub_container.button("Save")

        if submit_btn:
            if company_name:
                company_info["Name"] = company_name

            if company_exp:
                company_info["Field Exprience"] = company_exp

            if company_des:
                company_info["Description"] = company_des

            st.success("Your Information have been successfully stored!")

            print(company_info)

login_status = int(os.environ["LOGIN_STATUS"])
if login_status!=1:
    st.title("Login With Google")
    st.button("Login With Google", on_click=login_callback, type="primary")

else:
    get_company_details()
    st.button("Logout", on_click=logout_callback)