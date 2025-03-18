import langchainHelper
import streamlit as st

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

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

        st.code(cold_email.content,language="markdown",wrap_lines=True,height=700)


except Exception as e:
    st.write("Some Error has occurred :",e)
    st.write("Something went wrong!! Please retry or try contacting developer at niteshchauhanb@gmail.com ")
