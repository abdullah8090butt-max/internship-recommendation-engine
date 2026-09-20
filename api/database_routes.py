from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.dependencies import get_db
from database.models import Candidate


router = APIRouter(
    prefix="/database",
    tags=["Database"]
)


@router.post("/candidates")
def create_candidate(
    name: str,
    email: str,
    db: Session = Depends(get_db)
):
    """
    Create a candidate in the database.
    """

    candidate = Candidate(
        name=name,
        email=email
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return {
        "message": "Candidate saved successfully.",
        "candidate_id": candidate.id,
        "name": candidate.name,
        "email": candidate.email
    }


@router.get("/candidates/{candidate_id}")
def get_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):
    """
    Retrieve a candidate from the database.
    """

    candidate = db.get(
        Candidate,
        candidate_id
    )

    if candidate is None:
        return {
            "message": "Candidate not found."
        }

    return {
        "candidate_id": candidate.id,
        "name": candidate.name,
        "email": candidate.email,
        "skills": candidate.skills,
        "education": candidate.education,
        "certifications": candidate.certifications,
        "career_interests": candidate.career_interests,
        "projects": candidate.projects,
        "github_username": candidate.github_username,
        "portfolio_url": candidate.portfolio_url
    }


if __name__ == "__main__":

    print(
        "EEF database API routes loaded successfully."
    )