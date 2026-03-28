import sys
import os

from backend.ai_matcher import compute_ai_match

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
from backend.resume_improver import improve_resume

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
    ai_output = compute_ai_match(
    resume_data["raw_text"],
    job_description
)

    ai_score = ai_output["match_score"]
    ai_reason = ai_output["reason"]


    final_score = (0.6 * similarity_score) + (0.4 * ai_score)

    gap = compute_skill_gap(resume_skills, job_skills)

    ats_score = compute_ats_score(
        similarity_score,
        gap["matched_skills"],
        gap["missing_skills"]
    )

    st.subheader("🎯 Scores")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Match Score", f"{final_score}%")

    with col2:
        st.metric("ATS Score", f"{ats_score}%")
    
    st.progress(int(similarity_score))
    st.write(f"Match Score: {final_score}%")

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

    if st.button("Generate AI Email ✉️"):
        with st.spinner("Generating personalized email..."):

            email = generate_ai_email(
            resume_data["raw_text"],
            job_description,
            "Target Role",   # you can improve later dynamically
            "Target Company"
        )

        st.text_area("Generated Email", email, height=300)

        st.download_button(
            label="📥 Download Email",
            data=email,
            file_name="job_application_email.txt",
            mime="text/plain"
        )

    st.markdown("---")

    st.subheader("📊 Skill Analysis")

    fig = plot_skill_comparison(
        gap["matched_skills"],
        gap["missing_skills"]
    )

    st.pyplot(fig)

    st.subheader("✨ AI Resume Improver")

    if st.button("Improve Resume 🚀"):
        with st.spinner("Optimizing your resume for this job..."):

            improved_resume = improve_resume(
                resume_data["raw_text"],
                job_description
            )

            st.text_area("Improved Resume", improved_resume, height=400)

            st.download_button(
                label="📥 Download Improved Resume",
                data=improved_resume,
                file_name="improved_resume.txt",
                mime="text/plain"
            )
