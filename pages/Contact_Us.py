import streamlit as st
import pandas
from send_email import send_email

topics_df = pandas.read_csv("topics.csv")
topics = topics_df["topic"].tolist()

st.header("Contact Us")

with st.form(key="contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    reason = st.selectbox("Reason for Contact", topics)
    raw_message = st.text_area("Message")
    message = f"""\
Subject: New email from {email}

From: {email}
Topic: {reason}
{raw_message}
"""
    submit = st.form_submit_button("Submit")
    if submit:
        send_email(message)
        st.info(f"Thank you {name} for your message. We will get back to you at {email} shortly.")