from fastapi import APIRouter

from api.schemas import CandidateRequest

from nlp.skill_normalizer import normalize_skills
from nlp.candidate_text import create_candidate_text

from recommendation.recommendation_engine import (
    recommend_internship
)

from matching.mentor_semantic_matcher import (
    match_candidate_with_mentors
)

from recommendation.learning_roadmap import (
    generate_personalized_roadmap
)

from recommendation.track_explainer import (
    explain_track_recommendation
)

from recommendation.strength_analyzer import (
    analyze_strengths
)

from recommendation.weakness_analyzer import (
    analyze_weaknesses,
    create_skill_gap_explanation
)

from recommendation.mentor_explainer import (
    explain_mentor_recommendation
)

from recommendation.final_explanation import (
    generate_final_explanation
)


router = APIRouter()


@router.post("/candidate")
def create_candidate(
    candidate: CandidateRequest
):
    return {
        "message": "Candidate received successfully",
        "candidate": candidate
    }


@router.post("/recommend")
def recommend_candidate(
    candidate: CandidateRequest
):

    candidate.skills = normalize_skills(
        candidate.skills
    )

    candidate_text = create_candidate_text(
        candidate
    )

    recommendations = recommend_internship(
        candidate,
        candidate_text
    )

    # Stop recommendation processing when
    # the candidate profile has no meaningful data.
    if not recommendations:
        return {
            "candidate_name": candidate.name,
            "recommendations": [],
            "mentor_recommendations": [],
            "learning_roadmap": None,
            "explainable_recommendation": None,
            "message": (
                "Insufficient candidate information "
                "to generate recommendations. "
                "Please provide skills, education, "
                "certifications, career interests, "
                "projects, GitHub, portfolio, or resume."
            )
        }

    mentor_results = match_candidate_with_mentors(
        candidate
    )

    top_track = recommendations[0]

    roadmap = generate_personalized_roadmap(
        top_track["missing_skills"],
        top_track["name"]
    )

    track_explanation = explain_track_recommendation(
        top_track["name"],
        top_track["final_score"],
        top_track["skill_score"],
        top_track["semantic_score"],
        top_track["project_score"],
        top_track["career_interest_score"],
        top_track["education_score"],
        top_track["portfolio_score"],
        top_track["certification_score"]
    )

    strengths = analyze_strengths(
        top_track["matched_skills"],
        candidate.projects,
        candidate.certifications,
        candidate.career_interests
    )

    weaknesses = analyze_weaknesses(
        top_track["missing_skills"],
        top_track["name"]
    )

    skill_gap_explanation = (
        create_skill_gap_explanation(
            top_track["missing_skills"],
            top_track["name"]
        )
    )

    top_mentor = mentor_results[0]

    mentor = top_mentor["mentor"]

    mentor_explanation = (
        explain_mentor_recommendation(
            mentor["name"],
            mentor["track"],
            top_mentor["final_score"],
            top_mentor["expertise_score"],
            top_mentor["semantic_score"],
            top_mentor["track_score"],
            top_mentor["experience_score"],
            mentor["specialization"]
        )
    )

    final_explanation = generate_final_explanation(
        track_explanation,
        strengths,
        weaknesses,
        skill_gap_explanation,
        mentor_explanation,
        roadmap["summary"]
    )

    return {
        "candidate_name": candidate.name,
        "recommendations": recommendations,
        "mentor_recommendations": mentor_results,
        "learning_roadmap": roadmap,
        "explainable_recommendation": final_explanation
    }


if __name__ == "__main__":

    print(
        "EEF API routes loaded successfully."
    )