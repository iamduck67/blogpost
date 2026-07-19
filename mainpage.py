import streamlit as st

st.logo("https://i.ytimg.com/vi/N9g1WHfZgaM/hq720.jpg?sqp=-oaymwExCK4FEIIDSFryq4qpAyMIARUAAIhCGAHwAQH4Af4JgALQBYoCDAgAEAEYZSBPKFMwDw==&rs=AOn4CLAFcZJpKgs3NS2H8C_bOtjbPyWrvA", size="large", link="https://iamduck67.streamlit.app/")

if "logged_in" not in st.session_state:
  st.session_state.logged_in = False
def login():
  st.title("Log in")
  with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Log in")

  if submitted:
    if username == 'admin' and password == '1234':
      st.session_state.logged_in = True
      st.session_state.username = username
      st.rerun()
    else:
      st.error("Incorrect username or password...")  

def logout():
  st.session_state.logged_in = False
  st.rerun()
login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

pages = {
  "Daily life": [
    st.Page("Page1.py", title = "Page 1"),
    st.Page("page2.py", title = "Page 2")
  ],

  "Favorite food": [
     st.Page("food.py", title = "Food")
  ],
  "Settings": [logout_page]
}
if st.session_state.logged_in:
  pg = st.navigation(pages)
else:
  pg = st.navigation([login_page])


pg.run()