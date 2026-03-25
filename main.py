from backend.resume_parser import parse_resume
from backend.skill_extractor import extract_skills
from backend.job_parser import parse_job_description
from backend.similarity_engine import compute_similarity

if __name__ == "__main__":
    file_path = "data/sample_resume.pdf"

    # fake job description for now
    job_description = """
    We are looking for a Data Scientist with experience in Python, Machine Learning,
    SQL, and Deep Learning. Knowledge of TensorFlow or PyTorch is a plus.
    """

    resume_data = parse_resume(file_path)
    job_data = parse_job_description(job_description)

    if resume_data:
        skills = extract_skills(resume_data["cleaned_text"])

        score = compute_similarity(
            resume_data["cleaned_text"],
            job_data["cleaned_text"]
        )

        print("\n🧠 Skills:", skills)
        print(f"\n🎯 Match Score: {score}%")