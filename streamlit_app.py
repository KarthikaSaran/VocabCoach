import streamlit as st
import requests
openai_api_key = st.secrets["OPENAI_API_KEY"]

st.title("📖 AI-Powered Dictionary")

word = st.text_input("What's your vocab query?")

if st.button("Hit Me!"):
    response = requests.get(f"https://my-ai-dictionary.onrender.com/define/{word}")
    if response.status_code == 200:
        data = response.json()
        st.json(data)
    else:
        st.error("Error fetching word details.")
