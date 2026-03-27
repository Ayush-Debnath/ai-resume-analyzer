import json
from backend.job_parser import parse_job_description
from backend.skill_extractor import extract_skills
from backend.semantic_similarity import compute_semantic_similarity


def load_jobs():
    with open("data/jobs.json", "r") as f:
        return json.load(f)


def recommend_jobs(resume_text):
    jobs = load_jobs()
    recommendations = []

    # extract resume skills ONCE
    resume_skills = extract_skills(resume_text)

    for job in jobs:
        job_data = parse_job_description(job["description"])
        job_skills = extract_skills(job_data["cleaned_text"])

        # 🔥 1. Semantic similarity (skills-based)
        semantic_score = compute_semantic_similarity(
            " ".join(resume_skills),
            " ".join(job_skills)
        )

        # 🔥 2. Skill overlap score
        matched = set(resume_skills) & set(job_skills)

        if len(job_skills) == 0:
            skill_score = 0
        else:
            skill_score = (len(matched) / len(job_skills)) * 100

        # 🔥 3. Final hybrid score
        final_score = (0.7 * semantic_score) + (0.3 * skill_score)

        recommendations.append({
            "company": job["company"],
            "role": job["role"],
            "score": round(final_score, 2)
        })

    # sort by highest match
    recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)

    return recommendations