import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except:
        return os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=get_api_key())


def compute_ai_match(resume_text, job_description):

    prompt = f"""
You are an expert recruiter.

Evaluate how well the candidate matches the job.

Return:
1. Match Score (0-100)
2. Short reasoning

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    try:
        return response.text
    except:
        return response.candidates[0].content.parts[0].text