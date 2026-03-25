from utils.text_cleaning import clean_text

def parse_job_description(text):
    cleaned_text = clean_text(text)

    return {
        "raw_text": text,
        "cleaned_text": cleaned_text
    }