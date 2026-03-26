import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_email(text):
    email = re.findall(r'\S+@\S+', text)
    return email[0] if email else None


def extract_phone(text):
    phone = re.findall(r'\+?\d[\d -]{8,12}\d', text)
    return phone[0] if phone else None


def extract_skills(text, skills_list):
    doc = nlp(text.lower())
    found_skills = []

    for token in doc:
        if token.text in skills_list:
            found_skills.append(token.text)

    return list(set(found_skills))


def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    return None


def parse_resume(text, skills_list):

    data = {}

    data["name"] = extract_name(text)
    data["email"] = extract_email(text)
    data["phone"] = extract_phone(text)
    data["skills"] = extract_skills(text, skills_list)

    return data