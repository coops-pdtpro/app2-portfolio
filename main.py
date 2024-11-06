import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Dave Cooper")
    content = """
    I am a software tester with a passion for learning.
    """
    st.info(content)