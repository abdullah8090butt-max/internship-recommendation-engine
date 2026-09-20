EDUCATION_KEYWORDS = {
    "AI / Machine Learning": [
        "computer science",
        "artificial intelligence",
        "machine learning",
        "data science",
        "mathematics",
        "ics"
    ],

    "Data Science": [
        "computer science",
        "data science",
        "statistics",
        "mathematics",
        "ics"
    ],

    "Web Development": [
        "computer science",
        "software engineering",
        "information technology",
        "web development",
        "ics"
    ],

    "Cybersecurity": [
        "computer science",
        "cybersecurity",
        "information technology",
        "networking",
        "information security",
        "ics"
    ]
}


def calculate_education_score(
    candidate,
    track_name
):
    if not candidate.education:
        return 0

    keywords = EDUCATION_KEYWORDS.get(
        track_name,
        []
    )

    if not keywords:
        return 0

    education_text = " ".join(
        candidate.education
    ).lower()

    matched_keywords = 0

    for keyword in keywords:
        if keyword in education_text:
            matched_keywords += 1

    if matched_keywords == 0:
        return 0

    score = (
        matched_keywords
        / len(keywords)
    ) * 100

    return round(score, 2)


if __name__ == "__main__":

    test_candidate = type(
        "Candidate",
        (),
        {}
    )()

    test_candidate.education = [
        "FSc ICS",
        "Computer Science"
    ]

    tracks = [
        "AI / Machine Learning",
        "Data Science",
        "Web Development",
        "Cybersecurity"
    ]

    print(
        "\n========== EDUCATION RELEVANCE TEST =========="
    )

    for track in tracks:

        score = calculate_education_score(
            test_candidate,
            track
        )

        print(
            f"{track} → "
            f"Education Relevance: {score}%"
        )

    print(
        "\n=============================================="
    )