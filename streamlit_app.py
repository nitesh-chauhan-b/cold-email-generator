import streamlit as st

import sys
import pysqlite3
sys.modules["sqlite3"] = pysqlite3


#Defining Page
user_authentication = st.Page("authenticate_user.py",title="User Account",icon=":material/person:")
generate_Email = st.Page("cold_Email_Generator.py", title="Generate Cold Email", icon=":material/email:")
gathered_data = st.Page("job_collection.py", title="View Jobs", icon=":material/database:")
scrapper_page = st.Page("web_scrapper.py",title="Scrap Latest Data",icon=":material/search:")


pg = st.navigation([user_authentication,generate_Email,gathered_data,scrapper_page])


st.set_page_config(page_title="Cold Email Generator",page_icon=":material/email:")

pg.run()