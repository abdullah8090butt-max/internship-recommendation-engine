from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Database directory
DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_DIR.mkdir(exist_ok=True)

# SQLite database URL
DATABASE_URL = f"sqlite:///{DATABASE_DIR / 'eef.db'}"


# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


# Create database session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for database models
Base = declarative_base()


def create_tables():
    """
    Create all EEF database tables.
    """

    from database.models import (
        Candidate,
        Recommendation,
        MentorRecommendation,
        LearningRoadmap
    )

    Base.metadata.create_all(
        bind=engine
    )

    print(
        "All EEF database tables created successfully."
    )


if __name__ == "__main__":
    create_tables()