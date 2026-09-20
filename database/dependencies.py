from database.database import SessionLocal


def get_db():
    """
    Provide a database session
    for FastAPI endpoints.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


if __name__ == "__main__":

    # Test database session creation
    db = SessionLocal()

    try:
        print("Database session created successfully.")

    finally:
        db.close()

    print("Database session closed successfully.")
    print("Step 9.7.2 completed successfully.")