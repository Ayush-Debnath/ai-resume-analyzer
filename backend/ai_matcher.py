import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
import json

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

Return ONLY in JSON format:
{{
  "match_score": number (0-100),
  "reason": "short explanation"
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )

    try:
        text = response.text
    except:
        text = response.candidates[0].content.parts[0].text

    # 🔥 Parse JSON safely
    try:
        result = json.loads(text)
    except:
        # fallback if model messes up format
        result = {
            "match_score": 50,
            "reason": text
        }

    return result