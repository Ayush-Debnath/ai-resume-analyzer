import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Load local env (for dev)
load_dotenv()


def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]  # Streamlit Cloud
    except:
        return os.getenv("GEMINI_API_KEY")   # Local


GEMINI_API_KEY = get_api_key()

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_ai_email(resume_text, job_description, job_role, company):
    prompt = f"""
You are an expert career assistant.

Write a highly personalized and professional job application email.

Context:
- Role: {job_role}
- Company: {company}

Resume:
{resume_text}

Job Description:
{job_description}

Instructions:
- Keep it concise (100–150 words)
- Highlight relevant skills from resume based on JD
- Sound confident but natural (not robotic)
- Align experience with job requirements
- Do NOT sound generic

Return only the email.
"""

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    try:
        return response.text
    except:
        return response.candidates[0].content.parts[0].text