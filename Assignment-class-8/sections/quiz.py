import streamlit as st
import json
from utils.gemini import ask_gemini

def show_quiz(language):
    st.subheader("🧩 Mini Quiz")

    prompt = (
        f"Generate a JSON list of 10 beginner-level multiple choice questions for learning {language}. "
        f"Each item must include 'question', 'options', and 'answer'. "
        f"Return only valid JSON like:\n"
        f"""[
            {{
                "question": "What is 'Hello' in Spanish?",
                "options": ["Hola", "Bonjour", "Ciao", "Hello"],
                "answer": "Hola"
            }}
        ]"""
    )

    response = ask_gemini(prompt)

    try:
        if "```" in response:
            response = response.split("```")[1]
            if response.startswith("json"):
                response = response[4:].strip()

        quiz_data = json.loads(response)

        st.session_state["quiz_answers"] = {}

        with st.form("quiz_form"):
            for idx, q in enumerate(quiz_data):
                st.write(f"**Q{idx+1}. {q['question']}**")
                answer = st.radio(
                    "Choose one:",
                    q["options"],
                    key=f"question_{idx}",
                    index=None,  # <== No default selection!
                )
                st.session_state["quiz_answers"][idx] = answer
                st.markdown("---")

            submitted = st.form_submit_button("✅ Submit Quiz")

        if submitted:
            with st.spinner("Checking your answers... Please wait a moment."):
                score = 0
                for idx, q in enumerate(quiz_data):
                    user_answer = st.session_state["quiz_answers"].get(idx)
                    if user_answer == q["answer"]:
                        st.success(f"✅ Q{idx+1}: Correct")
                        score += 1
                    else:
                        st.error(f"❌ Q{idx+1}: Wrong — Correct: {q['answer']}")
                st.info(f"🎯 Final Score: {score} / {len(quiz_data)}")


    except Exception as e:
        st.error("❌ Gemini failed or returned bad data.")
        st.code(response)
