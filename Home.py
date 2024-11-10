import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap');
    .header {
        font-family: 'Dancing Script', cursive;
        font-size: 48px;
        text-align: center;
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .column {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }
    .project-title {
        font-size: 24px;
        font-weight: bold;
    }
    .project-title:hover {
        color: #007BFF;
    }
    </style>
    <div class="header">Dave Cooper's Portfolio</div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("About me:")
    content = """
    I am a veteran QA leader with a passion for learning 
    and delivering industry standard quality control measures
    along with strategic leadership to enable and facilitate 
    rapid company growth. 
    
    Currently I am studying Python to enable me to:
    * Strengthen my Test Automation skills
    * Become a Junior Python developer 
    
    This web app is being created by me to allow me to showcase my new skills
    within a portfolio of projects that I have already delivered, 
    are currently in progress or not yet started.
    
    My new skills are being taught to me by the amazing Ardit Sulce 
    via his Python Mega Course on Udemy which I highly recommend to anyone 
    wanting to learn or improve their knowledge of coding in Python.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python.  Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")