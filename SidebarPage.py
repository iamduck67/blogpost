import streamlit as st
st.logo("https://i.pinimg.com/736x/48/76/fa/4876faccd37a2ba781d1ac1f19555302.jpg", size='large', link="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

pages = {
    "I Like to live":[
        st.Page("Page1.py", title="I am the sigma-est of them all"),
        st.Page("main.py", title="I do not prefer to be a non-believer")
    ]
}



pg= st.navigation(pages)
pg.run()