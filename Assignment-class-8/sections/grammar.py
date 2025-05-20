import streamlit as st
from utils.gemini import ask_gemini

# Base LanguageModule class 
class LanguageModule:
    def __init__(self, language):
        self.language = language
    
    def get_content(self):
        raise NotImplementedError("Subclasses should implement this!")

# Grammar class inheriting LanguageModule (Inheritance)
class Grammar(LanguageModule):
    def get_content(self):
        prompt = (
            f"Explain the basic grammar rules of {self.language} for a beginner. "
            f"Keep it simple and give 2-3 examples."
        )
        return ask_gemini(prompt)

def show_grammar(language_name):
    st.subheader("📚 Grammar Basics")
    grammar = Grammar(language_name)  
    content = grammar.get_content()  
    st.markdown(content)
