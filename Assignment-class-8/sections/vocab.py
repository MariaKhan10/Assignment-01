import streamlit as st
from utils.gemini import ask_gemini
from utils.helpers import text_to_speech

# Base abstract class for all language modules
class LanguageModule:
    def __init__(self, language):
        self.language = language

    def get_content(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def display(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Vocabulary class inheriting from LanguageModule
class Vocabulary(LanguageModule):
    def get_content(self):
        prompt = (
            f"Give 5 common beginner-level words in {self.language} "
            f"with English meanings and example usage."
        )
        return ask_gemini(prompt)

    def play_audio(self, text):
        audio_path = text_to_speech(text, lang_code="en")
        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")

    def display(self):
        st.subheader("📘 Daily Vocabulary")
        vocab_text = self.get_content()
        st.markdown(vocab_text)

        if st.button("🔊 Hear Pronunciation"):
            with st.spinner("Generating audio... This may take 2-3 minutes. Please wait..."):
                self.play_audio(vocab_text)



def show_vocab(language_name):
    vocab = Vocabulary(language_name)  
    vocab.display()                   
