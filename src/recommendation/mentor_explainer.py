def explain_mentor_recommendation(
    mentor_name,
    mentor_track,
    final_score,
    expertise_score,
    semantic_score,
    track_score,
    experience_score,
    specialization
):
    """
    Explain why a mentor was recommended
    based on mentor matching factors.
    """

    factors = {

        "Expertise Match": expertise_score,

        "Semantic Match": semantic_score,

        "Track Match": track_score,

        "Experience Score": experience_score
    }

    strong_factors = []

    for factor, score in factors.items():

        if score >= 70:

            strong_factors.append(
                factor
            )

    explanation = {

        "mentor": mentor_name,

        "track": mentor_track,

        "final_score": final_score,

        "specialization": specialization,

        "factors": factors,

        "strong_factors": strong_factors,

        "reason": ""
    }

    if strong_factors:

        factor_text = ", ".join(
            strong_factors
        )

        explanation["reason"] = (
            f"{mentor_name} was recommended "
            f"because the mentor shows strong "
            f"alignment in {factor_text}. "
            f"The mentor's specialization is "
            f"{specialization}. "
            f"The final mentor score is "
            f"{final_score}%."
        )

    else:

        explanation["reason"] = (
            f"{mentor_name} received a "
            f"{final_score}% mentor score "
            f"based on expertise, semantic "
            f"similarity, track alignment, "
            f"and experience."
        )

    return explanation


if __name__ == "__main__":

    mentor_name = "Aamir Khan"

    mentor_track = "AI / Machine Learning"

    final_score = 63.73

    expertise_score = 75.0

    semantic_score = 73.76

    track_score = 33.33

    experience_score = 50.0

    specialization = (
        "Machine Learning and AI Applications"
    )

    explanation = explain_mentor_recommendation(

        mentor_name,

        mentor_track,

        final_score,

        expertise_score,

        semantic_score,

        track_score,

        experience_score,

        specialization
    )

    print(
        "\n========== WHY THIS MENTOR? =========="
    )

    print(
        "Mentor:",
        explanation["mentor"]
    )

    print(
        "Track:",
        explanation["track"]
    )

    print(
        "Final Mentor Score:",
        f"{explanation['final_score']}%"
    )

    print(
        "Specialization:",
        explanation["specialization"]
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
        "\n======================================="
    )