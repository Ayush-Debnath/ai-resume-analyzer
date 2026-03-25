from utils.pdf_loader import extract_text_from_pdf
from utils.text_cleaning import clean_text

def parse_resume(file_path):
    raw_text = extract_text_from_pdf(file_path)

    if not raw_text:
        return None

    cleaned_text = clean_text(raw_text)

    return {
        "raw_text": raw_text,
        "cleaned_text": cleaned_text
    }