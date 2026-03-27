import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
from backend.resume_parser import parse_resume
from backend.skill_extractor import extract_skills
from backend.job_parser import parse_job_description
from backend.similarity_engine import compute_similarity
from backend.skill_gap import compute_skill_gap
from backend.ats_scorer import compute_ats_score
from backend.job_recommender import recommend_jobs
from backend.email_generator import generate_ai_email
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🚀 AI Resume Analyzer")
st.caption("Built with NLP + ML + LLM (Gemini)")

# Upload Resume
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

# Job Description Input
job_description = st.text_area("Paste Job Description")

def plot_skill_comparison(matched, missing):
    labels = ['Matched Skills', 'Missing Skills']
    values = [len(matched), len(missing)]

    fig, ax = plt.subplots()
    ax.bar(labels, values)

    ax.set_title("Skill Comparison")
    ax.set_ylabel("Count")

    return fig

if uploaded_file and job_description:
    
    # Save uploaded file temporarily
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_data = parse_resume("temp_resume.pdf")
    job_data = parse_job_description(job_description)

    resume_skills = extract_skills(resume_data["cleaned_text"])
    job_skills = extract_skills(job_data["cleaned_text"])

    similarity_score = compute_similarity(
        " ".join(resume_skills),
        " ".join(job_skills)
    )

    gap = compute_skill_gap(resume_skills, job_skills)

    ats_score = compute_ats_score(
        similarity_score,
        gap["matched_skills"],
        gap["missing_skills"]
    )

    st.subheader("🎯 Scores")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Match Score", f"{similarity_score}%")

    with col2:
        st.metric("ATS Score", f"{ats_score}%")
    
    st.progress(int(similarity_score))
    st.write(f"Match Score: {similarity_score}%")

    st.progress(int(ats_score))
    st.write(f"ATS Score: {ats_score}%")

    st.write("🧠 Resume Skills", resume_skills)

    st.markdown("---")

    st.subheader("⚠️ Skill Gap")

    for skill in gap["missing_skills"]:
        st.markdown(f"❌ **{skill}**")

    st.markdown("---")
    st.subheader("💼 Job Recommendations")

    jobs = recommend_jobs(resume_data["cleaned_text"])

    for job in jobs:
        st.markdown(f"""
    ### 🏢 {job['company']}
    **Role:** {job['role']}  
    **Match:** {job['score']}%  
    """)
    
    st.markdown("---")

    st.subheader("📧 Generated HR Email")

    email = generate_ai_email(
        resume_skills,
        gap["matched_skills"],
        gap["missing_skills"],
        "Data Scientist",
        "Google"
    )

    st.text_area("Email", email, height=300)

    st.markdown("---")

    st.subheader("📊 Skill Analysis")

    fig = plot_skill_comparison(
        gap["matched_skills"],
        gap["missing_skills"]
    )

    st.pyplot(fig)

