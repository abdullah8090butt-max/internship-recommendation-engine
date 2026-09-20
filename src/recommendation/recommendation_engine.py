from matching.semantic_matcher import (
    generate_candidate_embedding,
    generate_track_embeddings,
    calculate_similarity,
    rank_tracks
)

from matching.similarity_scorer import (
    normalize_similarity_scores
)

from matching.multi_factor_matcher import (
    calculate_final_score
)

from matching.education_scorer import (
    calculate_education_score
)

from matching.portfolio_scorer import (
    calculate_portfolio_score
)

from matching.project_semantic_scorer import (
    calculate_project_semantic_score
)

from matching.certification_semantic_scorer import (
    calculate_certification_semantic_score
)

from matching.skill_scorer import (
    calculate_skill_score
)

from matching.skill_gap_analyzer import (
    analyze_skill_gap
)

from matching.confidence_scorer import (
    calculate_confidence_score
)

from recommendation.recommendation_explainer import (
    generate_recommendation_explanation
)


CAREER_INTEREST_GROUPS = {
    "AI / Machine Learning": [
        "ai",
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "generative ai",
        "computer vision",
        "natural language processing",
        "nlp"
    ],

    "Data Science": [
        "data science",
        "data analysis",
        "data analytics",
        "statistics",
        "visualization",
        "machine learning",
        "python",
        "pandas",
        "numpy"
    ],

    "Web Development": [
        "web development",
        "frontend",
        "backend",
        "full stack",
        "web applications",
        "apis",
        "databases"
    ],

    "Cybersecurity": [
        "cybersecurity",
        "network security",
        "ethical hacking",
        "penetration testing",
        "information security",
        "networking",
        "linux"
    ]
}


def calculate_career_interest_score(
    candidate,
    track_name
):
    if not candidate.career_interests:
        return 0

    interest_keywords = (
        CAREER_INTEREST_GROUPS.get(
            track_name,
            []
        )
    )

    if not interest_keywords:
        return 0

    matched_interests = 0

    for interest in candidate.career_interests:

        interest_text = (
            interest.lower().strip()
        )

        for keyword in interest_keywords:

            if (
                keyword in interest_text
                or interest_text in keyword
            ):
                matched_interests += 1
                break

    score = (
        matched_interests
        / len(candidate.career_interests)
    ) * 100

    return round(score, 2)


def has_meaningful_candidate_data(
    candidate
):
    """
    Check whether the candidate contains
    enough meaningful information to generate
    an AI internship recommendation.
    """

    fields = [
        candidate.skills,
        candidate.education,
        candidate.certifications,
        candidate.career_interests,
        candidate.projects,
        candidate.github_username,
        candidate.portfolio_url,
        getattr(candidate, "resume_text", "")
    ]

    for field in fields:

        if field:

            if isinstance(field, str):

                if field.strip():
                    return True

            elif isinstance(field, (list, tuple, set)):

                if len(field) > 0:
                    return True

            else:
                return True

    return False


def recommend_internship(
    candidate,
    candidate_text
):

    # Prevent recommendation generation
    # for a completely empty candidate profile.
    if not has_meaningful_candidate_data(
        candidate
    ):
        return []

    candidate_embedding = (
        generate_candidate_embedding(
            candidate_text
        )
    )

    track_embeddings = (
        generate_track_embeddings()
    )

    similarities = calculate_similarity(
        candidate_embedding,
        track_embeddings
    )

    ranked_tracks = rank_tracks(
        similarities
    )

    scored_tracks = (
        normalize_similarity_scores(
            ranked_tracks
        )
    )

    final_recommendations = []

    for track in scored_tracks:

        track_name = track["name"]

        skill_score = (
            calculate_skill_score(
                candidate,
                track_name
            )
        )

        semantic_score = (
            track["match_score"]
        )

        project_score = (
            calculate_project_semantic_score(
                candidate,
                track_name
            )
        )

        career_interest_score = (
            calculate_career_interest_score(
                candidate,
                track_name
            )
        )

        education_score = (
            calculate_education_score(
                candidate,
                track_name
            )
        )

        portfolio_score = (
            calculate_portfolio_score(
                candidate,
                track_name
            )
        )

        certification_score = (
            calculate_certification_semantic_score(
                candidate,
                track_name
            )
        )

        final_score = calculate_final_score(
            skill_score,
            semantic_score,
            project_score,
            career_interest_score,
            education_score,
            portfolio_score,
            certification_score
        )

        confidence_score = (
            calculate_confidence_score(
                skill_score,
                semantic_score,
                project_score,
                career_interest_score,
                education_score,
                portfolio_score,
                certification_score
            )
        )

        skill_gap = analyze_skill_gap(
            candidate,
            track_name
        )

        explanation = (
            generate_recommendation_explanation(
                candidate,
                {
                    "name": track_name
                }
            )
        )

        track["skill_score"] = skill_score

        track["semantic_score"] = semantic_score

        track["project_score"] = project_score

        track["career_interest_score"] = (
            career_interest_score
        )

        track["education_score"] = (
            education_score
        )

        track["portfolio_score"] = (
            portfolio_score
        )

        track["certification_score"] = (
            certification_score
        )

        track["matched_skills"] = (
            skill_gap["matched_skills"]
        )

        track["missing_skills"] = (
            skill_gap["missing_skills"]
        )

        track["final_score"] = final_score

        track["confidence_score"] = (
            confidence_score
        )

        track["explanation"] = explanation

        final_recommendations.append(
            track
        )

    final_recommendations.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return final_recommendations


if __name__ == "__main__":

    from pathlib import Path

    from ingestion.profile_builder import (
        build_candidate_profile
    )

    from nlp.skill_normalizer import (
        normalize_skills
    )

    from nlp.candidate_text import (
        create_candidate_text
    )

    project_root = (
        Path(__file__).resolve().parents[2]
    )

    pdf_path = (
        project_root
        / "data"
        / "sample_resume.pdf"
    )

    candidate = build_candidate_profile(
        pdf_path,
        github_username="testuser",
        portfolio_url="https://example.com"
    )

    candidate.skills = normalize_skills(
        candidate.skills
    )

    candidate_text = (
        create_candidate_text(
            candidate
        )
    )

    recommendations = (
        recommend_internship(
            candidate,
            candidate_text
        )
    )

    print(
        "\n========== COMPLETE "
        "RECOMMENDATIONS =========="
    )

    for rank, recommendation in enumerate(
        recommendations,
        start=1
    ):
        print(
            f"\n{rank}. "
            f"{recommendation['name']}"
        )

        print(
            f"Skill Match: "
            f"{recommendation['skill_score']}%"
        )

        print(
            f"Semantic Match: "
            f"{recommendation['semantic_score']}%"
        )

        print(
            f"Semantic Project Relevance: "
            f"{recommendation['project_score']}%"
        )

        print(
            f"Career Interest: "
            f"{recommendation['career_interest_score']}%"
        )

        print(
            f"Education Relevance: "
            f"{recommendation['education_score']}%"
        )

        print(
            f"Portfolio Relevance: "
            f"{recommendation['portfolio_score']}%"
        )

        print(
            f"Semantic Certification Relevance: "
            f"{recommendation['certification_score']}%"
        )

        print(
            f"FINAL SCORE: "
            f"{recommendation['final_score']}%"
        )

        print(
            f"CONFIDENCE SCORE: "
            f"{recommendation['confidence_score']}%"
        )

        print(
            "Matched Skills:",
            recommendation["matched_skills"]
        )

        print(
            "Missing Skills:",
            recommendation["missing_skills"]
        )

        print(
            "Why this track:"
        )

        for reason in recommendation[
            "explanation"
        ]:
            print(
                f"✓ {reason}"
            )

    print(
        "\n=========================================="
    )