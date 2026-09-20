import re


def extract_email(text):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""


def extract_name(text):
    lines = text.strip().splitlines()

    if lines:
        return lines[0].strip()

    return ""


def extract_skills(text):
    skills_list = [
        "Python",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "Machine Learning",
        "Streamlit",
        "Artificial Intelligence",
        "Generative AI"
    ]

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


def extract_education(text):
    education_keywords = [
        "FSc",
        "ICS",
        "BS",
        "Bachelor",
        "Master",
        "MS",
        "PhD"
    ]

    found_education = []

    for keyword in education_keywords:
        if keyword.lower() in text.lower():
            found_education.append(keyword)

    return found_education


def extract_certifications(text):
    certification_keywords = [
        "AI Fundamentals",
        "Python Programming",
        "Machine Learning",
        "Artificial Intelligence",
        "Data Science",
        "Deep Learning",
        "Generative AI"
    ]

    found_certifications = []

    for certification in certification_keywords:
        if certification.lower() in text.lower():
            found_certifications.append(certification)

    return found_certifications


def extract_career_interests(text):
    career_keywords = [
        "Artificial Intelligence",
        "Machine Learning",
        "Data Science",
        "Generative AI",
        "Computer Vision",
        "Natural Language Processing",
        "Software Development",
        "Web Development",
        "Data Analytics",
        "Cybersecurity"
    ]

    found_interests = []

    for interest in career_keywords:
        if interest.lower() in text.lower():
            found_interests.append(interest)

    return found_interests


def extract_projects(text):
    project_keywords = [
        "Medical AI Assistant",
        "Student Data Analysis",
        "Internship Recommendation Engine",
        "E-commerce Web Scraper",
        "Media Vision",
        "Sama AI Career Coach"
    ]

    found_projects = []

    for project in project_keywords:
        if project.lower() in text.lower():
            found_projects.append(project)

    return found_projects


if __name__ == "__main__":
    sample_text = """
    TEST CANDIDATE
    Email: test@example.com

    Education:
    FSc ICS - Computer Science

    Certifications:
    AI Fundamentals
    Python Programming

    Career Interests:
    Artificial Intelligence
    Machine Learning
    Generative AI

    Skills:
    Python, Pandas, Machine Learning, Streamlit

    Projects:
    Medical AI Assistant
    Student Data Analysis
    Internship Recommendation Engine
    """

    email = extract_email(sample_text)
    name = extract_name(sample_text)
    skills = extract_skills(sample_text)
    education = extract_education(sample_text)
    certifications = extract_certifications(sample_text)
    career_interests = extract_career_interests(sample_text)
    projects = extract_projects(sample_text)

    print("Extracted Email:", email)
    print("Extracted Name:", name)
    print("Extracted Skills:", skills)
    print("Extracted Education:", education)
    print("Extracted Certifications:", certifications)
    print("Extracted Career Interests:", career_interests)
    print("Extracted Projects:", projects)