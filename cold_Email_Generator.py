import os.path
import time

import langchainHelper
import streamlit as st
import cold_email_agent as agent
#Creating a User Interface for the application.

st.title("✉️ Cold Email Generator")
url = st.text_input("Paste Job portal url : ",placeholder="https://jobs.nike.com/R-33460")
submit = st.button("Submit")
try:
    if url and submit:
        #Webscrapping data from url
        page_data = langchainHelper.get_web_data(url)

        #Converting page_data into a required json data
        json_data = langchainHelper.get_json_data(page_data)

        #Storing the csv file into a vector database for similaritySearch
        langchainHelper.store_company_portfolio("resource/my_portfolio.csv")

        #Getting relevant links from the vector data for providing reference into email
        relevant_portfolio_links = langchainHelper.get_relevant_links(json_data)

        #Using these both relevant_links and json data to generate a cold email.
        if relevant_portfolio_links:
            cold_email = langchainHelper.get_cold_email(json_data, relevant_portfolio_links)
        else:
            cold_email = langchainHelper.get_cold_email(json_data, "")

        #Providing cold email to user
        st.header("**Cold Email**")

        generated_Email = cold_email.content

        #Storing email in session
        st.session_state.generated_Email = generated_Email

        is_email_generated = st.code(generated_Email,language="markdown",wrap_lines=True,height=700)

        #Creating a container for buttons
        container = st.empty()

        def daft_email():
            with container.status("Drafting email... ⏳", expanded=True) as status:
                # Calling email agent to draft the email
                recipient_email = "nkchauhan9090@gmail.com"
                email_text = st.session_state.generated_Email

                # Calling agent
                agent_response = agent.activate_email_draft_agent(email_text, recipient_email)

                container.write(f"**{agent_response}**")
                status.update(label="✅ Email saved in drafts!", state="complete")

        #Draft Email button
        container.button("Save Email In Draft", on_click=daft_email)

except Exception as e:
    print(e)
    st.write("Some Error has occurred :",e)
    st.write("Something went wrong!! Please retry or try contacting developer at niteshchauhanb@gmail.com ")