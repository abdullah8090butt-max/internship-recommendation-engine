from pathlib import Path

from ingestion.profile_builder import build_candidate_profile
from nlp.skill_normalizer import normalize_skills
from nlp.candidate_text import create_candidate_text

from recommendation.recommendation_engine import (
    recommend_internship
)

from recommendation.recommendation_explainer import (
    generate_recommendation_explanation
)


def run_pipeline(pdf_path):
    # Step 1: Build candidate profile
    candidate = build_candidate_profile(pdf_path)

    # Step 2: Normalize candidate skills
    candidate.skills = normalize_skills(
        candidate.skills
    )

    # Step 3: Create candidate text
    candidate_text = create_candidate_text(
        candidate
    )

    # Step 4: Generate recommendations
    recommendations = recommend_internship(
        candidate_text
    )

    # Step 5: Select best recommendation
    best_recommendation = recommendations[0]

    # Step 6: Generate explanation
    explanation = generate_recommendation_explanation(
        candidate,
        best_recommendation
    )

    return candidate, recommendations, explanation


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]

    pdf_path = (
        project_root
        / "data"
        / "sample_resume.pdf"
    )

    candidate, recommendations, explanation = (
        run_pipeline(pdf_path)
    )

    print("\n========== EEF AI RECOMMENDATION ==========")

    print("\nCandidate:")
    print(candidate.name)
    print(candidate.email)

    print("\nNormalized Skills:")
    print(", ".join(candidate.skills))

    print("\nInternship Recommendations:")

    for rank, recommendation in enumerate(
        recommendations,
        start=1
    ):
        print(
            f"{rank}. {recommendation['name']} "
            f"→ {recommendation['match_score']}%"
        )

    print("\nRecommended Track:")
    print(recommendations[0]["name"])

    print("\nWhy this track?")

    for reason in explanation:
        print(f"✓ {reason}")

    print("\n============================================")