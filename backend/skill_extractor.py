import json
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_nlp_entities(text):
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    return entities

def load_skills():
    with open("data/skills_db.json", "r") as f:
        return json.load(f)


def extract_skills(text):
    skills_db = load_skills()
    found_skills = set()

    text = text.lower()

    for category, skills in skills_db.items():
        for skill in skills:
            if skill in text:
                found_skills.add(skill)

    return list(found_skills)