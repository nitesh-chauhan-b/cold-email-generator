#Providing a view of the Scrapped data
import streamlit as st
import pandas as pd

st.title("Search Jobs")
try:
    jobs = pd.read_csv("Web_Scrapping/collection/All_Jobs.csv")

    #Creating a dataframe view
    st.dataframe(jobs,width=1000,height=600,
                 use_container_width=False,
                 selection_mode="single-column",
                 column_config={
                     "Link":st.column_config.LinkColumn("Link")
                 },
                 column_order=("Company","Title","Posted At","Link","Field","Location")
                 )

    #setting link clickable

except Exception as e:
    print(e)
