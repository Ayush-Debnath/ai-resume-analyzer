import backend
from backend.resume_parser import parse_resume
from backend.skill_extractor import extract_skills
from backend.job_parser import parse_job_description
from backend.similarity_engine import compute_similarity
from backend.skill_gap import compute_skill_gap
from backend.ats_scorer import compute_ats_score
from backend.job_recommender import recommend_jobs
# from backend.email_generator import generate_email
from backend.email_generator import generate_ai_email
from backend.job_scraper import scrape_jobs
from backend.semantic_similarity import compute_semantic_similarity
from backend.resume_improver import improve_resume

if __name__ == "__main__":
    file_path = "data/sample_resume.pdf"

    job_description = """
    Bachelor's degree in Statistics, Mathematics, or related field.
    Proficiency in SQL and data visualization tools (e.g., Tableau).
    Strong analytical and problem-solving skills.
    Knowledge of data mining techniques.
    Ability to work independently and as part of a team.
    Data Analysis SQL Data Visualization Tableau Data Mining
    """

    resume_data = parse_resume(file_path)
    job_data = parse_job_description(job_description)
    recommendations = recommend_jobs(resume_data["cleaned_text"])
    jobs = scrape_jobs("Full Stack Developer")
    semantic_score = compute_semantic_similarity(
    resume_data["cleaned_text"],
    job_data["cleaned_text"])
    improved = improve_resume(resume_data["raw_text"])


    if resume_data:
        resume_skills = extract_skills(resume_data["cleaned_text"])
        job_skills = extract_skills(job_data["cleaned_text"])


        similarity_score = compute_semantic_similarity(
            " ".join(resume_skills),
            " ".join(job_skills)
        )

        gap = compute_skill_gap(resume_skills, job_skills)

        ats_score = compute_ats_score(
            similarity_score,
            gap["matched_skills"],
            gap["missing_skills"]
        )

        email = generate_ai_email(
            resume_skills,
            gap["matched_skills"],
            gap["missing_skills"],
            "Data Scientist",
            "Google"
        )

        print("\n🧠 Resume Skills:", resume_skills)
        print("📌 Job Skills:", job_skills)

        print("\n✅ Matched Skills:", gap["matched_skills"])
        print("❌ Missing Skills:", gap["missing_skills"])

        print(f"\n🎯 Similarity Score: {similarity_score}%")
        print(f"📊 ATS Score: {ats_score}%")

        print("\n🔥 Job Recommendations:\n")
        for job in recommendations:
            print(f"{job['company']} | {job['role']} | {job['score']}%")
        
        # print("\n📧 Generated Email:\n")
        # print(email)

        print("\n🌍 Live Jobs:\n")
        for job in jobs:
            print(job) 

        print(f"\n🧠 Semantic Match Score: {semantic_score}%")   

        print("\n🔥 Improved Resume:\n")
        print(improved[:1000])   