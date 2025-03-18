import time
import streamlit as st
import website_scrapper
from Web_Scrapping.query_Manager import QuerySingleton

st.header("🔍 Search Latest Jobs")
query = st.text_input("Enter Title of the Job",placeholder="Like Python, AI/ML etc.")

scrap_btn =st.button("Get Latest Data")

#Setting query for search

if scrap_btn:

    if query:
        singleton = QuerySingleton()
        singleton.query = query

        st.write(f"Starting Scrapping for {query}")
        scrapped = website_scrapper.scrap()
        st.write("Data have been scrapped successfully!!")

        st.write("Collecting job details from data...")
        collect = website_scrapper.collect()
        st.write("Data have been collected successfully!!")

        #Saving data
        st.write("Saving job details from data...")
        saved = website_scrapper.save_data()
        if saved:
            st.write("Data have been saved successfully!!")
        else:
            st.write("Failure!")
        # save_btn = st.button("Save Data")



        # if save_btn:
        #     saved = website_scrapper.save_data()
        #
        #     if saved:
        #         st.write("The data have been successfully saved!")
        #         print("The data has been saved successfully!")
        #         time.sleep(5)
        #     else:
        #         st.write("There is some issue in saving data!")
        #         print("The data has not been saved successfully!")
        #         time.sleep(5)