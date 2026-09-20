from database.database import SessionLocal, create_tables
from database.models import Recommendation


def create_recommendation(
    candidate_id,
    track_name,
    final_score,
    confidence_score,
    matched_skills=None,
    missing_skills=None
):
    """
    Save an internship recommendation
    for a candidate.
    """

    db = SessionLocal()

    try:
        recommendation = Recommendation(
            candidate_id=candidate_id,
            track_name=track_name,
            final_score=final_score,
            confidence_score=confidence_score,
            matched_skills=matched_skills or [],
            missing_skills=missing_skills or []
        )

        db.add(recommendation)
        db.commit()
        db.refresh(recommendation)

        return recommendation

    finally:
        db.close()


def get_recommendations(candidate_id):
    """
    Retrieve all recommendations for a candidate.
    """

    db = SessionLocal()

    try:
        return (
            db.query(Recommendation)
            .filter(
                Recommendation.candidate_id == candidate_id
            )
            .order_by(Recommendation.id)
            .all()
        )

    finally:
        db.close()


def get_latest_recommendation(candidate_id):
    """
    Retrieve the latest recommendation.
    """

    db = SessionLocal()

    try:
        return (
            db.query(Recommendation)
            .filter(
                Recommendation.candidate_id == candidate_id
            )
            .order_by(Recommendation.id.desc())
            .first()
        )

    finally:
        db.close()


def get_recommendations_by_track(
    candidate_id,
    track_name
):
    """
    Retrieve recommendations for a
    specific candidate and track.
    """

    db = SessionLocal()

    try:
        return (
            db.query(Recommendation)
            .filter(
                Recommendation.candidate_id == candidate_id,
                Recommendation.track_name == track_name
            )
            .order_by(Recommendation.id.desc())
            .all()
        )

    finally:
        db.close()


def delete_recommendation(recommendation_id):
    """
    Delete one recommendation.
    """

    db = SessionLocal()

    try:
        recommendation = db.get(
            Recommendation,
            recommendation_id
        )

        if recommendation is None:
            return False

        db.delete(recommendation)
        db.commit()

        return True

    finally:
        db.close()


def delete_candidate_recommendations(candidate_id):
    """
    Delete all recommendations for a candidate.
    """

    db = SessionLocal()

    try:
        recommendations = (
            db.query(Recommendation)
            .filter(
                Recommendation.candidate_id == candidate_id
            )
            .all()
        )

        count = len(recommendations)

        for recommendation in recommendations:
            db.delete(recommendation)

        db.commit()

        return count

    finally:
        db.close()


if __name__ == "__main__":

    # Make sure tables exist
    create_tables()

    # Clean previous test records
    delete_candidate_recommendations(1)

    print("1. Creating recommendations...")

    first = create_recommendation(
        candidate_id=1,
        track_name="AI / Machine Learning",
        final_score=92.5,
        confidence_score=88.0,
        matched_skills=[
            "Python",
            "Machine Learning",
            "NLP"
        ],
        missing_skills=[
            "Deep Learning"
        ]
    )

    second = create_recommendation(
        candidate_id=1,
        track_name="Data Science",
        final_score=84.5,
        confidence_score=81.0,
        matched_skills=[
            "Python",
            "Pandas",
            "NumPy"
        ],
        missing_skills=[
            "Advanced Statistics"
        ]
    )

    print("   Recommendations created:", 2)

    print("\n2. Reading recommendation history...")

    history = get_recommendations(1)

    print(
        "   Total recommendations:",
        len(history)
    )

    print("\n3. Testing track filter...")

    ai_recommendations = get_recommendations_by_track(
        1,
        "AI / Machine Learning"
    )

    print(
        "   AI / ML recommendations:",
        len(ai_recommendations)
    )

    print("\n4. Testing latest recommendation...")

    latest = get_latest_recommendation(1)

    if latest:
        print(
            "   Latest track:",
            latest.track_name
        )
        print(
            "   Latest score:",
            latest.final_score
        )

    print("\n5. Testing deletion...")

    deleted = delete_recommendation(
        first.id
    )

    print(
        "   Recommendation deleted:",
        deleted
    )

    remaining = get_recommendations(1)

    print(
        "   Remaining recommendations:",
        len(remaining)
    )

    print("\nRecommendation repository test completed successfully.")