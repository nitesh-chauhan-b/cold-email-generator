import streamlit as st

#Defining Page
generate_Email = st.Page("cold_Email_Generator.py", title="Generate Cold Email", icon=":material/email:")
gathered_data = st.Page("job_collection.py", title="View Jobs", icon=":material/database:")
scrapper_page = st.Page("web_scrapper.py",title="Scrap Latest Data",icon="🔍")


pg = st.navigation([generate_Email,gathered_data,scrapper_page])


st.set_page_config(page_title="Cold Email Generator",page_icon=":material/email:")

pg.run()