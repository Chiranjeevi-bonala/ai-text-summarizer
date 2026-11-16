
import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure page
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🤖",
    layout="centered"
)

# Application heading
st.title("🤖 AI Text Summarizer")
st.write("Summarize text using Google Gemini AI.")

st.divider()

# Text input
user_text = st.text_area(
    "Enter your text:",
    height=250,
    placeholder="Paste your article here..."
)

# Summary length selection
summary_length = st.selectbox(
    "Choose summary length:",
    ["Short", "Medium", "Detailed"]
)

# Summary generation
if st.button("Generate Summary", type="primary"):

    if not user_text.strip():
        st.warning("Please enter some text.")

    elif not api_key:
        st.error("Gemini API key not found. Check your .env file.")

    else:
        try:
            client = genai.Client(api_key=api_key)

            # Instructions based on selected length
            length_instructions = {
                "Short": "Summarize in 2-3 sentences.",
                "Medium": "Summarize in one concise paragraph.",
                "Detailed": "Provide a detailed summary covering all important points."
            }

            prompt = f"""
            You are an AI text summarization assistant.

            Summarize the following text in simple English.

            Summary length: {summary_length}
            Instructions: {length_instructions[summary_length]}

            Rules:
            1. Do not add facts that are not in the original text.
            2. Preserve the important information.
            3. Use clear and simple English.

            Text:
            {user_text}
            """

            with st.spinner("Gemini is generating your summary..."):

                response = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=prompt
                )

            # Display result
            if response.output_text:
                st.divider()
                st.subheader("✨ AI Generated Summary")
                st.write(response.output_text)

                st.caption(f"Summary length: {summary_length}")

            else:
                st.warning("The AI did not return a summary. Please try again.")

        except Exception as e:
            st.error(f"Something went wrong: {e}")
