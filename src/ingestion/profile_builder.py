from pathlib import Path

from ingestion.candidate_profile import CandidateProfile
from ingestion.resume_parser import extract_text_from_pdf
from ingestion.resume_info_extractor import (
    extract_email,
    extract_name,
    extract_skills,
    extract_education,
    extract_certifications,
    extract_career_interests,
    extract_projects
)


def build_candidate_profile(
    pdf_path,
    github_username="",
    portfolio_url=""
):
    resume_text = extract_text_from_pdf(pdf_path)

    candidate = CandidateProfile(
        name=extract_name(resume_text),
        email=extract_email(resume_text),
        skills=extract_skills(resume_text),
        education=extract_education(resume_text),
        certifications=extract_certifications(resume_text),
        career_interests=extract_career_interests(resume_text),
        projects=extract_projects(resume_text),
        github_username=github_username,
        portfolio_url=portfolio_url,
        resume_text=resume_text
    )

    return candidate


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]

    pdf_path = (
        project_root
        / "data"
        / "sample_resume.pdf"
    )

    candidate = build_candidate_profile(
        pdf_path,
        github_username="testuser",
        portfolio_url="https://example.com"
    )

    print("\n========== CANDIDATE PROFILE ==========")

    print("Name:", candidate.name)
    print("Email:", candidate.email)
    print("Skills:", candidate.skills)
    print("Education:", candidate.education)
    print("Certifications:", candidate.certifications)
    print("Career Interests:", candidate.career_interests)
    print("Projects:", candidate.projects)
    print("GitHub:", candidate.github_username)
    print("Portfolio:", candidate.portfolio_url)

    print("=======================================")