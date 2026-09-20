SKILL_ALIASES = {
    "ml": "Machine Learning",
    "machine learning": "Machine Learning",
    "ai": "Artificial Intelligence",
    "artificial intelligence": "Artificial Intelligence",
    "sklearn": "Scikit-learn",
    "scikit learn": "Scikit-learn",
    "np": "NumPy",
    "numpy": "NumPy",
    "pd": "Pandas",
    "pandas": "Pandas",
    "python programming": "Python",
    "python": "Python"
}


def normalize_skill(skill):
    skill = skill.strip().lower()

    return SKILL_ALIASES.get(skill, skill.title())


def normalize_skills(skills):
    normalized_skills = []

    for skill in skills:
        normalized_skill = normalize_skill(skill)

        if normalized_skill not in normalized_skills:
            normalized_skills.append(normalized_skill)

    return normalized_skills


if __name__ == "__main__":
    test_skills = [
        "Python",
        "ML",
        "AI",
        "sklearn",
        "np",
        "pd",
        "Python Programming",
        "AI"
    ]

    normalized_skills = normalize_skills(test_skills)

    print("Original Skills:", test_skills)
    print("Normalized Skills:", normalized_skills)