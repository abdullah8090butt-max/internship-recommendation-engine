TRACK_SKILLS = {
    "AI / Machine Learning": [
        "python",
        "machine learning",
        "artificial intelligence",
        "deep learning",
        "generative ai",
        "computer vision",
        "natural language processing",
        "scikit-learn"
    ],

    "Data Science": [
        "python",
        "pandas",
        "numpy",
        "data science",
        "data analysis",
        "statistics",
        "visualization",
        "machine learning"
    ],

    "Web Development": [
        "html",
        "css",
        "javascript",
        "frontend",
        "backend",
        "api",
        "database",
        "web development"
    ],

    "Cybersecurity": [
        "cybersecurity",
        "network security",
        "ethical hacking",
        "penetration testing",
        "linux",
        "networking",
        "information security"
    ]
}


def calculate_skill_score(
    candidate,
    track_name
):
    if not candidate.skills:
        return 0

    required_skills = TRACK_SKILLS.get(
        track_name,
        []
    )

    if not required_skills:
        return 0

    candidate_skills = [
        skill.lower().strip()
        for skill in candidate.skills
    ]

    matched_skills = 0

    for required_skill in required_skills:

        for candidate_skill in candidate_skills:

            if (
                required_skill in candidate_skill
                or candidate_skill in required_skill
            ):
                matched_skills += 1
                break

    score = (
        matched_skills
        / len(required_skills)
    ) * 100

    return round(
        score,
        2
    )


if __name__ == "__main__":

    test_candidate = type(
        "Candidate",
        (),
        {}
    )()

    test_candidate.skills = [
        "Python",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "Machine Learning",
        "Streamlit",
        "Artificial Intelligence",
        "Generative AI"
    ]

    tracks = [
        "AI / Machine Learning",
        "Data Science",
        "Web Development",
        "Cybersecurity"
    ]

    print(
        "\n========== SKILL-TO-TRACK "
        "MATCHING TEST =========="
    )

    for track in tracks:

        score = calculate_skill_score(
            test_candidate,
            track
        )

        print(
            f"{track} → "
            f"Skill Match Score: "
            f"{score}%"
        )

    print(
        "\n========================================"
    )