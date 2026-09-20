# EEF AI-001 — Intelligent Internship Recommendation & Candidate Matching Engine

**Developed by:** Abdullah Butt
**Framework:** Ezitech Engineering Framework (EEF)
**Category:** Artificial Intelligence | Machine Learning | NLP | Recommendation Systems

---

## 🌐 Live Demo

🚀 **Live Streamlit Demo:** Coming soon

🐙 **GitHub Repository:** Coming soon

> The live demo and GitHub repository links will be added after deployment.

---

## 📌 Project Overview

The **EEF AI-001 Intelligent Internship Recommendation & Candidate Matching Engine** is an AI-powered system designed to analyze candidate profiles and recommend suitable internship tracks.

The system evaluates information including:

* Skills
* Education
* Certifications
* Career interests
* Projects
* GitHub profile
* Portfolio
* Resume information

It combines semantic matching and multiple candidate factors to generate internship recommendations, mentor recommendations, skill-gap analysis, personalized learning roadmaps, and explainable recommendations.

---

## 🎯 Objectives

The system is designed to:

* Analyze candidate profiles automatically
* Understand candidate skills and career interests
* Process resume information
* Match candidates with suitable internship tracks
* Recommend compatible mentors
* Identify skill gaps
* Generate personalized learning roadmaps
* Provide explanations for recommendations
* Store candidate and recommendation data
* Provide API access through FastAPI
* Provide an interactive Streamlit interface

---

## ✨ Key Features

### 👤 Candidate Profile

Candidates can provide:

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

### 📄 Resume Processing

The application can process resume information and use it as part of candidate analysis.

### 🧠 AI-Based Semantic Matching

The system uses semantic embeddings to compare candidate information with internship-track descriptions.

### 🎯 Internship Recommendations

The current system supports:

1. AI / Machine Learning
2. Data Science
3. Web Development
4. Cybersecurity

### 👨‍🏫 Mentor Recommendation

Candidates can receive mentor recommendations based on factors such as:

* Expertise
* Semantic similarity
* Track compatibility
* Experience

### 📊 Skill-Gap Analysis

The system identifies skills that candidates may need to develop for their recommended internship direction.

### 🗺️ Personalized Learning Roadmap

The system generates a learning direction based on identified skill gaps.

### 💡 Explainable Recommendations

The system provides an explanation of relevant factors contributing to the recommendation.

### 💾 Database Persistence

Candidate information and generated results can be stored using SQLite and SQLAlchemy.

### ⚡ FastAPI Backend

The project includes a FastAPI backend for programmatic access to the system.

### 🖥️ Streamlit Dashboard

An interactive Streamlit interface allows users to enter their profile and view generated results.

---

## 🏗️ System Architecture

```text
                    Candidate Profile
                           │
                           ▼
                  Data Ingestion
                           │
                           ▼
              Resume & Skill Processing
                           │
                           ▼
                NLP / Embeddings
                           │
                           ▼
                Recommendation Engine
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
     Internship         Mentor          Skill Gap
     Matching           Matching         Analysis
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                Learning Roadmap
                           │
                           ▼
                 AI Explanation
                           │
                           ▼
             Streamlit + FastAPI
                           │
                           ▼
                 SQLite Database
```

---

## 🧰 Technology Stack

### Programming

* Python 3.12

### AI / Machine Learning

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

### GitHub Integration

* PyGithub

---

## 🤖 Embedding Model

The project uses:

```text
sentence-transformers/paraphrase-MiniLM-L3-v2
```

The model converts candidate and internship information into numerical vectors.

These vectors are compared using semantic similarity to determine how closely candidate information relates to available internship tracks.

---

## 🔄 Recommendation Workflow

```text
1. Candidate enters profile information
              ↓
2. Data is cleaned and normalized
              ↓
3. Resume information is processed
              ↓
4. Candidate information is converted into embeddings
              ↓
5. Candidate is compared with internship tracks
              ↓
6. Multiple scoring factors are calculated
              ↓
7. Internship tracks are ranked
              ↓
8. Suitable mentors are identified
              ↓
9. Skill gaps are analyzed
              ↓
10. Learning roadmap is generated
              ↓
11. Recommendation explanation is generated
              ↓
12. Results are stored in the database
```

---

## 📂 Project Structure

```text
internship-recommendation-engine/
│
├── .streamlit/
│   └── config.toml
│
├── api/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   ├── database_routes.py
│   └── recommendation_database_routes.py
│
├── data/
│
├── database/
│   ├── database.py
│   ├── models.py
│   ├── candidate_repository.py
│   ├── mentor_repository.py
│   ├── recommendation_repository.py
│   └── persistence.py
│
├── docs/
│   └── PROJECT_DOCUMENTATION.md
│
├── frontend/
│   └── app.py
│
├── models/
│
├── src/
│   ├── embeddings/
│   ├── matching/
│   ├── nlp/
│   └── recommendation/
│
├── tests/
│
├── .gitignore
├── Procfile
├── README.md
└── requirements.txt
```

---

## 🚀 Local Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Enter the project directory

```bash
cd internship-recommendation-engine
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows:

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

For optimized local startup:

```bash
streamlit run frontend/app.py --server.headless true --browser.gatherUsageStats false --server.fileWatcherType none
```

The application will normally be available at:

```text
http://localhost:8501
```

If that port is already in use, Streamlit may automatically use another available port.

---

## 🔌 Run the FastAPI Backend

```bash
python -m uvicorn api.main:app --host 0.0.0.0 --port 8000
```

The API can then be accessed locally through:

```text
http://localhost:8000
```

---

## 🧪 Testing

The project was evaluated across major components, including:

* Python environment
* Candidate profile processing
* Resume processing
* Skill normalization
* Internship recommendation
* Recommendation scoring
* Mentor recommendation
* Skill-gap analysis
* Learning roadmap
* AI explanation
* Database persistence
* FastAPI backend
* Streamlit frontend
* Multiple candidate scenarios
* Edge cases
* Performance
* Final integration

The testing phase also addressed insufficient candidate information and empty recommendation scenarios.

---

## ⚡ Performance Optimization

The recommendation engine originally experienced unnecessary delays caused by repeated initialization of the Sentence Transformer model.

The project was optimized by centralizing model access through a shared model-loading function.

The model is loaded only when required rather than unnecessarily during initial application startup.

Streamlit startup was also optimized by disabling its file watcher for the local production-style launch command.

---

## 🗄️ Database

The project uses:

```text
SQLite
+
SQLAlchemy
```

The database stores information related to:

* Candidates
* Recommendations
* Mentor recommendations
* Learning roadmaps

---

## 🔐 Security & Deployment Notes

Before public deployment, the project should be checked to ensure that:

* No API keys are committed
* No passwords are committed
* `.env` files are excluded
* Local databases are excluded where appropriate
* Personal information is not exposed
* Personal Windows paths are not required
* Deployment configuration works in a clean environment

---

## ☁️ Deployment

The project is prepared for:

* GitHub repository publication
* Streamlit deployment
* FastAPI deployment

The final public resources will be added here:

### Live Demo

**Streamlit:** Coming soon

### Source Code

**GitHub:** Coming soon

---

## 📸 Screenshots

Screenshots of the Streamlit dashboard will be added after the final live deployment.

---

## 🔮 Future Improvements

Possible future enhancements include:

* Cloud database integration
* More internship categories
* Larger mentor database
* Advanced resume extraction
* More sophisticated recommendation calibration
* User authentication
* Admin dashboard
* Recommendation feedback
* Larger evaluation datasets
* Production monitoring
* Automated CI/CD deployment

---

## 👨‍💻 Developer

### Abdullah Butt

AI & Python Developer

This project demonstrates practical experience in:

* Python
* Artificial Intelligence
* Machine Learning
* Natural Language Processing
* Semantic Matching
* Recommendation Systems
* Vector Embeddings
* FAISS
* FastAPI
* Streamlit
* SQLAlchemy
* SQLite
* Git & GitHub
* AI Application Deployment

---

## 📄 Documentation

Detailed project documentation is available at:

```text
docs/PROJECT_DOCUMENTATION.md
```

---

## 📜 Project

**EEF AI-001 — Intelligent Internship Recommendation & Candidate Matching Engine**

**Developed by Abdullah Butt**

**Ezitech Engineering Framework (EEF)**
