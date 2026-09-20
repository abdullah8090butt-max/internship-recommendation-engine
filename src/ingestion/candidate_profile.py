from dataclasses import dataclass, field


@dataclass
class CandidateProfile:
    name: str
    email: str
    skills: list[str] = field(default_factory=list)
    education: list[str] = field(default_factory=list)
    certifications: list[str] = field(default_factory=list)
    career_interests: list[str] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)
    github_username: str = ""
    portfolio_url: str = ""
    resume_text: str = ""


if __name__ == "__main__":
    candidate = CandidateProfile(
        name="Test Candidate",
        email="test@example.com",
        skills=["Python", "Pandas", "Machine Learning"],
        education=["FSc ICS"],
        certifications=["AI Fundamentals"],
        career_interests=["Artificial Intelligence"],
        projects=["Medical AI Assistant"],
        github_username="testuser",
        portfolio_url="https://example.com",
        resume_text="Python developer interested in AI and machine learning."
    )

    print(candidate)