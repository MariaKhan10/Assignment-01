import streamlit as st
from sections.description import show_description
from sections.vocab import show_vocab
from sections.grammar import show_grammar
from sections.practice import show_practice
from sections.quiz import show_quiz


class LanguageTab:
    def __init__(self, language):
        self.language = language

    def render(self):
        raise NotImplementedError()

class DescriptionTab(LanguageTab):
    def render(self):
        show_description(self.language)

class VocabularyTab(LanguageTab):
    def render(self):
        show_vocab(self.language)

class GrammarTab(LanguageTab):
    def render(self):
        show_grammar(self.language)

class QuizTab(LanguageTab):
    def render(self):
        show_quiz(self.language)

st.set_page_config(page_title="LingoCoach AI", layout="wide")


st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .stApp {
            padding: 2rem;
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 18px;
            padding: 12px 20px;
        }
        .stButton>button {
            background-color: #2e7bcf;
            color: white;
            border-radius: 6px;
        }
        .stButton>button:hover {
            background-color: #1a5fa1;
        }
        .stSelectbox, .stSidebar select {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# ----------- Sidebar -------------------
st.sidebar.title("🌐 Select Your Language")
languages = [
    "Select a Language",
    "Spanish",
    "French",
    "German",
    "Italian",
    "Chinese",
    "Arabic",
    "Japanese",
    "Korean",
    "Hindi",
    "Turkish",
]
selected_language = st.sidebar.selectbox("Language", languages)

# ----------- Header -------------------
st.markdown("<h1 style='color:#2e7bcf;'>👨‍🏫 LingoCoach AI</h1>", unsafe_allow_html=True)
st.markdown("### Master any language with vocabulary, grammar, audio, and quizzes — all in one place.")
st.markdown("---")

# ----------- Main Content -------------
if selected_language != "Select a Language":
    st.success(f"✅ You selected: **{selected_language}**")

    tabs = {
        "📘 Description": DescriptionTab(selected_language),
        "🗣️ Vocabulary": VocabularyTab(selected_language),
        "📚 Grammar": GrammarTab(selected_language),
        "🧩 Quiz": QuizTab(selected_language)
    }

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📘 Description",
        "🗣️ Vocabulary",
        "📚 Grammar",
        "✍️ Practice",      
        "🧩 Quiz"
    ])

    with tab1:
        show_description(selected_language)

    with tab2:
        show_vocab(selected_language)

    with tab3:
        show_grammar(selected_language)

    with tab4:
        show_practice(selected_language)   

    with tab5:
        show_quiz(selected_language)

else:
    st.warning("⬅️ Please select a language from the sidebar to begin.")
