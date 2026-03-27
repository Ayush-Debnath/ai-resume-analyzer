from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# load model once (IMPORTANT)
model = SentenceTransformer('all-MiniLM-L6-v2')


def compute_semantic_similarity(text1, text2):
    embeddings = model.encode([text1, text2])

    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(score * 100, 2)