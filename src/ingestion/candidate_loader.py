from candidate_profile import CandidateProfile
from resume_parser import extract_text_from_pdf
from pathlib import Path


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]
    pdf_path = project_root / "data" / "sample_resume.pdf"

    resume_text = extract_text_from_pdf(pdf_path)

    candidate = CandidateProfile(
        name="Test Candidate",
        email="test@example.com",
        resume_text=resume_text
    )

    print(candidate)