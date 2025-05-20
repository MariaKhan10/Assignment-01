import streamlit as st
from utils.gemini import ask_gemini

class LanguageModule:
    def __init__(self, language):
        self.language = language

    def get_content(self):
        raise NotImplementedError

class Practice(LanguageModule):
    def get_content(self):
        prompt = (
            f"Give 3 English sentences for the learner to translate into {self.language}. "
            f"Then provide correct translations and brief explanation for each."
        )
        return ask_gemini(prompt)

def show_practice(language_name):
    st.subheader("✍️ Practice Sentences")
    practice = Practice(language_name)
    content = practice.get_content()
    st.markdown(content)
