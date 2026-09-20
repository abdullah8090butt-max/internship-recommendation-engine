PORTFOLIO_KEYWORDS = {
    "AI / Machine Learning": [
        "ai",
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "generative ai",
        "computer vision",
        "nlp",
        "python"
    ],

    "Data Science": [
        "data science",
        "data analysis",
        "data analytics",
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
        "web application",
        "api",
        "database",
        "javascript",
        "html",
        "css"
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


def calculate_portfolio_score(
    candidate,
    track_name
):
    if not candidate.portfolio_url:
        return 0

    if not candidate.projects:
        return 0

    keywords = PORTFOLIO_KEYWORDS.get(
        track_name,
        []
    )

    if not keywords:
        return 0

    matched_projects = 0

    for project in candidate.projects:

        project_text = project.lower()

        for keyword in keywords:

            if keyword in project_text:
                matched_projects += 1
                break

    score = (
        matched_projects
        / len(candidate.projects)
    ) * 100

    return round(score, 2)


if __name__ == "__main__":

    test_candidate = type(
        "Candidate",
        (),
        {}
    )()

    test_candidate.portfolio_url = (
        "https://example.com"
    )

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
        "\n========== PORTFOLIO RELEVANCE TEST =========="
    )

    for track in tracks:

        score = calculate_portfolio_score(
            test_candidate,
            track
        )

        print(
            f"{track} → "
            f"Portfolio Relevance: {score}%"
        )

    print(
        "\n==============================================="
    )