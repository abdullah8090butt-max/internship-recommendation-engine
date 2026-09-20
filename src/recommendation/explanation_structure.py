def create_recommendation_explanation(
    track_name,
    final_score,
    matched_skills,
    missing_skills
):
    """
    Create a structured explanation
    for an internship recommendation.
    """

    explanation = {

        "track": track_name,

        "final_score": final_score,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "strengths": [],

        "weaknesses": [],

        "reason": ""
    }

    # Identify candidate strengths
    if matched_skills:

        explanation["strengths"].append(
            "Candidate has relevant skills "
            "for this internship track."
        )

    if len(matched_skills) >= 3:

        explanation["strengths"].append(
            "Candidate has a strong set of "
            "technical skills related to the track."
        )

    # Identify candidate weaknesses
    if missing_skills:

        explanation["weaknesses"].append(
            "Candidate is missing some skills "
            "required for this track."
        )

    # Generate basic recommendation reason
    explanation["reason"] = (
        f"The candidate received a "
        f"{final_score}% recommendation score "
        f"for the {track_name} track based on "
        f"skills, semantic similarity, projects, "
        f"career interests, education, portfolio, "
        f"and certifications."
    )

    return explanation


if __name__ == "__main__":

    track_name = "AI / Machine Learning"

    final_score = 66.4

    matched_skills = [
        "Python",
        "Machine Learning",
        "Artificial Intelligence",
        "Generative AI",
        "Scikit-learn"
    ]

    missing_skills = [
        "Deep Learning",
        "Computer Vision",
        "Natural Language Processing"
    ]

    explanation = create_recommendation_explanation(
        track_name,
        final_score,
        matched_skills,
        missing_skills
    )

    print(
        "\n========== RECOMMENDATION EXPLANATION =========="
    )

    print(
        "Track:",
        explanation["track"]
    )

    print(
        "Final Score:",
        f"{explanation['final_score']}%"
    )

    print(
        "\nMatched Skills:"
    )

    for skill in explanation["matched_skills"]:

        print(
            f"- {skill}"
        )

    print(
        "\nMissing Skills:"
    )

    for skill in explanation["missing_skills"]:

        print(
            f"- {skill}"
        )

    print(
        "\nStrengths:"
    )

    for strength in explanation["strengths"]:

        print(
            f"- {strength}"
        )

    print(
        "\nWeaknesses:"
    )

    for weakness in explanation["weaknesses"]:

        print(
            f"- {weakness}"
        )

    print(
        "\nReason:"
    )

    print(
        explanation["reason"]
    )

    print(
        "\n================================================"
    )