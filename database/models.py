from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import JSON

from database.database import Base


# =========================================================
# CANDIDATE
# =========================================================

class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        nullable=False
    )

    skills = Column(
        JSON,
        default=list
    )

    education = Column(
        JSON,
        default=list
    )

    certifications = Column(
        JSON,
        default=list
    )

    career_interests = Column(
        JSON,
        default=list
    )

    projects = Column(
        JSON,
        default=list
    )

    github_username = Column(
        String(100),
        default=""
    )

    portfolio_url = Column(
        String(300),
        default=""
    )

    resume_text = Column(
        String,
        default=""
    )


# =========================================================
# INTERNSHIP RECOMMENDATION
# =========================================================

class Recommendation(Base):

    __tablename__ = "recommendations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    candidate_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    track_name = Column(
        String(100),
        nullable=False
    )

    final_score = Column(
        Float,
        nullable=False
    )

    confidence_score = Column(
        Float,
        nullable=False
    )

    # Existing stored information
    matched_skills = Column(
        JSON,
        default=list
    )

    missing_skills = Column(
        JSON,
        default=list
    )

    # Additional recommendation engine results
    semantic_score = Column(
        Float,
        default=0
    )

    skill_score = Column(
        Float,
        default=0
    )

    project_score = Column(
        Float,
        default=0
    )

    career_interest_score = Column(
        Float,
        default=0
    )

    education_score = Column(
        Float,
        default=0
    )

    portfolio_score = Column(
        Float,
        default=0
    )

    certification_score = Column(
        Float,
        default=0
    )

    # Full AI explanation
    explanation = Column(
        JSON,
        default=dict
    )


# =========================================================
# MENTOR RECOMMENDATION
# =========================================================

class MentorRecommendation(Base):

    __tablename__ = "mentor_recommendations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    candidate_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    mentor_name = Column(
        String(100),
        nullable=False
    )

    track_name = Column(
        String(100),
        nullable=False
    )

    final_score = Column(
        Float,
        nullable=False
    )

    expertise_score = Column(
        Float,
        default=0
    )

    semantic_score = Column(
        Float,
        default=0
    )

    track_score = Column(
        Float,
        default=0
    )

    experience_score = Column(
        Float,
        default=0
    )

    specialization = Column(
        String(300),
        default=""
    )


# =========================================================
# LEARNING ROADMAP
# =========================================================

class LearningRoadmap(Base):

    __tablename__ = "learning_roadmaps"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    candidate_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    track_name = Column(
        String(100),
        nullable=False
    )

    skill = Column(
        String(100),
        nullable=False
    )

    sequence = Column(
        Integer,
        default=1
    )

    priority = Column(
        String(50),
        default="High"
    )

    stage = Column(
        String(50),
        default="Beginner"
    )

    duration = Column(
        String(50),
        default=""
    )

    resource_type = Column(
        String(200),
        default=""
    )

    milestone = Column(
        String(300),
        default=""
    )

    status = Column(
        String(50),
        default="Not Started"
    )

    progress = Column(
        Float,
        default=0
    )


if __name__ == "__main__":

    print(
        "EEF database models loaded successfully."
    )