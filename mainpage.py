import streamlit as st

st.logo("https://i.ytimg.com/vi/N9g1WHfZgaM/hq720.jpg?sqp=-oaymwExCK4FEIIDSFryq4qpAyMIARUAAIhCGAHwAQH4Af4JgALQBYoCDAgAEAEYZSBPKFMwDw==&rs=AOn4CLAFcZJpKgs3NS2H8C_bOtjbPyWrvA", size="large", link="https://iamduck67.streamlit.app/")

pages = {
  "Daily life": [
    st.Page("page1.py", title = "Page 1"),
    st.Page("page2.py", title = "Page 2")
  ],

  "Favorite food": [
     st.Page("food.py", title = "Food")
  ]
}

pg = st.navigation(pages)
pg.run()