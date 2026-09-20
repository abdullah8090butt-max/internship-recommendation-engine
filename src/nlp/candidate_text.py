def create_candidate_text(candidate):
    sections = []

    if candidate.skills:
        sections.append(
            "Skills: " + ", ".join(candidate.skills)
        )

    if candidate.education:
        sections.append(
            "Education: " + ", ".join(candidate.education)
        )

    if candidate.certifications:
        sections.append(
            "Certifications: " + ", ".join(candidate.certifications)
        )

    if candidate.career_interests:
        sections.append(
            "Career Interests: " + ", ".join(candidate.career_interests)
        )

    if candidate.projects:
        sections.append(
            "Projects: " + ", ".join(candidate.projects)
        )

    return "\n".join(sections)


if __name__ == "__main__":
    test_candidate = type("Candidate", (), {})()

    test_candidate.skills = [
        "Python",
        "Machine Learning",
        "Artificial Intelligence"
    ]

    test_candidate.education = [
        "FSc ICS"
    ]

    test_candidate.certifications = [
        "AI Fundamentals"
    ]

    test_candidate.career_interests = [
        "Artificial Intelligence",
        "Generative AI"
    ]

    test_candidate.projects = [
        "Medical AI Assistant",
        "Student Data Analysis"
    ]

    candidate_text = create_candidate_text(test_candidate)

    print("========== CANDIDATE TEXT ==========")
    print(candidate_text)
    print("====================================")