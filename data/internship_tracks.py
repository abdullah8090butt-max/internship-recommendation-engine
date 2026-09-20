INTERNSHIP_TRACKS = [
    {
        "id": 1,
        "name": "AI / Machine Learning",
        "description": (
            "Work on Artificial Intelligence, Machine Learning, "
            "Python, data analysis, model development, and AI applications."
        )
    },
    {
        "id": 2,
        "name": "Data Science",
        "description": (
            "Work on data analysis, statistics, Python, Pandas, "
            "visualization, and machine learning."
        )
    },
    {
        "id": 3,
        "name": "Web Development",
        "description": (
            "Work on web applications, frontend development, "
            "backend development, APIs, and databases."
        )
    },
    {
        "id": 4,
        "name": "Cybersecurity",
        "description": (
            "Work on network security, ethical security practices, "
            "system protection, and cybersecurity tools."
        )
    }
]


if __name__ == "__main__":
    print("========== INTERNSHIP TRACKS ==========")

    for track in INTERNSHIP_TRACKS:
        print(f"\nID: {track['id']}")
        print(f"Name: {track['name']}")
        print(f"Description: {track['description']}")

    print("\n=======================================")