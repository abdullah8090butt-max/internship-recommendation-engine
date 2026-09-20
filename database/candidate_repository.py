from database.database import SessionLocal, create_tables
from database.models import Candidate


def create_candidate(
    name,
    email,
    skills=None,
    education=None,
    certifications=None,
    career_interests=None,
    projects=None,
    github_username="",
    portfolio_url="",
    resume_text=""
):
    """
    Create and save a candidate in the database.
    """

    db = SessionLocal()

    try:
        candidate = Candidate(
            name=name,
            email=email,
            skills=skills or [],
            education=education or [],
            certifications=certifications or [],
            career_interests=career_interests or [],
            projects=projects or [],
            github_username=github_username,
            portfolio_url=portfolio_url,
            resume_text=resume_text
        )

        db.add(candidate)
        db.commit()
        db.refresh(candidate)

        return candidate

    finally:
        db.close()


def get_candidate(candidate_id):
    """
    Retrieve a candidate by ID.
    """

    db = SessionLocal()

    try:
        candidate = db.get(
            Candidate,
            candidate_id
        )

        return candidate

    finally:
        db.close()


def update_candidate(
    candidate_id,
    name=None,
    email=None,
    skills=None,
    education=None,
    certifications=None,
    career_interests=None,
    projects=None,
    github_username=None,
    portfolio_url=None,
    resume_text=None
):
    """
    Update an existing candidate.
    """

    db = SessionLocal()

    try:
        candidate = db.get(
            Candidate,
            candidate_id
        )

        if candidate is None:
            return None

        if name is not None:
            candidate.name = name

        if email is not None:
            candidate.email = email

        if skills is not None:
            candidate.skills = skills

        if education is not None:
            candidate.education = education

        if certifications is not None:
            candidate.certifications = certifications

        if career_interests is not None:
            candidate.career_interests = career_interests

        if projects is not None:
            candidate.projects = projects

        if github_username is not None:
            candidate.github_username = github_username

        if portfolio_url is not None:
            candidate.portfolio_url = portfolio_url

        if resume_text is not None:
            candidate.resume_text = resume_text

        db.commit()
        db.refresh(candidate)

        return candidate

    finally:
        db.close()


def delete_candidate(candidate_id):
    """
    Delete a candidate from the database.
    """

    db = SessionLocal()

    try:
        candidate = db.get(
            Candidate,
            candidate_id
        )

        if candidate is None:
            return False

        db.delete(candidate)
        db.commit()

        return True

    finally:
        db.close()


if __name__ == "__main__":

    # Make sure database tables exist
    create_tables()

    # Test candidate retrieval
    candidate = get_candidate(1)

    if candidate:

        print("Candidate found.")
        print("Candidate ID:", candidate.id)
        print("Candidate Name:", candidate.name)

        # Delete candidate
        deleted = delete_candidate(1)

        if deleted:
            print("\nCandidate deleted successfully.")

            # Verify deletion
            deleted_candidate = get_candidate(1)

            if deleted_candidate is None:
                print("Deletion verified.")
            else:
                print("Candidate still exists.")

        else:
            print("Candidate could not be deleted.")

    else:
        print("Candidate with ID 1 not found.")