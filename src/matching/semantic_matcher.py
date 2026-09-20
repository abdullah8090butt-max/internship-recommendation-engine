import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

from data.internship_tracks import INTERNSHIP_TRACKS


MODEL_NAME = "sentence-transformers/paraphrase-MiniLM-L3-v2"


# Load the Sentence Transformer model only once.
# This prevents the model from being loaded repeatedly
# every time a recommendation is generated.
_model = None


def get_model():
    global _model

    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)

    return _model


def generate_candidate_embedding(candidate_text):
    model = get_model()

    embedding = model.encode(
        [candidate_text],
        convert_to_numpy=True
    )

    return embedding


def generate_track_embeddings():
    model = get_model()

    track_texts = [
        track["description"]
        for track in INTERNSHIP_TRACKS
    ]

    embeddings = model.encode(
        track_texts,
        convert_to_numpy=True
    )

    return embeddings


def calculate_similarity(
    candidate_embedding,
    track_embeddings
):
    similarities = cosine_similarity(
        candidate_embedding,
        track_embeddings
    )

    return similarities[0]


def rank_tracks(similarities):
    ranked_tracks = []

    for index, score in enumerate(similarities):

        ranked_tracks.append({
            "name": INTERNSHIP_TRACKS[index]["name"],
            "score": float(score)
        })

    ranked_tracks.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked_tracks


if __name__ == "__main__":

    candidate_text = """
    Skills: Python, Pandas, NumPy, Scikit-learn,
    Machine Learning, Streamlit

    Education: FSc ICS

    Certifications: AI Fundamentals

    Career Interests: Artificial Intelligence,
    Machine Learning, Generative AI

    Projects: Medical AI Assistant,
    Student Data Analysis
    """

    print(
        "\nLoading Sentence Transformer model..."
    )

    candidate_embedding = (
        generate_candidate_embedding(
            candidate_text
        )
    )

    print(
        "Candidate embedding generated."
    )

    track_embeddings = (
        generate_track_embeddings()
    )

    print(
        "Track embeddings generated."
    )

    similarities = calculate_similarity(
        candidate_embedding,
        track_embeddings
    )

    ranked_tracks = rank_tracks(
        similarities
    )

    print(
        "\n========== INTERNSHIP MATCHING =========="
    )

    for rank, track in enumerate(
        ranked_tracks,
        start=1
    ):

        print(
            f"{rank}. {track['name']} "
            f"→ Similarity: "
            f"{track['score']:.4f}"
        )

    print(
        "========================================="
    )