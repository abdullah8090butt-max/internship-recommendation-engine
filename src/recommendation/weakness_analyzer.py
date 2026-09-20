def analyze_weaknesses(
    missing_skills,
    track_name
):
    """
    Analyze candidate weaknesses based on
    missing skills required for the track.
    """

    weaknesses = []

    if not missing_skills:

        return weaknesses

    weaknesses.append({

        "category": "Missing Skills",

        "details": (
            f"Candidate is missing "
            f"{len(missing_skills)} skill(s) "
            f"required or useful for the "
            f"{track_name} track."
        ),

        "items": missing_skills
    })

    return weaknesses


def create_skill_gap_explanation(
    missing_skills,
    track_name
):
    """
    Create a clear explanation of the
    candidate's skill gaps.
    """

    if not missing_skills:

        return (
            f"No major skill gaps were identified "
            f"for the {track_name} track."
        )

    skills_text = ", ".join(
        missing_skills
    )

    return (
        f"For the {track_name} track, the "
        f"candidate should strengthen the "
        f"following skills: {skills_text}. "
        f"These skills can be addressed through "
        f"the personalized learning roadmap."
    )


if __name__ == "__main__":

    track_name = "AI / Machine Learning"

    missing_skills = [
        "Deep Learning",
        "Computer Vision",
        "Natural Language Processing"
    ]

    weaknesses = analyze_weaknesses(
        missing_skills,
        track_name
    )

    explanation = create_skill_gap_explanation(
        missing_skills,
        track_name
    )

    print(
        "\n========== CANDIDATE WEAKNESS ANALYSIS =========="
    )

    for weakness in weaknesses:

        print(
            f"\nCategory: "
            f"{weakness['category']}"
        )

        print(
            f"Details: "
            f"{weakness['details']}"
        )

        print(
            "Skill Gaps:"
        )

        for skill in weakness["items"]:

            print(
                f"- {skill}"
            )

    print(
        "\n--------------- SKILL GAP EXPLANATION ---------------"
    )

    print(
        explanation
    )

    print(
        "\n======================================================"
    )