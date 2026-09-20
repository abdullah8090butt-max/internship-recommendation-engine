def generate_recommendation_explanation(
    candidate,
    recommended_track
):
    reasons = []

    candidate_skills = [
        skill.lower()
        for skill in candidate.skills
    ]

    track_name = recommended_track["name"].lower()

    if "ai" in track_name or "machine learning" in track_name:
        if "python" in candidate_skills:
            reasons.append("Strong Python skills")

        if "machine learning" in candidate_skills:
            reasons.append("Machine Learning experience")

        if "artificial intelligence" in candidate_skills:
            reasons.append("Artificial Intelligence skills")

    if candidate.projects:
        reasons.append(
            f"{len(candidate.projects)} relevant project(s)"
        )

    if candidate.career_interests:
        reasons.append(
            "Career interests align with this track"
        )

    if candidate.certifications:
        reasons.append(
            "Relevant certification(s)"
        )

    if candidate.education:
        reasons.append(
            "Relevant educational background"
        )

    return reasons


if __name__ == "__main__":
    candidate = type("Candidate", (), {})()

    candidate.skills = [
        "Python",
        "Machine Learning",
        "Artificial Intelligence"
    ]

    candidate.projects = [
        "Medical AI Assistant",
        "Student Data Analysis"
    ]

    candidate.career_interests = [
        "Artificial Intelligence",
        "Machine Learning"
    ]

    candidate.certifications = [
        "AI Fundamentals"
    ]

    candidate.education = [
        "FSc ICS"
    ]

    recommended_track = {
        "name": "AI / Machine Learning"
    }

    reasons = generate_recommendation_explanation(
        candidate,
        recommended_track
    )

    print("\n========== RECOMMENDATION EXPLANATION ==========")
    print("Recommended Track: AI / Machine Learning")
    print("\nWhy this track?")

    for reason in reasons:
        print(f"✓ {reason}")

    print("================================================")