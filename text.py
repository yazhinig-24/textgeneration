import streamlit as st
import cohere

# Replace with your Cohere API key
COHERE_API_KEY = "BYK0dv9byAIxxv88wCa4wHJ4CxYtDDhXp0tnE8Ep"

co = cohere.Client(COHERE_API_KEY)

st.set_page_config(page_title="Text-to-Text with Cohere", layout="centered")

st.title("🧠 Text-to-Text Generator with Cohere")

task = st.selectbox("Choose your task", ["Summarization", "Paraphrasing", "Custom Prompt"])
user_input = st.text_area("Enter your text here", height=200)

if st.button("Generate"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating..."):
            if task == "Summarization":
                prompt = f"Summarize this: {user_input}"
            elif task == "Paraphrasing":
                prompt = f"Paraphrase this: {user_input}"
            else:
                prompt = user_input

            response = co.generate(
                model='command-xlarge',
                prompt=prompt,
                max_tokens=100,
                temperature=0.7
            )

            result = response.generations[0].text.strip()
            st.subheader("Output:")
            st.success(result)
