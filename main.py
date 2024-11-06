import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Dave Cooper")
    content = """
    I am a veteran QA leader with a passion for learning 
    and delivering industry standard quality control measures. 
    Currently I am studying to become a Python developer 
    with great portfolio of projects to showcase in this web app"""
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python.  Feel free to contact me!
"""
st.write(content2)