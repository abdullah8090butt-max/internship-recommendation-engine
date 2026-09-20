from matching.skill_scorer import TRACK_SKILLS


def analyze_skill_gap(candidate, track_name):
    required_skills = TRACK_SKILLS.get(
        track_name,
        []
    )

    if not required_skills:
        return {
            "matched_skills": [],
            "missing_skills": []
        }

    candidate_skills = [
        skill.lower().strip()
        for skill in candidate.skills
    ]

    matched_skills = []
    missing_skills = []

    for required_skill in required_skills:

        found = False

        for candidate_skill in candidate_skills:

            if (
                required_skill in candidate_skill
                or candidate_skill in required_skill
            ):
                matched_skills.append(
                    required_skill
                )

                found = True
                break

        if not found:
            missing_skills.append(
                required_skill
            )

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }


if __name__ == "__main__":

    test_candidate = type(
        "Candidate",
        (),
        {}
    )()

    test_candidate.skills = [
        "Python",
        "Machine Learning",
        "Artificial Intelligence",
        "Scikit-learn",
        "Generative AI"
    ]

    tracks = [
        "AI / Machine Learning",
        "Data Science",
        "Web Development",
        "Cybersecurity"
    ]

    print(
        "\n========== SKILL GAP ANALYSIS =========="
    )

    for track in tracks:

        result = analyze_skill_gap(
            test_candidate,
            track
        )

        print(f"\n{track}")

        print(
            "Matched Skills:",
            result["matched_skills"]
        )

        print(
            "Missing Skills:",
            result["missing_skills"]
        )

    print(
        "\n========================================"
    )