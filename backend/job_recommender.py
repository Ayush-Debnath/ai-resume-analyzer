import json
from backend.job_parser import parse_job_description
from backend.skill_extractor import extract_skills
from backend.similarity_engine import compute_similarity


def load_jobs():
    with open("data/jobs.json", "r") as f:
        return json.load(f)


def recommend_jobs(resume_text):
    jobs = load_jobs()
    recommendations = []

    for job in jobs:
        job_data = parse_job_description(job["description"])

        score = compute_similarity(
            resume_text,
            job_data["cleaned_text"]
        )

        recommendations.append({
            "company": job["company"],
            "role": job["role"],
            "score": score
        })

    # sort by highest match
    recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)

    return recommendations