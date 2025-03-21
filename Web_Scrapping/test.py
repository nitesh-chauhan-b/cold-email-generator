# # text ="""<div class="ibm--card__copy__inner">Professional<br/>GUADALAJARA, MX</div>"""
# # list = text.split("<br/>")
# # print(list)
# # print(list[0].find(">"))
# # _,_,res = list[0].partition(">")
# # res,_,_ = list[1].partition("<")
# # print(res)
#
# test = """
#             Bangalore, IN, 560103
#
#         """
# list = test.strip()
# # list = list[0][-1]
#
# print(list)


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
