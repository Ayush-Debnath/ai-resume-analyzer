from google import genai
import os
import streamlit as st


GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]



client = genai.Client(api_key=GEMINI_API_KEY)


def generate_ai_email(resume_skills, matched_skills, missing_skills, job_role, company):

    prompt = f"""
You are an expert career assistant.

Write a professional, personalized job application email.

Context:
- Role: {job_role}
- Company: {company}
- Candidate Skills: {resume_skills}
- Matching Skills: {matched_skills}
- Missing Skills: {missing_skills}

Requirements:
- Keep it concise and human-like
- Sound confident but not arrogant
- Mention strengths
- Acknowledge improvement areas subtly
- Make it impactful

Generate email:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text