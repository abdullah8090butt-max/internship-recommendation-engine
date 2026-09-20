TRACK_KEYWORDS = {
    "AI / Machine Learning": [
        "ai",
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "python",
        "generative ai",
        "computer vision",
        "nlp"
    ],

    "Data Science": [
        "data science",
        "data analysis",
        "pandas",
        "numpy",
        "statistics",
        "visualization",
        "machine learning",
        "python"
    ],

    "Web Development": [
        "web development",
        "frontend",
        "backend",
        "api",
        "database",
        "javascript",
        "html",
        "css",
        "django",
        "flask"
    ],

    "Cybersecurity": [
        "cybersecurity",
        "network security",
        "ethical hacking",
        "penetration testing",
        "security",
        "linux",
        "networking"
    ]
}


def calculate_relevance_score(items, track_name):
    if not items:
        return 0

    keywords = TRACK_KEYWORDS.get(
        track_name,
        []
    )

    if not keywords:
        return 0

    matched_items = 0

    for item in items:
        item_text = item.lower()

        for keyword in keywords:
            if keyword in item_text:
                matched_items += 1
                break

    score = (
        matched_items / len(items)
    ) * 100

    return round(score, 2)


def calculate_project_score(candidate, track_name):
    return calculate_relevance_score(
        candidate.projects,
        track_name
    )


def calculate_certification_score(
    candidate,
    track_name
):
    return calculate_relevance_score(
        candidate.certifications,
        track_name
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

    test_candidate.certifications = [
        "AI Fundamentals",
        "Python Programming"
    ]

    tracks = [
        "AI / Machine Learning",
        "Data Science",
        "Web Development",
        "Cybersecurity"
    ]

    print(
        "\n========== TRACK RELEVANCE TEST =========="
    )

    for track in tracks:

        project_score = calculate_project_score(
            test_candidate,
            track
        )

        certification_score = (
            calculate_certification_score(
                test_candidate,
                track
            )
        )

        print(f"\n{track}")
        print(
            f"Project Relevance: "
            f"{project_score}%"
        )
        print(
            f"Certification Relevance: "
            f"{certification_score}%"
        )

    print(
        "\n=========================================="
    )