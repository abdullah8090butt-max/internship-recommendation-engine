MENTORS = [
    {
        "id": 1,
        "name": "Aamir Khan",
        "expertise": [
            "Artificial Intelligence",
            "Machine Learning",
            "Python",
            "Deep Learning"
        ],
        "track": "AI / Machine Learning",
        "experience_years": 5,
        "specialization": "Machine Learning and AI Applications"
    },
    {
        "id": 2,
        "name": "Sara Ahmed",
        "expertise": [
            "Data Science",
            "Python",
            "Pandas",
            "NumPy",
            "Machine Learning"
        ],
        "track": "Data Science",
        "experience_years": 4,
        "specialization": "Data Analysis and Machine Learning"
    },
    {
        "id": 3,
        "name": "Hamza Malik",
        "expertise": [
            "Web Development",
            "HTML",
            "CSS",
            "JavaScript",
            "Backend",
            "APIs"
        ],
        "track": "Web Development",
        "experience_years": 6,
        "specialization": "Full-Stack Web Development"
    },
    {
        "id": 4,
        "name": "Usman Ali",
        "expertise": [
            "Cybersecurity",
            "Network Security",
            "Linux",
            "Ethical Hacking",
            "Networking"
        ],
        "track": "Cybersecurity",
        "experience_years": 7,
        "specialization": "Network Security and Ethical Hacking"
    },
    {
        "id": 5,
        "name": "Fatima Noor",
        "expertise": [
            "Generative AI",
            "Natural Language Processing",
            "Python",
            "Machine Learning",
            "LLMs"
        ],
        "track": "AI / Machine Learning",
        "experience_years": 3,
        "specialization": "Generative AI and NLP"
    }
]


if __name__ == "__main__":

    print(
        "\n========== MENTOR DATA =========="
    )

    for mentor in MENTORS:

        print(
            f"\nID: {mentor['id']}"
        )

        print(
            f"Name: {mentor['name']}"
        )

        print(
            f"Track: {mentor['track']}"
        )

        print(
            f"Expertise: {mentor['expertise']}"
        )

        print(
            f"Experience: "
            f"{mentor['experience_years']} years"
        )

        print(
            f"Specialization: "
            f"{mentor['specialization']}"
        )

    print(
        "\n================================="
    )