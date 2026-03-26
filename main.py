from backend.resume_parser import parse_resume
from backend.skill_extractor import extract_skills
from backend.job_parser import parse_job_description
from backend.similarity_engine import compute_similarity
from backend.skill_gap import compute_skill_gap
from backend.ats_scorer import compute_ats_score

if __name__ == "__main__":
    file_path = "data/sample_resume.pdf"

    job_description = """
    Looking for a Data Scientist with Python, Machine Learning, SQL,
    Deep Learning, Docker, and AWS experience.
    """

    resume_data = parse_resume(file_path)
    job_data = parse_job_description(job_description)

    if resume_data:
        resume_skills = extract_skills(resume_data["cleaned_text"])
        job_skills = extract_skills(job_data["cleaned_text"])

        similarity_score = compute_similarity(
            resume_data["cleaned_text"],
            job_data["cleaned_text"]
        )

        gap = compute_skill_gap(resume_skills, job_skills)

        ats_score = compute_ats_score(
            similarity_score,
            gap["matched_skills"],
            gap["missing_skills"]
        )

        print("\n🧠 Resume Skills:", resume_skills)
        print("📌 Job Skills:", job_skills)

        print("\n✅ Matched Skills:", gap["matched_skills"])
        print("❌ Missing Skills:", gap["missing_skills"])

        print(f"\n🎯 Similarity Score: {similarity_score}%")
        print(f"📊 ATS Score: {ats_score}%")