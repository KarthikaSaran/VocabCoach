import streamlit as st
import requests

st.title("📖 AI-Powered Dictionary")

word = st.text_input("Enter a word to look up:")

if st.button("Get Meaning"):
    response = requests.get(f"https://my-ai-dictionary.onrender.com/define/{word}")
    if response.status_code == 200:
        data = response.json()
        st.json(data)
    else:
        st.error("Error fetching word details.")
