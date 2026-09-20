# EEF AI-001

## Intelligent Internship Recommendation & Candidate Matching Engine

**Developed by:** Abdullah Butt
**Project Framework:** Ezitech Engineering Framework (EEF)
**Project Category:** Artificial Intelligence / Machine Learning / NLP / Recommendation Systems
**Project Status:** Completed and prepared for deployment

---

## 1. Project Overview

The **EEF AI-001 Intelligent Internship Recommendation & Candidate Matching Engine** is an AI-powered recommendation system designed to analyze candidate profiles and recommend suitable internship tracks.

The system evaluates information such as:

* Skills
* Education
* Certifications
* Career interests
* Projects
* GitHub profile
* Portfolio
* Resume information

Using semantic matching, multi-factor scoring, skill-gap analysis, mentor matching, and personalized learning-roadmap generation, the system produces explainable internship recommendations.

The project is designed as a prototype that can support an internship portal and can be further extended toward production deployment.

---

## 2. Problem Statement

Traditional internship matching can involve manual profile review and subjective decisions.

This can result in:

* Slow candidate evaluation
* Inconsistent recommendations
* Difficulty identifying suitable internship tracks
* Difficulty identifying missing skills
* Limited personalization
* Additional workload for mentors and administrators

The EEF AI-001 system addresses these challenges by applying AI-based candidate analysis and recommendation techniques.

---

## 3. Project Objectives

The main objectives are to:

1. Analyze candidate information automatically.
2. Understand candidate skills and interests.
3. Extract and process information from resumes.
4. Compare candidate profiles with internship tracks.
5. Generate internship recommendations using multiple factors.
6. Recommend suitable mentors.
7. Identify missing or underrepresented skills.
8. Generate a personalized learning roadmap.
9. Provide explanations for recommendations.
10. Store candidate and recommendation data persistently.
11. Provide API access through FastAPI.
12. Provide an interactive user interface through Streamlit.

---

## 4. Main Features

### Candidate Profile Management

The system allows candidates to provide:

* Name
* Email
* Education
* Skills
* Certifications
* Career interests
* Projects
* GitHub username
* Portfolio URL
* Resume information

### Resume Processing

The system can process resume information and use extracted content as part of candidate analysis.

### Skill Normalization

Candidate skills are normalized before recommendation processing so that related or differently formatted skill names can be handled more consistently.

### Internship Recommendation

The recommendation engine evaluates the candidate against multiple internship tracks, including:

* AI / Machine Learning
* Data Science
* Web Development
* Cybersecurity

The system calculates recommendation scores and ranks the available tracks.

### Semantic Matching

The system uses sentence-transformer embeddings to represent candidate and internship information as numerical vectors.

Semantic similarity is then used to measure how closely the candidate's information matches an internship track.

### Multi-Factor Recommendation

Recommendations are not based on a single similarity calculation.

The system combines multiple factors, including:

* Skill matching
* Education
* Projects
* Certifications
* Portfolio
* Career interests
* Semantic similarity
* Candidate profile information

### Mentor Recommendation

The system compares candidates with available mentors using factors such as:

* Expertise
* Semantic similarity
* Internship-track compatibility
* Experience

### Skill-Gap Analysis

The system identifies skills that may be missing or require further development for the recommended internship track.

### Personalized Learning Roadmap

Based on identified skill gaps, the system generates a learning roadmap to help candidates prepare for their recommended internship direction.

### Explainable Recommendations

The system generates an explanation describing relevant factors behind the recommendation rather than presenting only a numerical score.

### Persistent Database

Candidate information and generated recommendations can be stored using a SQLite database through SQLAlchemy.

### FastAPI Backend

The project includes a FastAPI backend providing API endpoints for:

* Candidate data
* Recommendations
* Mentor recommendations
* Learning roadmap data
* Database operations

### Streamlit Dashboard

The project provides an interactive Streamlit frontend through which users can enter their information and generate recommendations.

---

## 5. AI and Technology Stack

### Programming Language

* Python 3.12

### Artificial Intelligence / Machine Learning

* Sentence Transformers
* Natural Language Processing
* Semantic Embeddings
* Cosine Similarity
* Scikit-learn
* FAISS

### Data Processing

* NumPy
* Pandas

### Resume Processing

* PyMuPDF

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Database

* SQLite
* SQLAlchemy

### External Integration

* PyGithub for GitHub-related functionality

---

## 6. System Architecture

The system follows a modular architecture.

```text
                    ┌──────────────────────┐
                    │      Candidate       │
                    │       Profile        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Candidate Data       │
                    │ Ingestion             │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Resume / Skill       │
                    │ Processing            │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Semantic Embeddings  │
                    │ & NLP Processing      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Recommendation       │
                    │ Engine               │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
      Internship Track     Mentor Match     Skill Gap
      Recommendation                       Analysis
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Learning Roadmap &   │
                    │ AI Explanation       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Dashboard  │
                    │ + FastAPI Backend    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Persistent Database  │
                    └──────────────────────┘
```

---

## 7. Recommendation Workflow

The recommendation process follows these general stages:

### Step 1 — Candidate Input

The candidate provides profile information through the Streamlit interface or API.

### Step 2 — Data Processing

Candidate information is cleaned and normalized.

### Step 3 — Candidate Representation

Relevant candidate information is converted into semantic embeddings.

### Step 4 — Internship Track Comparison

Candidate embeddings are compared with internship-track representations.

### Step 5 — Multi-Factor Scoring

Additional factors such as skills, education, projects, certifications, career interests, and portfolio information contribute to the final recommendation.

### Step 6 — Ranking

Available internship tracks are ranked according to their calculated scores.

### Step 7 — Mentor Matching

The system evaluates candidate-to-mentor compatibility.

### Step 8 — Skill-Gap Analysis

The system identifies skills that can be improved for the recommended track.

### Step 9 — Learning Roadmap

A personalized roadmap is generated from the identified skill gaps.

### Step 10 — Explanation

The system generates an explanation of the recommendation.

### Step 11 — Persistence

Candidate and generated recommendation information can be saved in the database.

---

## 8. Semantic Embedding System

The project uses the Sentence Transformers model:

`sentence-transformers/paraphrase-MiniLM-L3-v2`

The model converts text into numerical embeddings.

For example:

```text
Candidate Information
        ↓
Semantic Embedding
        ↓
Numerical Vector
        ↓
Compare with Internship Track Vector
        ↓
Similarity Score
```

Cosine similarity is used to measure semantic closeness between candidate information and internship-track descriptions.

FAISS is also included in the project architecture for efficient vector-based similarity operations.

---

## 9. Recommendation Tracks

The current recommendation engine supports four major internship categories:

| Internship Track      | Example Focus                                                  |
| --------------------- | -------------------------------------------------------------- |
| AI / Machine Learning | AI, ML, Deep Learning, Generative AI, Computer Vision          |
| Data Science          | Data Analysis, Statistics, Pandas, NumPy, Visualization, ML    |
| Web Development       | Frontend, Backend, APIs, Databases, Web Applications           |
| Cybersecurity         | Network Security, Ethical Hacking, Linux, Information Security |

The system evaluates the candidate against these tracks rather than relying only on a single user-selected preference.

---

## 10. Mentor Recommendation

The mentor recommendation component evaluates compatibility between the candidate and available mentors.

The scoring process considers factors such as:

* Mentor expertise
* Candidate-to-mentor semantic similarity
* Internship-track compatibility
* Mentor experience

This allows the system to provide mentor recommendations alongside internship-track recommendations.

---

## 11. Skill-Gap Analysis

After recommendation generation, the system can analyze the difference between the candidate's current skill profile and the requirements associated with the recommended track.

The resulting information can be used to identify areas for improvement.

Example workflow:

```text
Candidate Skills
       +
Recommended Track Requirements
       ↓
Skill Comparison
       ↓
Missing / Development Skills
       ↓
Learning Roadmap
```

---

## 12. Personalized Learning Roadmap

The learning-roadmap component uses the identified skill gaps to generate a structured preparation path.

The purpose of the roadmap is to help candidates understand:

* What skills they should develop
* Which areas need improvement
* What learning direction they can follow
* How their current profile relates to the recommended internship

---

## 13. Explainable AI

The system does not only provide a recommendation score.

It also generates an explanation based on relevant candidate information.

This improves transparency by helping users understand why a particular internship track was recommended.

The explanation can consider factors such as:

* Skills
* Education
* Projects
* Certifications
* Career interests
* Semantic matching

---

## 14. Database Architecture

The project uses SQLite with SQLAlchemy for persistent storage.

The database contains models for information such as:

* Candidates
* Recommendations
* Mentor Recommendations
* Learning Roadmaps

The database layer provides repository and persistence functions for storing and retrieving generated data.

---

## 15. API Architecture

The FastAPI backend provides a programmatic interface to the recommendation system.

The API is organized into modules for:

* Database routes
* Recommendation database routes
* AI/recommendation routes
* Request/response schemas

The backend can be started locally using:

```bash
python -m uvicorn api.main:app --host 0.0.0.0 --port 8000
```

The root health endpoint returns a confirmation that the API and database are running.

---

## 16. Streamlit Frontend

The Streamlit dashboard provides the main interactive user interface.

Users can:

1. Enter candidate information.
2. Upload or provide resume information.
3. Review their candidate profile.
4. Generate internship recommendations.
5. View mentor recommendations.
6. View skill-gap information.
7. View the learning roadmap.
8. Review the AI-generated explanation.

The application is implemented in:

```text
frontend/app.py
```

For faster local startup, the following command can be used:

```bash
streamlit run frontend/app.py --server.headless true --browser.gatherUsageStats false --server.fileWatcherType none
```

---

## 17. Performance Optimization

During development, recommendation generation was initially slowed by repeated loading of the Sentence Transformer model.

The architecture was optimized by centralizing model access through a shared model-loading function.

The model is now loaded lazily rather than being initialized unnecessarily during application startup.

This significantly reduced repeated model initialization during recommendation processing.

The Streamlit startup process was also tested with the file watcher disabled:

```bash
--server.fileWatcherType none
```

This removed the observed startup delay caused by Streamlit's file-watching process during local execution.

---

## 18. Testing and Evaluation

The project was tested across multiple components.

Testing covered:

* Python environment
* Candidate profiles
* Resume processing
* Skill extraction and normalization
* Internship recommendations
* Recommendation scoring
* Mentor recommendations
* Skill-gap analysis
* Learning roadmap
* AI explanations
* Database persistence
* FastAPI backend
* Streamlit frontend
* Multiple candidate scenarios
* Error and edge cases
* Performance
* Final bug fixes

The final testing phase confirmed that the major project components were functioning together.

Edge cases were also handled, including insufficient candidate information and empty recommendation results.

---

## 19. Project Structure

The project is organized into the following major directories:

```text
internship-recommendation-engine/
│
├── .streamlit/
├── api/
├── data/
├── database/
├── docs/
├── frontend/
├── models/
├── src/
├── tests/
│
├── .gitignore
├── Procfile
├── requirements.txt
└── ...
```

### Important Components

```text
api/
    FastAPI backend

database/
    Database models
    Repositories
    Persistence

frontend/
    Streamlit dashboard

src/
    AI and recommendation logic

tests/
    Testing and validation

docs/
    Project documentation
```

---

## 20. Deployment Preparation

The project has been prepared for deployment with:

* Production-oriented FastAPI configuration
* Streamlit configuration
* `requirements.txt`
* `.gitignore`
* `Procfile`
* SQLite database configuration
* Environment/secrets review
* Local deployment validation

The next deployment stage is to publish the project repository to GitHub and deploy the Streamlit frontend as a live application.

---

## 21. GitHub and Live Demo

After final deployment, the project will provide two primary public resources:

### GitHub Repository

**Repository:** To be added after GitHub publication.

### Live Streamlit Demo

**Live Demo:** To be added after Streamlit deployment.

These links will be included in the final README and project presentation so that teachers, reviewers, and other users can access and test the project.

---

## 22. Future Improvements

Possible future development includes:

* Cloud database integration
* More internship categories
* Larger mentor database
* Advanced resume information extraction
* Improved recommendation calibration
* More external job/internship data sources
* User authentication
* Admin dashboard
* Recommendation feedback system
* Model evaluation with larger datasets
* Production-grade monitoring
* Automated deployment pipeline

---

## 23. Developer

**Developed by Abdullah Butt**

This project demonstrates practical experience in:

* Python Development
* Artificial Intelligence
* Machine Learning
* Natural Language Processing
* Semantic Search
* Recommendation Systems
* Vector Embeddings
* FAISS
* FastAPI
* Streamlit
* SQLAlchemy
* SQLite
* Git/GitHub
* AI application deployment

---

## 24. Conclusion

The EEF AI-001 Intelligent Internship Recommendation & Candidate Matching Engine combines artificial intelligence, semantic matching, multi-factor recommendation, mentor matching, skill-gap analysis, personalized learning, explainable AI, database persistence, API integration, and an interactive Streamlit interface into a single application.

The project has progressed from an AI recommendation prototype into a complete application architecture prepared for public GitHub publication and live Streamlit deployment.

**Developer:** Abdullah Butt
**Project:** EEF AI-001 Intelligent Internship Recommendation & Candidate Matching Engine
