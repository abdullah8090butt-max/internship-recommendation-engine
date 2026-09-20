import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from matching.semantic_matcher import get_model


TRACK_DESCRIPTIONS = {
    "AI / Machine Learning": (
        "Artificial Intelligence, Machine Learning, "
        "Deep Learning, Python, Generative AI, "
        "Computer Vision and AI applications"
    ),

    "Data Science": (
        "Data Science, data analysis, statistics, "
        "Python, Pandas, NumPy, visualization "
        "and machine learning"
    ),

    "Web Development": (
        "Web Development, frontend, backend, "
        "web applications, APIs, databases "
        "and web technologies"
    ),

    "Cybersecurity": (
        "Cybersecurity, network security, "
        "ethical hacking, penetration testing, "
        "Linux, networking and information security"
    )
}


def calculate_project_semantic_score(
    candidate,
    track_name
):
    if not candidate.projects:
        return 0

    track_description = TRACK_DESCRIPTIONS.get(
        track_name,
        ""
    )

    if not track_description:
        return 0

    # Reuse the Sentence Transformer model
    # already loaded by semantic_matcher.py.
    model = get_model()

    project_embeddings = model.encode(
        candidate.projects,
        convert_to_numpy=True
    )

    track_embedding = model.encode(
        [track_description],
        convert_to_numpy=True
    )

    similarities = cosine_similarity(
        project_embeddings,
        track_embedding
    ).flatten()

    average_similarity = np.mean(
        similarities
    )

    score = max(
        0,
        average_similarity
    ) * 100

    return round(
        float(score),
        2
    )


if __name__ == "__main__":

    test_candidate = type(
        "Candidate",
        (),
        {}
    )()

    test_candidate.projects = [
        "Medical AI Assistant",
        "Student Data Analysis",
        "Internship Recommendation Engine"
    ]

    tracks = [
        "AI / Machine Learning",
        "Data Science",
        "Web Development",
        "Cybersecurity"
    ]

    print(
        "\n========== SEMANTIC PROJECT "
        "MATCHING TEST =========="
    )

    for track in tracks:

        score = (
            calculate_project_semantic_score(
                test_candidate,
                track
            )
        )

        print(
            f"{track} → "
            f"Semantic Project Score: "
            f"{score}%"
        )

    print(
        "\n=========================================="
    )