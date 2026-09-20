def calculate_confidence_score(
    skill_score,
    semantic_score,
    project_score,
    career_interest_score,
    education_score,
    portfolio_score,
    certification_score
):
    signals = [
        skill_score,
        semantic_score,
        project_score,
        career_interest_score,
        education_score,
        portfolio_score,
        certification_score
    ]

    confidence = sum(signals) / len(signals)

    return round(confidence, 2)


if __name__ == "__main__":

    skill_score = 62.5
    semantic_score = 100.0
    project_score = 31.32
    career_interest_score = 100.0
    education_score = 16.67
    portfolio_score = 33.33
    certification_score = 54.91

    confidence = calculate_confidence_score(
        skill_score,
        semantic_score,
        project_score,
        career_interest_score,
        education_score,
        portfolio_score,
        certification_score
    )

    print(
        "\n========== CONFIDENCE SCORE =========="
    )

    print(
        f"Confidence Score: {confidence}%"
    )

    print(
        "======================================"
    )