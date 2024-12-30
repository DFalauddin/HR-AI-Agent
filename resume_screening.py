import spacy

class ResumeScreening:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def extract_skills(self, resume_text):
        doc = self.nlp(resume_text)
        skills = [ent.text for ent in doc.ents if ent.label_ == 'SKILL']
        return skills

    def match_skills(self, resume_skills, job_description):
        job_doc = self.nlp(job_description)
        job_skills = [ent.text for ent in job_doc.ents if ent.label_ == 'SKILL']
        matched_skills = set(resume_skills).intersection(set(job_skills))
        return matched_skills
