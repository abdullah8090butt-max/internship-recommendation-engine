from database.database import SessionLocal, create_tables
from database.models import MentorRecommendation


def create_mentor_recommendation(
    candidate_id,
    mentor_name,
    track_name,
    final_score,
    expertise_score,
    semantic_score,
    track_score,
    experience_score,
    specialization=""
):
    """
    Save a mentor recommendation
    for a candidate.
    """

    db = SessionLocal()

    try:
        mentor = MentorRecommendation(
            candidate_id=candidate_id,
            mentor_name=mentor_name,
            track_name=track_name,
            final_score=final_score,
            expertise_score=expertise_score,
            semantic_score=semantic_score,
            track_score=track_score,
            experience_score=experience_score,
            specialization=specialization
        )

        db.add(mentor)
        db.commit()
        db.refresh(mentor)

        return mentor

    finally:
        db.close()


def get_mentor_recommendations(candidate_id):
    """
    Retrieve all mentor recommendations
    for a candidate.
    """

    db = SessionLocal()

    try:
        mentors = (
            db.query(MentorRecommendation)
            .filter(
                MentorRecommendation.candidate_id == candidate_id
            )
            .order_by(
                MentorRecommendation.id.desc()
            )
            .all()
        )

        return mentors

    finally:
        db.close()


if __name__ == "__main__":

    # Make sure database tables exist
    create_tables()

    print("Creating mentor recommendations...")

    create_mentor_recommendation(
        candidate_id=1,
        mentor_name="Aamir Jamil",
        track_name="AI / Machine Learning",
        final_score=91.5,
        expertise_score=94.0,
        semantic_score=90.0,
        track_score=92.0,
        experience_score=90.0,
        specialization="AI, Machine Learning, Generative AI"
    )

    create_mentor_recommendation(
        candidate_id=1,
        mentor_name="Sarah Khan",
        track_name="Data Science",
        final_score=86.0,
        expertise_score=88.0,
        semantic_score=85.0,
        track_score=87.0,
        experience_score=84.0,
        specialization="Data Science, Python, Statistics"
    )

    print("\nRetrieving mentor recommendations...")

    mentors = get_mentor_recommendations(1)

    print(
        "Total mentor recommendations:",
        len(mentors)
    )

    for mentor in mentors:
        print("\nMentor ID:", mentor.id)
        print("Mentor Name:", mentor.mentor_name)
        print("Track:", mentor.track_name)
        print("Final Score:", mentor.final_score)

    print("\nStep 9.6.2 completed successfully.")