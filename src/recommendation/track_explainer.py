def explain_track_recommendation(
    track_name,
    final_score,
    skill_score,
    semantic_score,
    project_score,
    career_interest_score,
    education_score,
    portfolio_score,
    certification_score
):
    """
    Explain why an internship track was recommended
    based on the individual matching factors.
    """

    factors = {

        "Skill Match": skill_score,

        "Semantic Match": semantic_score,

        "Project Relevance": project_score,

        "Career Interest": career_interest_score,

        "Education": education_score,

        "Portfolio": portfolio_score,

        "Certification": certification_score
    }

    strong_factors = []

    for factor, score in factors.items():

        if score >= 70:

            strong_factors.append(
                factor
            )

    explanation = {

        "track": track_name,

        "final_score": final_score,

        "factors": factors,

        "strong_factors": strong_factors,

        "reason": ""
    }

    if strong_factors:

        factor_text = ", ".join(
            strong_factors
        )

        explanation["reason"] = (
            f"The {track_name} track was recommended "
            f"because the candidate shows strong "
            f"alignment in {factor_text}. "
            f"The overall recommendation score is "
            f"{final_score}%."
        )

    else:

        explanation["reason"] = (
            f"The {track_name} track received a "
            f"{final_score}% recommendation score "
            f"based on the combined matching factors."
        )

    return explanation


if __name__ == "__main__":

    track_name = "AI / Machine Learning"

    final_score = 66.4

    skill_score = 80.0

    semantic_score = 90.0

    project_score = 70.0

    career_interest_score = 100.0

    education_score = 80.0

    portfolio_score = 100.0

    certification_score = 90.0

    explanation = explain_track_recommendation(

        track_name,

        final_score,

        skill_score,

        semantic_score,

        project_score,

        career_interest_score,

        education_score,

        portfolio_score,

        certification_score
    )

    print(
        "\n========== WHY THIS INTERNSHIP TRACK? =========="
    )

    print(
        "Track:",
        explanation["track"]
    )

    print(
        "Final Recommendation Score:",
        f"{explanation['final_score']}%"
    )

    print(
        "\nMatching Factors:"
    )

    for factor, score in (
        explanation["factors"].items()
    ):

        print(
            f"- {factor}: {score}%"
        )

    print(
        "\nStrong Factors:"
    )

    for factor in explanation["strong_factors"]:

        print(
            f"- {factor}"
        )

    print(
        "\nReason:"
    )

    print(
        explanation["reason"]
    )

    print(
        "\n================================================="
    )
