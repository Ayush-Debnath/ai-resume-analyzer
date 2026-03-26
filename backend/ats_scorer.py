def compute_ats_score(similarity_score, matched_skills, missing_skills):
    
    # Normalize similarity (out of 100)
    similarity_weight = 0.4 * similarity_score

    total_skills = len(matched_skills) + len(missing_skills)

    if total_skills == 0:
        skill_score = 0
    else:
        skill_score = (len(matched_skills) / total_skills) * 100

    skill_weight = 0.6 * skill_score

    final_score = similarity_weight + skill_weight

    return round(final_score, 2)