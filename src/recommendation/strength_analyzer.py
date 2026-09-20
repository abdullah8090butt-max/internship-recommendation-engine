def analyze_strengths(
    matched_skills,
    projects,
    certifications,
    career_interests
):
    """
    Analyze candidate strengths based on
    skills, projects, certifications,
    and career interests.
    """

    strengths = []

    # Technical skill strength
    if matched_skills:

        strengths.append({
            "category": "Technical Skills",
            "details": (
                f"Candidate has {len(matched_skills)} "
                "skills relevant to the recommended track."
            ),
            "items": matched_skills
        })

    # Project strength
    if projects:

        strengths.append({
            "category": "Projects",
            "details": (
                f"Candidate has {len(projects)} "
                "relevant project(s) demonstrating "
                "practical experience."
            ),
            "items": projects
        })

    # Certification strength
    if certifications:

        strengths.append({
            "category": "Certifications",
            "details": (
                f"Candidate has {len(certifications)} "
                "relevant certification(s)."
            ),
            "items": certifications
        })

    # Career interest strength
    if career_interests:

        strengths.append({
            "category": "Career Interests",
            "details": (
                "Candidate's career interests align "
                "with the recommended track."
            ),
            "items": career_interests
        })

    return strengths


if __name__ == "__main__":

    matched_skills = [
        "Python",
        "Machine Learning",
        "Artificial Intelligence",
        "Generative AI",
        "Scikit-learn"
    ]

    projects = [
        "Medical AI Assistant",
        "Student Data Analysis",
        "Internship Recommendation Engine"
    ]

    certifications = [
        "AI Fundamentals"
    ]

    career_interests = [
        "Artificial Intelligence",
        "Machine Learning",
        "Generative AI"
    ]

    strengths = analyze_strengths(
        matched_skills,
        projects,
        certifications,
        career_interests
    )

    print(
        "\n========== CANDIDATE STRENGTH ANALYSIS =========="
    )

    for strength in strengths:

        print(
            f"\nCategory: "
            f"{strength['category']}"
        )

        print(
            f"Details: "
            f"{strength['details']}"
        )

        print(
            "Items:"
        )

        for item in strength["items"]:

            print(
                f"- {item}"
            )

    print(
        "\n================================================="
    )