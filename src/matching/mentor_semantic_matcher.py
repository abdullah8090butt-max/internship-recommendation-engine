from pathlib import Path

from sklearn.metrics.pairwise import cosine_similarity

from data.mentors import MENTORS
from embeddings.mentor_embeddings import create_mentor_text
from ingestion.profile_builder import build_candidate_profile
from nlp.candidate_normalizer import normalize_candidate_skills

from matching.semantic_matcher import get_model

from matching.mentor_score import (
    calculate_expertise_score,
    calculate_track_score,
    calculate_experience_score,
    calculate_mentor_score
)


def create_candidate_text(candidate):
    """
    Convert candidate profile into text
    for semantic mentor matching.
    """

    sections = []

    if candidate.skills:

        sections.append(
            "Skills: " +
            ", ".join(candidate.skills)
        )

    if candidate.education:

        sections.append(
            "Education: " +
            ", ".join(candidate.education)
        )

    if candidate.career_interests:

        sections.append(
            "Career Interests: " +
            ", ".join(candidate.career_interests)
        )

    if candidate.projects:

        sections.append(
            "Projects: " +
            ", ".join(candidate.projects)
        )

    return "\n".join(sections)


def match_candidate_with_mentors(candidate):
    """
    Generate mentor recommendations for a candidate.

    The final mentor score is calculated using:

    - Expertise Match: 35%
    - Semantic Match: 35%
    - Track Match: 20%
    - Experience Score: 10%
    """

    model = get_model()

    candidate_text = create_candidate_text(
        candidate
    )

    candidate_embedding = model.encode(
        [candidate_text]
    )

    mentor_texts = []

    for mentor in MENTORS:

        mentor_text = create_mentor_text(
            mentor
        )

        mentor_texts.append(
            mentor_text
        )

    mentor_embeddings = model.encode(
        mentor_texts
    )

    similarities = cosine_similarity(
        candidate_embedding,
        mentor_embeddings
    )[0]

    results = []

    for index, score in enumerate(
        similarities
    ):

        mentor = MENTORS[index]

        semantic_score = (
            float(score) * 100
        )

        expertise_score = (
            calculate_expertise_score(
                candidate,
                mentor
            )
        )

        track_score = (
            calculate_track_score(
                candidate,
                mentor
            )
        )

        experience_score = (
            calculate_experience_score(
                mentor
            )
        )

        final_score = calculate_mentor_score(
            expertise_score,
            semantic_score,
            track_score,
            experience_score
        )

        results.append({

            "mentor": mentor,

            "semantic_score": round(
                semantic_score,
                2
            ),

            "expertise_score": round(
                expertise_score,
                2
            ),

            "track_score": round(
                track_score,
                2
            ),

            "experience_score": round(
                experience_score,
                2
            ),

            "final_score": round(
                final_score,
                2
            )
        })

    results.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return results


if __name__ == "__main__":

    project_root = Path(
        __file__
    ).resolve().parents[2]

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

    candidate = normalize_candidate_skills(
        candidate
    )

    results = match_candidate_with_mentors(
        candidate
    )

    print(
        "\n========== FINAL MENTOR RECOMMENDATIONS =========="
    )

    for index, result in enumerate(
        results,
        start=1
    ):

        mentor = result["mentor"]

        print(
            f"\n{index}. "
            f"{mentor['name']}"
        )

        print(
            f"Track: "
            f"{mentor['track']}"
        )

        print(
            f"Expertise Match: "
            f"{result['expertise_score']}%"
        )

        print(
            f"Semantic Match: "
            f"{result['semantic_score']}%"
        )

        print(
            f"Track Match: "
            f"{result['track_score']}%"
        )

        print(
            f"Experience Score: "
            f"{result['experience_score']}%"
        )

        print(
            f"FINAL MENTOR SCORE: "
            f"{result['final_score']}%"
        )

        print(
            f"Specialization: "
            f"{mentor['specialization']}"
        )

    print(
        "\n=================================================="
    )