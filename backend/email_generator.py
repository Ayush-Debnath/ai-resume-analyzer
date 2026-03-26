def generate_email(resume_skills, matched_skills, missing_skills, job_role, company):

    intro = f"""
Subject: Application for {job_role} Role at {company}

Dear Hiring Manager,
"""

    body = f"""
I hope you are doing well.

I am writing to express my interest in the {job_role} position at {company}. 
With a strong background in {', '.join(resume_skills[:5])}, I believe I am a strong candidate for this role.

My experience aligns well with your requirements, particularly in {', '.join(matched_skills)}.
"""

    improvement = ""
    if missing_skills:
        improvement = f"""
I am also actively working on improving my skills in {', '.join(missing_skills)}, ensuring continuous growth and alignment with industry demands.
"""

    closing = """
I would love the opportunity to contribute to your team and discuss how my skills can add value.

Thank you for your time and consideration.

Best regards,  
[Your Name]
"""

    email = intro + body + improvement + closing

    return email.strip()