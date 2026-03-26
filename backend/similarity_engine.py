from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_text, job_text):
    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2),max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    return round(similarity_score * 100, 2)