import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

# 🔥 Load .env (for local development)
load_dotenv()

def get_api_key():
    try:
        # ✅ Streamlit Cloud
        return st.secrets["GEMINI_API_KEY"]
    except:
        # ✅ Local (.env)
        return os.getenv("GEMINI_API_KEY")

GEMINI_API_KEY = get_api_key()

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in secrets or environment variables")

client = genai.Client(api_key=GEMINI_API_KEY)

def improve_resume(text):

    prompt = f"""
You are an expert resume writer.

Improve the following resume content:
- Make it professional and impactful
- Use strong action verbs
- Add measurable impact where possible
- Keep it concise and ATS-friendly

Resume:
{text}

Return improved version:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    try:
        return response.text
    except:
        return response.candidates[0].content.parts[0].text