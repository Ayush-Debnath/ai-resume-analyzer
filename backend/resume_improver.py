import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

# Load env for local
load_dotenv()


def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except:
        return os.getenv("GEMINI_API_KEY")


GEMINI_API_KEY = get_api_key()

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=GEMINI_API_KEY)


def improve_resume(resume_text, job_description):
    prompt = f"""
You are an expert resume writer and recruiter.

Improve and tailor the following resume specifically for the given job.

Job Description:
{job_description}

Resume:
{resume_text}

Instructions:
- Rewrite content to match job requirements
- Use strong action verbs
- Add measurable impact where possible
- Make it ATS-friendly
- Keep it concise and professional
- Focus on relevance to the job

Return the improved resume.
"""

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    try:
        return response.text
    except:
        return response.candidates[0].content.parts[0].text