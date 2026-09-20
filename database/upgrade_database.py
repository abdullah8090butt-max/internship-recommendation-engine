from sqlalchemy import text

from database.database import engine


def add_column_if_missing(
    table_name,
    column_name,
    column_definition
):

    with engine.connect() as connection:

        columns = connection.execute(
            text(
                f"PRAGMA table_info({table_name})"
            )
        ).fetchall()

        existing_columns = [
            column[1]
            for column in columns
        ]

        if column_name not in existing_columns:

            connection.execute(
                text(
                    f"""
                    ALTER TABLE {table_name}
                    ADD COLUMN {column_name}
                    {column_definition}
                    """
                )
            )

            connection.commit()

            print(
                f"Added column: "
                f"{table_name}.{column_name}"
            )


def upgrade_database():

    recommendation_columns = {

        "semantic_score":
            "FLOAT DEFAULT 0",

        "skill_score":
            "FLOAT DEFAULT 0",

        "project_score":
            "FLOAT DEFAULT 0",

        "career_interest_score":
            "FLOAT DEFAULT 0",

        "education_score":
            "FLOAT DEFAULT 0",

        "portfolio_score":
            "FLOAT DEFAULT 0",

        "certification_score":
            "FLOAT DEFAULT 0",

        "explanation":
            "JSON"
    }

    for column_name, definition in (
        recommendation_columns.items()
    ):

        add_column_if_missing(
            "recommendations",
            column_name,
            definition
        )

    print(
        "\nEEF database upgrade completed successfully."
    )


if __name__ == "__main__":

    upgrade_database()