# from app.Web_Scrapping.query_Manager import  QuerySingleton
#
# instance = QuerySingleton()
# # instance.query = "Machine Learning"
# # instance.query = "Hello"
# print("The value of query is :",instance.query)


import streamlit as st

# Initialize session state
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

# Button callback to update state
def button_callback():
    st.session_state.button_clicked = True

# Button with callback
st.button("Click Me", on_click=button_callback)

# Show output without losing state
if st.session_state.button_clicked:
    st.write("Button Clicked!")