from database.database import SessionLocal
from database.models import (
    Candidate,
    Recommendation,
    MentorRecommendation,
    LearningRoadmap
)


# =========================================================
# CANDIDATE STORAGE
# =========================================================

def save_candidate(candidate_data):

    db = SessionLocal()

    try:

        candidate = Candidate(
            name=candidate_data.get(
                "name",
                ""
            ),

            email=candidate_data.get(
                "email",
                ""
            ),

            skills=candidate_data.get(
                "skills",
                []
            ),

            education=candidate_data.get(
                "education",
                []
            ),

            certifications=candidate_data.get(
                "certifications",
                []
            ),

            career_interests=candidate_data.get(
                "career_interests",
                []
            ),

            projects=candidate_data.get(
                "projects",
                []
            ),

            github_username=candidate_data.get(
                "github_username",
                ""
            ),

            portfolio_url=candidate_data.get(
                "portfolio_url",
                ""
            ),

            resume_text=candidate_data.get(
                "resume_text",
                ""
            )
        )

        db.add(candidate)
        db.commit()
        db.refresh(candidate)

        return candidate.id

    finally:

        db.close()


# =========================================================
# GET CANDIDATE
# =========================================================

def get_saved_candidate(candidate_id):

    db = SessionLocal()

    try:

        return db.get(
            Candidate,
            candidate_id
        )

    finally:

        db.close()


# =========================================================
# SAVE INTERNSHIP RECOMMENDATIONS
# =========================================================

def save_recommendations(
    candidate_id,
    recommendations
):

    db = SessionLocal()

    try:

        db.query(
            Recommendation
        ).filter(
            Recommendation.candidate_id
            == candidate_id
        ).delete()

        db.commit()

        for result in recommendations:

            recommendation = Recommendation(

                candidate_id=candidate_id,

                track_name=result.get(
                    "name",
                    result.get(
                        "track_name",
                        ""
                    )
                ),

                final_score=float(
                    result.get(
                        "final_score",
                        0
                    )
                ),

                confidence_score=float(
                    result.get(
                        "confidence_score",
                        0
                    )
                ),

                matched_skills=result.get(
                    "matched_skills",
                    []
                ),

                missing_skills=result.get(
                    "missing_skills",
                    []
                ),

                semantic_score=float(
                    result.get(
                        "semantic_score",
                        0
                    )
                ),

                skill_score=float(
                    result.get(
                        "skill_score",
                        0
                    )
                ),

                project_score=float(
                    result.get(
                        "project_score",
                        0
                    )
                ),

                career_interest_score=float(
                    result.get(
                        "career_interest_score",
                        0
                    )
                ),

                education_score=float(
                    result.get(
                        "education_score",
                        0
                    )
                ),

                portfolio_score=float(
                    result.get(
                        "portfolio_score",
                        0
                    )
                ),

                certification_score=float(
                    result.get(
                        "certification_score",
                        0
                    )
                ),

                explanation=result.get(
                    "explanation",
                    []
                )
            )

            db.add(
                recommendation
            )

        db.commit()

        return get_saved_recommendations(
            candidate_id
        )

    finally:

        db.close()


# =========================================================
# LOAD INTERNSHIP RECOMMENDATIONS
# =========================================================

def get_saved_recommendations(
    candidate_id
):

    db = SessionLocal()

    try:

        records = (
            db.query(
                Recommendation
            )
            .filter(
                Recommendation.candidate_id
                == candidate_id
            )
            .order_by(
                Recommendation.final_score.desc()
            )
            .all()
        )

        recommendations = []

        for record in records:

            recommendations.append({

                "name": record.track_name,

                "track_name": record.track_name,

                "final_score": record.final_score,

                "confidence_score": (
                    record.confidence_score
                ),

                "matched_skills": (
                    record.matched_skills or []
                ),

                "missing_skills": (
                    record.missing_skills or []
                ),

                "semantic_score": (
                    record.semantic_score or 0
                ),

                "skill_score": (
                    record.skill_score or 0
                ),

                "project_score": (
                    record.project_score or 0
                ),

                "career_interest_score": (
                    record.career_interest_score or 0
                ),

                "education_score": (
                    record.education_score or 0
                ),

                "portfolio_score": (
                    record.portfolio_score or 0
                ),

                "certification_score": (
                    record.certification_score or 0
                ),

                "explanation": (
                    record.explanation or []
                )
            })

        return recommendations

    finally:

        db.close()


# =========================================================
# SAVE MENTOR RECOMMENDATIONS
# =========================================================

def save_mentor_recommendations(
    candidate_id,
    mentor_results
):

    db = SessionLocal()

    try:

        db.query(
            MentorRecommendation
        ).filter(
            MentorRecommendation.candidate_id
            == candidate_id
        ).delete()

        db.commit()

        for result in mentor_results:

            mentor = result.get(
                "mentor",
                {}
            )

            record = MentorRecommendation(

                candidate_id=candidate_id,

                mentor_name=mentor.get(
                    "name",
                    result.get(
                        "mentor_name",
                        ""
                    )
                ),

                track_name=mentor.get(
                    "track",
                    result.get(
                        "track_name",
                        ""
                    )
                ),

                final_score=float(
                    result.get(
                        "final_score",
                        0
                    )
                ),

                expertise_score=float(
                    result.get(
                        "expertise_score",
                        0
                    )
                ),

                semantic_score=float(
                    result.get(
                        "semantic_score",
                        0
                    )
                ),

                track_score=float(
                    result.get(
                        "track_score",
                        0
                    )
                ),

                experience_score=float(
                    result.get(
                        "experience_score",
                        0
                    )
                ),

                specialization=mentor.get(
                    "specialization",
                    result.get(
                        "specialization",
                        ""
                    )
                )
            )

            db.add(record)

        db.commit()

        return get_saved_mentor_recommendations(
            candidate_id
        )

    finally:

        db.close()


# =========================================================
# LOAD MENTOR RECOMMENDATIONS
# =========================================================

def get_saved_mentor_recommendations(
    candidate_id
):

    db = SessionLocal()

    try:

        records = (
            db.query(
                MentorRecommendation
            )
            .filter(
                MentorRecommendation.candidate_id
                == candidate_id
            )
            .order_by(
                MentorRecommendation.final_score.desc()
            )
            .all()
        )

        mentor_results = []

        for record in records:

            mentor_results.append({

                "mentor": {

                    "name": record.mentor_name,

                    "track": record.track_name,

                    "specialization": (
                        record.specialization or ""
                    )
                },

                "final_score": record.final_score,

                "expertise_score": (
                    record.expertise_score or 0
                ),

                "semantic_score": (
                    record.semantic_score or 0
                ),

                "track_score": (
                    record.track_score or 0
                ),

                "experience_score": (
                    record.experience_score or 0
                )
            })

        return mentor_results

    finally:

        db.close()


# =========================================================
# SAVE LEARNING ROADMAP
# =========================================================

def save_learning_roadmap(
    candidate_id,
    track_name,
    roadmap
):

    db = SessionLocal()

    try:

        db.query(
            LearningRoadmap
        ).filter(
            LearningRoadmap.candidate_id
            == candidate_id
        ).delete()

        db.commit()

        # The roadmap generator returns:
        #
        # {
        #     "track": ...,
        #     "roadmap": [...],
        #     "summary": {...},
        #     "total_duration_weeks": ...
        # }

        if isinstance(
            roadmap,
            dict
        ):

            roadmap_items = roadmap.get(
                "roadmap",
                []
            )

        else:

            roadmap_items = roadmap or []

        for index, item in enumerate(
            roadmap_items,
            start=1
        ):

            record = LearningRoadmap(

                candidate_id=candidate_id,

                track_name=track_name,

                skill=item.get(
                    "skill",
                    item.get(
                        "name",
                        ""
                    )
                ),

                sequence=item.get(
                    "sequence",
                    index
                ),

                priority=item.get(
                    "priority",
                    "High"
                ),

                stage=item.get(
                    "stage",
                    "Beginner"
                ),

                duration=item.get(
                    "duration",
                    ""
                ),

                resource_type=item.get(
                    "resource_type",
                    item.get(
                        "resource",
                        ""
                    )
                ),

                milestone=item.get(
                    "milestone",
                    ""
                ),

                status=item.get(
                    "status",
                    "Not Started"
                ),

                progress=float(
                    item.get(
                        "progress",
                        0
                    )
                )
            )

            db.add(record)

        db.commit()

        return get_saved_learning_roadmap(
            candidate_id
        )

    finally:

        db.close()


# =========================================================
# LOAD LEARNING ROADMAP
# =========================================================

def get_saved_learning_roadmap(
    candidate_id
):

    db = SessionLocal()

    try:

        records = (
            db.query(
                LearningRoadmap
            )
            .filter(
                LearningRoadmap.candidate_id
                == candidate_id
            )
            .order_by(
                LearningRoadmap.sequence.asc()
            )
            .all()
        )

        roadmap_items = []

        for record in records:

            roadmap_items.append({

                "skill": record.skill,

                "track": record.track_name,

                "sequence": record.sequence,

                "priority": record.priority,

                "stage": record.stage,

                "duration": record.duration,

                "resource_type": (
                    record.resource_type
                ),

                "milestone": record.milestone,

                "status": record.status,

                "progress": record.progress
            })

        return roadmap_items

    finally:

        db.close()


# =========================================================
# DELETE ALL GENERATED DATA FOR CANDIDATE
# =========================================================

def clear_candidate_generated_data(
    candidate_id
):

    db = SessionLocal()

    try:

        db.query(
            Recommendation
        ).filter(
            Recommendation.candidate_id
            == candidate_id
        ).delete()

        db.query(
            MentorRecommendation
        ).filter(
            MentorRecommendation.candidate_id
            == candidate_id
        ).delete()

        db.query(
            LearningRoadmap
        ).filter(
            LearningRoadmap.candidate_id
            == candidate_id
        ).delete()

        db.commit()

    finally:

        db.close()


# =========================================================
# DATABASE TEST
# =========================================================

if __name__ == "__main__":

    print(
        "EEF persistence module loaded successfully."
    )