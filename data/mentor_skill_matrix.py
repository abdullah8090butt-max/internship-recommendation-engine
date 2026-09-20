MENTOR_SKILL_MATRIX = {

    "AI / Machine Learning": [
        "Python",
        "Machine Learning",
        "Artificial Intelligence",
        "Deep Learning",
        "Generative AI",
        "Natural Language Processing",
        "Computer Vision",
        "LLMs"
    ],

    "Data Science": [
        "Python",
        "Data Science",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "Statistics",
        "Data Analysis",
        "Data Visualization"
    ],

    "Web Development": [
        "HTML",
        "CSS",
        "JavaScript",
        "Web Development",
        "Frontend",
        "Backend",
        "APIs",
        "Databases"
    ],

    "Cybersecurity": [
        "Cybersecurity",
        "Network Security",
        "Linux",
        "Ethical Hacking",
        "Networking",
        "Penetration Testing",
        "Information Security"
    ]
}


if __name__ == "__main__":

    print(
        "\n========== MENTOR SKILL MATRIX =========="
    )

    for track, skills in MENTOR_SKILL_MATRIX.items():

        print(
            f"\nTrack: {track}"
        )

        print(
            f"Required Mentor Skills: {skills}"
        )

    print(
        "\n========================================="
    )