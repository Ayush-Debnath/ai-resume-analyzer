def clean_text(text):
    import re

    text = text.lower()

    # replace common synonyms
    text = text.replace("ml", "machine learning")

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()