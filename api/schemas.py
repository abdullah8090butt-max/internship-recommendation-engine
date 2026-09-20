from pydantic import BaseModel, Field


class CandidateRequest(BaseModel):
    name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)

    skills: list[str] = Field(default_factory=list)

    education: list[str] = Field(default_factory=list)

    certifications: list[str] = Field(
        default_factory=list
    )

    career_interests: list[str] = Field(
        default_factory=list
    )

    projects: list[str] = Field(
        default_factory=list
    )

    github_username: str = ""

    portfolio_url: str = ""


if __name__ == "__main__":

    candidate = CandidateRequest(
        name="Test Candidate",
        email="test@example.com",
        skills=[
            "Python",
            "Machine Learning"
        ],
        education=[
            "FSc ICS"
        ],
        certifications=[
            "AI Fundamentals"
        ],
        career_interests=[
            "Artificial Intelligence"
        ],
        projects=[
            "Medical AI Assistant"
        ],
        github_username="testuser",
        portfolio_url="https://example.com"
    )

    print(
        "\n========== CANDIDATE API SCHEMA =========="
    )

    print(candidate)

    print(
        "\n==========================================="
    )