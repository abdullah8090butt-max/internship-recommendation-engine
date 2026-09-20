import pymupdf
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    document = pymupdf.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[2]
    pdf_path = project_root / "data" / "sample_resume.pdf"

    resume_text = extract_text_from_pdf(pdf_path)

    print(resume_text)