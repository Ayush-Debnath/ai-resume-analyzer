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


def extract_skills_ai(job_description):

    prompt = f"""
Extract the key technical skills from the following job description.

Return ONLY a Python list.

Job Description:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    try:
        text = response.text
    except:
        text = response.candidates[0].content.parts[0].text

    return text