def calculate_final_score(
    skill_score,
    semantic_score,
    project_score,
    career_interest_score,
    education_score,
    portfolio_score,
    certification_score
):
    final_score = (
        skill_score * 0.25
        + semantic_score * 0.25
        + project_score * 0.15
        + career_interest_score * 0.15
        + education_score * 0.10
        + portfolio_score * 0.05
        + certification_score * 0.05
    )

    return round(
        final_score,
        2
    )


if __name__ == "__main__":

    skill_score = 80
    semantic_score = 90
    project_score = 70
    career_interest_score = 100
    education_score = 80
    portfolio_score = 100
    certification_score = 90

    final_score = calculate_final_score(
        skill_score,
        semantic_score,
        project_score,
        career_interest_score,
        education_score,
        portfolio_score,
        certification_score
    )

    print(
        "========== UPDATED FINAL SCORE =========="
    )

    print(
        f"Skill Match: {skill_score}%"
    )

    print(
        f"Semantic Match: {semantic_score}%"
    )

    print(
        f"Project Relevance: {project_score}%"
    )

    print(
        f"Career Interest: {career_interest_score}%"
    )

    print(
        f"Education: {education_score}%"
    )

    print(
        f"Portfolio: {portfolio_score}%"
    )

    print(
        f"Certification: {certification_score}%"
    )

    print("-----------------------------------------")

    print(
        f"Final Recommendation Score: "
        f"{final_score}%"
    )

    print(
        "========================================="
    )