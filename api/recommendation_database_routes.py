from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from database.models import Recommendation


router = APIRouter(
    prefix="/database",
    tags=["Recommendations"]
)


@router.post("/recommendations")
def create_recommendation(
    candidate_id: int,
    track_name: str,
    final_score: float,
    confidence_score: float,
    db: Session = Depends(get_db)
):
    """
    Save an internship recommendation
    for a candidate.
    """

    recommendation = Recommendation(
        candidate_id=candidate_id,
        track_name=track_name,
        final_score=final_score,
        confidence_score=confidence_score,
        matched_skills=[],
        missing_skills=[]
    )

    db.add(recommendation)
    db.commit()
    db.refresh(recommendation)

    return {
        "message": "Recommendation saved successfully.",
        "recommendation_id": recommendation.id,
        "candidate_id": recommendation.candidate_id,
        "track_name": recommendation.track_name,
        "final_score": recommendation.final_score,
        "confidence_score": recommendation.confidence_score
    }


@router.get("/recommendations/{candidate_id}")
def get_recommendations(
    candidate_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve recommendation history
    for a candidate.
    """

    recommendations = (
        db.query(Recommendation)
        .filter(
            Recommendation.candidate_id == candidate_id
        )
        .order_by(
            Recommendation.id.desc()
        )
        .all()
    )

    return {
        "candidate_id": candidate_id,
        "total_recommendations": len(recommendations),
        "recommendations": [
            {
                "recommendation_id": recommendation.id,
                "track_name": recommendation.track_name,
                "final_score": recommendation.final_score,
                "confidence_score": recommendation.confidence_score,
                "matched_skills": recommendation.matched_skills,
                "missing_skills": recommendation.missing_skills
            }
            for recommendation in recommendations
        ]
    }


if __name__ == "__main__":

    print(
        "EEF recommendation database API routes loaded successfully."
    )