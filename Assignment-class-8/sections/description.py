import streamlit as st
from utils.gemini import ask_gemini

class LanguageDescription:
    def __init__(self, language):
        self.language = language

    def get_description(self):
        prompt = (
            f"Write a detailed, friendly, and engaging introduction about the "
            f"{self.language} language. Include why it's interesting, useful, "
            f"and some key cultural or linguistic facts to motivate new learners."
        )
        return ask_gemini(prompt)

def show_description(language_name):
    st.subheader("📘 Language Overview")
    lang_desc = LanguageDescription(language_name) 
    description_text = lang_desc.get_description()
    st.markdown(description_text)

