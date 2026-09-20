import fitz

pdf = fitz.open()

page = pdf.new_page()

text = """
TEST CANDIDATE

Email: test@example.com

Skills:
Python, Pandas, NumPy, Scikit-learn, Machine Learning, Streamlit

Education:
FSc ICS - Computer Science

Certifications:
AI Fundamentals
Python Programming

Career Interests:
Artificial Intelligence
Machine Learning
Generative AI

Projects:
Medical AI Assistant
Student Data Analysis
Internship Recommendation Engine

Profile:
Python developer interested in Artificial Intelligence and Machine Learning.
Experienced in data analysis and building small AI applications.
"""

page.insert_text((50, 50), text)

pdf.save("sample_resume.pdf")

pdf.close()

print("Test PDF created successfully!")