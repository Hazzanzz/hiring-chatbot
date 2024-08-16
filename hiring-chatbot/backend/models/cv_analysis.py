from transformers import pipeline

nlp = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")

def parse_cv(cv_text):
    """Extract skills, experiences, and qualifications from the CV."""
    entities = nlp(cv_text)
    parsed_data = {
        "skills": [ent['word'] for ent in entities if ent['entity'] == 'SKILL'],
        "experience": [ent['word'] for ent in entities if ent['entity'] == 'ORG'],
        "qualifications": [ent['word'] for ent in entities if ent['entity'] == 'DEGREE']
    }
    return parsed_data
