import sys
import re
from pathlib import Path

import fitz
import streamlit as st


# ============================================================
# PATH CONFIGURATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


# ============================================================
# DATABASE IMPORTS
# ============================================================

from database.candidate_repository import (
    create_candidate,
    get_candidate,
    update_candidate
)

from database.persistence import (
    save_recommendations,
    get_saved_recommendations,
    save_mentor_recommendations,
    get_saved_mentor_recommendations,
    save_learning_roadmap,
    get_saved_learning_roadmap
)

from database.models import (
    Candidate,
    Recommendation,
    MentorRecommendation,
    LearningRoadmap
)

from database.database import (
    SessionLocal,
    create_tables
)


# ============================================================
# AI / NLP IMPORTS
# ============================================================

from nlp.skill_normalizer import normalize_skills
from nlp.candidate_text import create_candidate_text

from recommendation.recommendation_engine import (
    recommend_internship
)

from matching.mentor_semantic_matcher import (
    match_candidate_with_mentors
)

from recommendation.learning_roadmap import (
    generate_personalized_roadmap
)

from recommendation.track_explainer import (
    explain_track_recommendation
)

from recommendation.strength_analyzer import (
    analyze_strengths
)

from recommendation.weakness_analyzer import (
    analyze_weaknesses,
    create_skill_gap_explanation
)

from recommendation.final_explanation import (
    generate_final_explanation
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="EEF AI Internship Recommendation Engine",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# DATABASE INITIALIZATION
# ============================================================

try:
    create_tables()

except Exception as error:

    st.error(
        f"Database initialization failed: {error}"
    )

    st.stop()


# ============================================================
# PROFESSIONAL UI STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------------------------------
       GLOBAL
    -------------------------------------------------------- */

    .main {
        padding-top: 1.5rem;
    }

    .block-container {
        max-width: 1400px;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* --------------------------------------------------------
       SIDEBAR
    -------------------------------------------------------- */

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.18);
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }

    /* --------------------------------------------------------
       HEADER
    -------------------------------------------------------- */

    .eef-header {
        padding: 1.4rem 1.6rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(128, 128, 128, 0.18);
        background: rgba(128, 128, 128, 0.05);
    }

    .eef-header h1 {
        margin-bottom: 0.25rem;
        font-size: 2rem;
    }

    .eef-header p {
        margin: 0;
        opacity: 0.75;
        font-size: 1rem;
    }

    /* --------------------------------------------------------
       METRIC CARDS
    -------------------------------------------------------- */

    .metric-card {
        padding: 1.2rem;
        border-radius: 14px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        background: rgba(128, 128, 128, 0.04);
        min-height: 120px;
    }

    .metric-title {
        font-size: 0.85rem;
        opacity: 0.7;
        margin-bottom: 0.4rem;
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .metric-description {
        font-size: 0.78rem;
        opacity: 0.65;
    }

    /* --------------------------------------------------------
       SECTION CARDS
    -------------------------------------------------------- */

    .section-card {
        padding: 1.25rem;
        border-radius: 14px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        background: rgba(128, 128, 128, 0.035);
        margin-bottom: 1rem;
    }

    .section-card h3 {
        margin-top: 0;
    }

    /* --------------------------------------------------------
       STATUS
    -------------------------------------------------------- */

    .status-item {
        padding: 0.9rem 1rem;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.16);
        background: rgba(128, 128, 128, 0.035);
        text-align: center;
    }

    /* --------------------------------------------------------
       PIPELINE
    -------------------------------------------------------- */

    .pipeline-step {
        padding: 0.8rem;
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.16);
        text-align: center;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
    }

    /* --------------------------------------------------------
       SCORE BADGE
    -------------------------------------------------------- */

    .score-badge {
        display: inline-block;
        padding: 0.35rem 0.7rem;
        border-radius: 999px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        font-weight: 600;
        font-size: 0.85rem;
    }

    /* --------------------------------------------------------
       RESUME SCORE
    -------------------------------------------------------- */

    .resume-score-card {
        padding: 1.25rem;
        border-radius: 16px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        background: rgba(128, 128, 128, 0.045);
        margin: 0.75rem 0 1rem 0;
    }

    .resume-score-title {
        font-size: 0.9rem;
        opacity: 0.7;
        margin-bottom: 0.25rem;
    }

    .resume-score-value {
        font-size: 2.3rem;
        font-weight: 750;
        margin-bottom: 0.25rem;
    }

    .resume-score-description {
        font-size: 0.82rem;
        opacity: 0.7;
    }

    .resume-upload-card {
        padding: 1rem;
        border-radius: 14px;
        border: 1px dashed rgba(128, 128, 128, 0.3);
        background: rgba(128, 128, 128, 0.025);
        margin-bottom: 1rem;
    }

    /* --------------------------------------------------------
       RESUME ANALYSIS
    -------------------------------------------------------- */

    .resume-analysis-card {
        padding: 1.1rem;
        border-radius: 14px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        background: rgba(128, 128, 128, 0.035);
        margin-bottom: 1rem;
    }

    .resume-analysis-title {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .resume-analysis-description {
        font-size: 0.82rem;
        opacity: 0.7;
    }

    /* --------------------------------------------------------
       INFO BOX
    -------------------------------------------------------- */

    .info-box {
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.18);
        background: rgba(128, 128, 128, 0.035);
        margin-bottom: 1rem;
    }

    /* --------------------------------------------------------
       FOOTER
    -------------------------------------------------------- */

    .eef-footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        opacity: 0.55;
        font-size: 0.8rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "current_candidate_id" not in st.session_state:
    st.session_state.current_candidate_id = 7

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

if "mentor_recommendations" not in st.session_state:
    st.session_state.mentor_recommendations = []

if "learning_roadmap" not in st.session_state:
    st.session_state.learning_roadmap = None

if "final_explanation" not in st.session_state:
    st.session_state.final_explanation = None

if "resume_score" not in st.session_state:
    st.session_state.resume_score = 0


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def is_valid_email(email):

    return (
        isinstance(email, str)
        and "@" in email
        and "." in email.split("@")[-1]
    )


def extract_resume_text(uploaded_file):

    if uploaded_file is None:
        return ""

    try:

        pdf_bytes = uploaded_file.read()

        document = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text.strip()

    except Exception as error:

        st.error(
            f"Unable to read resume: {error}"
        )

        return ""


# ============================================================
# RESUME SCORE
# ============================================================

def calculate_resume_score(resume_text):

    """
    Calculate a resume quality/completeness score
    from extracted resume text.

    This is NOT an internship recommendation score.

    Maximum score = 100.
    """

    if not resume_text:
        return 0

    text = resume_text.strip()
    lower_text = text.lower()

    score = 0

    # --------------------------------------------------------
    # 1. Resume content length
    # --------------------------------------------------------

    word_count = len(
        re.findall(
            r"\b\w+\b",
            text
        )
    )

    if word_count >= 300:
        score += 20

    elif word_count >= 200:
        score += 15

    elif word_count >= 100:
        score += 10

    elif word_count >= 50:
        score += 5

    # --------------------------------------------------------
    # 2. Contact information
    # --------------------------------------------------------

    has_email = bool(
        re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )
    )

    has_phone = bool(
        re.search(
            r"(?:\+92|0092|0)?\s*3\d{2}[-\s]?\d{7}",
            text
        )
    )

    if has_email or has_phone:
        score += 10

    if has_email and has_phone:
        score += 5

    # --------------------------------------------------------
    # 3. Education
    # --------------------------------------------------------

    education_keywords = [
        "education",
        "academic",
        "qualification",
        "degree",
        "bachelor",
        "master",
        "college",
        "university",
        "school",
        "fsc",
        "hssc",
        "matric"
    ]

    if any(
        keyword in lower_text
        for keyword in education_keywords
    ):
        score += 15

    # --------------------------------------------------------
    # 4. Skills
    # --------------------------------------------------------

    skill_keywords = [
        "skills",
        "technical skills",
        "programming",
        "python",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data science",
        "sql",
        "git",
        "github"
    ]

    skill_matches = sum(
        1
        for keyword in skill_keywords
        if keyword in lower_text
    )

    if skill_matches >= 5:
        score += 15

    elif skill_matches >= 3:
        score += 10

    elif skill_matches >= 1:
        score += 5

    # --------------------------------------------------------
    # 5. Projects
    # --------------------------------------------------------

    project_keywords = [
        "projects",
        "project",
        "developed",
        "built",
        "implemented",
        "application",
        "system"
    ]

    project_matches = sum(
        1
        for keyword in project_keywords
        if keyword in lower_text
    )

    if project_matches >= 3:
        score += 10

    elif project_matches >= 1:
        score += 5

    # --------------------------------------------------------
    # 6. Certifications
    # --------------------------------------------------------

    certification_keywords = [
        "certification",
        "certifications",
        "certificate",
        "certified",
        "training",
        "course"
    ]

    if any(
        keyword in lower_text
        for keyword in certification_keywords
    ):
        score += 10

    # --------------------------------------------------------
    # 7. Experience / Internship
    # --------------------------------------------------------

    experience_keywords = [
        "experience",
        "internship",
        "intern",
        "work experience",
        "professional experience",
        "employment"
    ]

    if any(
        keyword in lower_text
        for keyword in experience_keywords
    ):
        score += 10

    return min(
        score,
        100
    )


def get_resume_score_description(score):

    if score >= 80:
        return "Strong resume content and good section coverage."

    elif score >= 60:
        return "Good resume coverage with some areas that can be improved."

    elif score >= 40:
        return "Basic resume information is present, but several areas can be improved."

    elif score > 0:
        return "Resume content is limited. Adding more professional sections may improve the score."

    return "No resume available."


def render_resume_score(resume_text):

    score = calculate_resume_score(
        resume_text
    )

    description = get_resume_score_description(
        score
    )

    st.markdown(
        f"""
        <div class="resume-score-card">

            <div class="resume-score-title">
                📊 Resume Quality Score
            </div>

            <div class="resume-score-value">
                {score:.0f}/100
            </div>

            <div class="resume-score-description">
                {description}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(
        score / 100
    )

    return score


# ============================================================
# RESUME SKILL ANALYSIS
# ============================================================

def extract_resume_skills(resume_text):

    """
    Detect common technical and AI skills from resume text.

    This analysis is intentionally separate from the
    internship recommendation engine.
    """

    if not resume_text:
        return []

    text = resume_text.lower()

    skill_patterns = {
        "Python": [
            r"\bpython\b"
        ],
        "NumPy": [
            r"\bnumpy\b"
        ],
        "Pandas": [
            r"\bpandas\b"
        ],
        "Matplotlib": [
            r"\bmatplotlib\b"
        ],
        "Seaborn": [
            r"\bseaborn\b"
        ],
        "Scikit-learn": [
            r"\bscikit[- ]learn\b",
            r"\bsklearn\b"
        ],
        "Machine Learning": [
            r"\bmachine learning\b"
        ],
        "Deep Learning": [
            r"\bdeep learning\b"
        ],
        "Artificial Intelligence": [
            r"\bartificial intelligence\b",
            r"\bai\b"
        ],
        "Generative AI": [
            r"\bgenerative ai\b",
            r"\bgen ai\b"
        ],
        "Computer Vision": [
            r"\bcomputer vision\b"
        ],
        "NLP": [
            r"\bnatural language processing\b",
            r"\bnlp\b"
        ],
        "Keras": [
            r"\bkeras\b"
        ],
        "TensorFlow": [
            r"\btensorflow\b"
        ],
        "PyTorch": [
            r"\bpytorch\b"
        ],
        "YOLO": [
            r"\byolo\b"
        ],
        "MediaPipe": [
            r"\bmediapipe\b"
        ],
        "SQL": [
            r"\bsql\b"
        ],
        "Git": [
            r"\bgit\b"
        ],
        "GitHub": [
            r"\bgithub\b"
        ],
        "Streamlit": [
            r"\bstreamlit\b"
        ],
        "FastAPI": [
            r"\bfastapi\b"
        ],
        "REST API": [
            r"\brest api\b",
            r"\brestful api\b"
        ],
        "Langflow": [
            r"\blangflow\b"
        ],
        "RAG": [
            r"\brag\b",
            r"\bretrieval augmented generation\b"
        ],
        "FAISS": [
            r"\bfaiss\b"
        ],
        "Embeddings": [
            r"\bembeddings?\b"
        ],
        "Data Science": [
            r"\bdata science\b"
        ],
        "Data Analysis": [
            r"\bdata analysis\b",
            r"\bdata analytics\b"
        ],
        "Web Development": [
            r"\bweb development\b"
        ],
        "HTML": [
            r"\bhtml\b"
        ],
        "CSS": [
            r"\bcss\b"
        ],
        "JavaScript": [
            r"\bjavascript\b",
            r"\bjs\b"
        ]
    }

    detected_skills = []

    for skill, patterns in skill_patterns.items():

        for pattern in patterns:

            if re.search(
                pattern,
                text
            ):

                detected_skills.append(
                    skill
                )

                break

    return detected_skills


def normalize_skill_for_comparison(skill):

    skill = str(skill).strip().lower()

    aliases = {
        "sklearn": "scikit-learn",
        "scikit learn": "scikit-learn",
        "artificial intelligence": "artificial intelligence",
        "ai": "artificial intelligence",
        "machine-learning": "machine learning",
        "deep-learning": "deep learning",
        "computer-vision": "computer vision",
        "natural language processing": "nlp",
        "generative-ai": "generative ai",
        "gen ai": "generative ai",
        "github": "github",
        "rest api": "rest api"
    }

    return aliases.get(
        skill,
        skill
    )


def analyze_resume_skill_match(
    resume_skills,
    candidate_skills
):

    normalized_resume = {
        normalize_skill_for_comparison(skill)
        for skill in resume_skills
    }

    normalized_candidate = {
        normalize_skill_for_comparison(skill)
        for skill in candidate_skills
    }

    matching_skills = []
    missing_from_resume = []

    for resume_skill in resume_skills:

        normalized = normalize_skill_for_comparison(
            resume_skill
        )

        if normalized in normalized_candidate:

            matching_skills.append(
                resume_skill
            )

    for candidate_skill in candidate_skills:

        normalized = normalize_skill_for_comparison(
            candidate_skill
        )

        if normalized not in normalized_resume:

            missing_from_resume.append(
                candidate_skill
            )

    return (
        matching_skills,
        missing_from_resume
    )


def get_resume_information(resume_text):

    if not resume_text:
        return []

    text = resume_text.lower()

    information = []

    information_patterns = {
        "Education": [
            "education",
            "degree",
            "university",
            "college",
            "school",
            "fsc",
            "hssc",
            "matric"
        ],
        "Certifications": [
            "certification",
            "certifications",
            "certificate",
            "training",
            "course"
        ],
        "Projects": [
            "projects",
            "project",
            "developed",
            "built",
            "implemented"
        ],
        "Experience": [
            "experience",
            "work experience",
            "internship",
            "employment"
        ],
        "GitHub": [
            "github"
        ],
        "Portfolio": [
            "portfolio"
        ],
        "LinkedIn": [
            "linkedin"
        ]
    }

    for section, keywords in information_patterns.items():

        if any(
            keyword in text
            for keyword in keywords
        ):

            information.append(
                section
            )

    return information


def get_resume_insights(
    resume_text,
    resume_skills,
    matching_skills,
    missing_from_resume
):

    insights = []

    if not resume_text:

        return insights

    word_count = len(
        re.findall(
            r"\b\w+\b",
            resume_text
        )
    )

    if word_count >= 300:

        insights.append(
            "The resume contains a substantial amount of professional information."
        )

    elif word_count < 100:

        insights.append(
            "The extracted resume content is relatively short."
        )

    if resume_skills:

        insights.append(
            f"{len(resume_skills)} technical skills were detected from the resume."
        )

    if matching_skills:

        insights.append(
            f"{len(matching_skills)} detected resume skills also appear in the candidate profile."
        )

    if missing_from_resume:

        insights.append(
            f"{len(missing_from_resume)} candidate-profile skills were not detected in the uploaded resume."
        )

    if not resume_skills:

        insights.append(
            "No recognized technical skills were detected from the extracted resume text."
        )

    return insights


def render_resume_analysis(
    resume_text,
    candidate=None
):

    if not resume_text:

        st.info(
            "Upload a resume PDF to generate resume analysis."
        )

        return

    st.divider()

    st.subheader(
        "🧠 Resume Analysis"
    )

    st.caption(
        "This section analyzes the extracted resume content. "
        "Matching and missing skills are compared with the candidate profile."
    )

    # --------------------------------------------------------
    # Extract resume skills
    # --------------------------------------------------------

    resume_skills = extract_resume_skills(
        resume_text
    )

    candidate_skills = (
        candidate.skills
        if candidate
        and candidate.skills
        else []
    )

    (
        matching_skills,
        missing_from_resume
    ) = analyze_resume_skill_match(
        resume_skills,
        candidate_skills
    )

    # --------------------------------------------------------
    # Skill metrics
    # --------------------------------------------------------

    metric_col1, metric_col2, metric_col3 = st.columns(3)

    with metric_col1:

        st.metric(
            "Resume Skills Detected",
            len(resume_skills)
        )

    with metric_col2:

        st.metric(
            "Matching Skills",
            len(matching_skills)
        )

    with metric_col3:

        st.metric(
            "Profile Skills Not Found",
            len(missing_from_resume)
        )

    # --------------------------------------------------------
    # Detected skills
    # --------------------------------------------------------

    st.markdown(
        "### 🔎 Skills Detected From Resume"
    )

    if resume_skills:

        skill_columns = st.columns(
            min(
                max(
                    len(resume_skills),
                    1
                ),
                4
            )
        )

        for index, skill in enumerate(
            resume_skills
        ):

            with skill_columns[
                index % len(skill_columns)
            ]:

                st.success(
                    f"✓ {skill}"
                )

    else:

        st.info(
            "No recognized technical skills were detected."
        )

    # --------------------------------------------------------
    # Matching skills
    # --------------------------------------------------------

    st.markdown(
        "### 🎯 Matching Skills"
    )

    if matching_skills:

        for skill in matching_skills:

            st.success(
                f"✓ {skill}"
            )

    else:

        st.info(
            "No direct skill matches were found between "
            "the resume and candidate profile."
        )

    # --------------------------------------------------------
    # Skills missing from resume
    # --------------------------------------------------------

    st.markdown(
        "### ⚠️ Skills From Profile Not Detected In Resume"
    )

    if missing_from_resume:

        for skill in missing_from_resume:

            st.warning(
                f"• {skill}"
            )

    else:

        st.success(
            "All candidate-profile skills were detected in the resume."
        )

    # --------------------------------------------------------
    # Resume information
    # --------------------------------------------------------

    st.markdown(
        "### 📋 Resume Information Detected"
    )

    resume_information = get_resume_information(
        resume_text
    )

    if resume_information:

        info_columns = st.columns(
            min(
                max(
                    len(resume_information),
                    1
                ),
                4
            )
        )

        for index, information in enumerate(
            resume_information
        ):

            with info_columns[
                index % len(info_columns)
            ]:

                st.info(
                    f"✓ {information}"
                )

    else:

        st.info(
            "No standard resume sections were detected."
        )

    # --------------------------------------------------------
    # Suitable internship tracks
    # --------------------------------------------------------

    st.markdown(
        "### 💼 Suitable Internship Tracks"
    )

    saved_recommendations = []

    if candidate:

        try:

            saved_recommendations = (
                get_saved_recommendations(
                    candidate.id
                )
            )

        except Exception:

            saved_recommendations = []

    if saved_recommendations:

        for index, recommendation in enumerate(
            saved_recommendations[:5],
            start=1
        ):

            track_name = recommendation.get(
                "name",
                recommendation.get(
                    "track_name",
                    "Unknown Track"
                )
            )

            final_score = float(
                recommendation.get(
                    "final_score",
                    0.0
                )
            )

            matched = recommendation.get(
                "matched_skills",
                []
            )

            missing = recommendation.get(
                "missing_skills",
                []
            )

            with st.expander(
                f"{index}. {track_name} • {final_score:.2f}%"
            ):

                st.metric(
                    "AI Recommendation Score",
                    f"{final_score:.2f}%"
                )

                if matched:

                    st.write(
                        "**AI Matching Skills:**"
                    )

                    for skill in matched:

                        st.success(
                            f"✓ {skill}"
                        )

                if missing:

                    st.write(
                        "**AI Missing Skills:**"
                    )

                    for skill in missing:

                        st.warning(
                            f"• {skill}"
                        )

    else:

        st.info(
            "Generate AI internship recommendations to identify "
            "suitable internship tracks and track-specific missing skills."
        )

    # --------------------------------------------------------
    # Resume insights
    # --------------------------------------------------------

    st.markdown(
        "### 💡 Resume Insights"
    )

    insights = get_resume_insights(
        resume_text,
        resume_skills,
        matching_skills,
        missing_from_resume
    )

    if insights:

        for insight in insights:

            st.write(
                f"• {insight}"
            )


# ============================================================
# DASHBOARD HELPERS
# ============================================================

def get_dashboard_counts():

    db = SessionLocal()

    try:

        candidate_count = (
            db.query(Candidate).count()
        )

        recommendation_count = (
            db.query(Recommendation).count()
        )

        mentor_count = (
            db.query(MentorRecommendation).count()
        )

        roadmap_count = (
            db.query(LearningRoadmap).count()
        )

        return (
            candidate_count,
            recommendation_count,
            mentor_count,
            roadmap_count
        )

    finally:

        db.close()


def load_candidate_from_database(candidate_id):

    return get_candidate(candidate_id)


def generate_real_recommendations(candidate):

    normalized_candidate_skills = normalize_skills(
        candidate.skills or []
    )

    candidate.skills = normalized_candidate_skills

    candidate_text = create_candidate_text(
        candidate
    )

    recommendations = recommend_internship(
        candidate,
        candidate_text
    )

    return recommendations


def reset_generated_results():

    st.session_state.recommendations = []
    st.session_state.mentor_recommendations = []
    st.session_state.learning_roadmap = None
    st.session_state.final_explanation = None


def render_metric_card(
    title,
    value,
    description
):

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-description">{description}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# DASHBOARD
# ============================================================

def dashboard():

    st.markdown(
        """
        <div class="eef-header">
            <h1>🤖 EEF Intelligent Internship Recommendation Engine</h1>
            <p>
                AI-powered candidate matching, internship recommendation,
                mentor discovery and personalized career development.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    (
        candidate_count,
        recommendation_count,
        mentor_count,
        roadmap_count
    ) = get_dashboard_counts()

    st.subheader("📊 System Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        render_metric_card(
            "Candidates",
            candidate_count,
            "Candidate profiles stored"
        )

    with col2:

        render_metric_card(
            "Recommendations",
            recommendation_count,
            "AI recommendations generated"
        )

    with col3:

        render_metric_card(
            "Mentor Matches",
            mentor_count,
            "Mentor recommendations stored"
        )

    with col4:

        render_metric_card(
            "Roadmap Items",
            roadmap_count,
            "Learning roadmap records"
        )

    st.write("")

    st.subheader("🟢 System Status")

    status_col1, status_col2, status_col3, status_col4 = (
        st.columns(4)
    )

    with status_col1:

        st.markdown(
            """
            <div class="status-item">
                🗄️<br>
                <strong>Database</strong><br>
                <small>Connected</small>
            </div>
            """,
            unsafe_allow_html=True
        )

    with status_col2:

        st.markdown(
            """
            <div class="status-item">
                🤖<br>
                <strong>AI Engine</strong><br>
                <small>Operational</small>
            </div>
            """,
            unsafe_allow_html=True
        )

    with status_col3:

        st.markdown(
            """
            <div class="status-item">
                🧑‍🏫<br>
                <strong>Mentor Engine</strong><br>
                <small>Operational</small>
            </div>
            """,
            unsafe_allow_html=True
        )

    with status_col4:

        st.markdown(
            """
            <div class="status-item">
                📚<br>
                <strong>Roadmap Engine</strong><br>
                <small>Operational</small>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("🔄 AI Recommendation Pipeline")

    pipeline = [
        "👤 Candidate Profile",
        "📄 Resume Processing",
        "🧠 NLP & Skill Normalization",
        "🎯 AI Internship Matching",
        "🧑‍🏫 Mentor Matching",
        "⚠️ Skill Gap Analysis",
        "📚 Personalized Roadmap",
        "💡 Explainable AI"
    ]

    for index, step in enumerate(
        pipeline,
        start=1
    ):

        st.markdown(
            f"""
            <div class="pipeline-step">
                <strong>{index}</strong> &nbsp; {step}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader("🚀 How the System Works")

    info_col1, info_col2 = st.columns(2)

    with info_col1:

        st.markdown(
            """
            <div class="section-card">

            ### Candidate Analysis

            The system analyzes:

            - Resume information
            - Technical skills
            - Education
            - Certifications
            - Career interests
            - Projects
            - GitHub information
            - Portfolio information

            </div>
            """,
            unsafe_allow_html=True
        )

    with info_col2:

        st.markdown(
            """
            <div class="section-card">

            ### AI Career Recommendations

            The system provides:

            - Internship track recommendations
            - Recommendation scores
            - Confidence scores
            - Resume quality score
            - Resume skill analysis
            - Skill gap analysis
            - Mentor recommendations
            - Personalized learning roadmap
            - Explainable AI insights

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# CANDIDATE PROFILE
# ============================================================

def candidate_profile():

    st.title("👤 Candidate Profile")

    st.caption(
        "Create or update a candidate profile and upload a resume for analysis."
    )

    candidate_id = st.number_input(
        "Candidate ID",
        min_value=1,
        value=st.session_state.current_candidate_id,
        step=1
    )

    st.session_state.current_candidate_id = candidate_id

    candidate = get_candidate(
        candidate_id
    )

    if candidate:

        st.success(
            f"Candidate #{candidate.id} loaded — {candidate.name}"
        )

    else:

        st.info(
            "No candidate found. Fill the form below to create a new candidate."
        )

    st.divider()

    with st.form(
        "candidate_profile_form"
    ):

        st.subheader("📋 Personal Information")

        personal_col1, personal_col2 = st.columns(2)

        with personal_col1:

            name = st.text_input(
                "Full Name",
                value=(
                    candidate.name
                    if candidate
                    else ""
                )
            )

        with personal_col2:

            email = st.text_input(
                "Email Address",
                value=(
                    candidate.email
                    if candidate
                    else ""
                )
            )

        st.subheader("🎓 Education & Professional Background")

        education_text = st.text_area(
            "Education",
            value=(
                ", ".join(candidate.education)
                if candidate
                and candidate.education
                else ""
            ),
            help="Separate multiple entries with commas."
        )

        certifications_text = st.text_area(
            "Certifications",
            value=(
                ", ".join(candidate.certifications)
                if candidate
                and candidate.certifications
                else ""
            ),
            help="Separate multiple certifications with commas."
        )

        st.subheader("🧠 AI & Technical Profile")

        skills_text = st.text_area(
            "Skills",
            value=(
                ", ".join(candidate.skills)
                if candidate
                and candidate.skills
                else ""
            ),
            help="Example: Python, Machine Learning, Artificial Intelligence"
        )

        career_interests_text = st.text_area(
            "Career Interests",
            value=(
                ", ".join(candidate.career_interests)
                if candidate
                and candidate.career_interests
                else ""
            ),
            help="Example: Artificial Intelligence, Data Science"
        )

        projects_text = st.text_area(
            "Projects",
            value=(
                ", ".join(candidate.projects)
                if candidate
                and candidate.projects
                else ""
            ),
            help="List projects separated by commas."
        )

        st.subheader("🌐 Online Profile")

        online_col1, online_col2 = st.columns(2)

        with online_col1:

            github_username = st.text_input(
                "GitHub Username",
                value=(
                    candidate.github_username
                    if candidate
                    and candidate.github_username
                    else ""
                )
            )

        with online_col2:

            portfolio_url = st.text_input(
                "Portfolio URL",
                value=(
                    candidate.portfolio_url
                    if candidate
                    and candidate.portfolio_url
                    else ""
                )
            )

        st.subheader("📄 Resume")

        st.markdown(
            """
            <div class="resume-upload-card">
                <strong>📄 Upload your latest resume</strong><br>
                <small>
                    PDF format is supported. The resume text will be extracted
                    and stored for candidate analysis.
                </small>
            </div>
            """,
            unsafe_allow_html=True
        )

        resume_file = st.file_uploader(
            "Upload Resume PDF",
            type=["pdf"],
            help="Upload a PDF resume for AI candidate analysis."
        )

        if candidate and candidate.resume_text:

            st.success(
                "📄 Existing resume text is stored for this candidate."
            )

            current_resume_score = render_resume_score(
                candidate.resume_text
            )

            st.session_state.resume_score = (
                current_resume_score
            )

        else:

            st.info(
                "No resume is currently stored for this candidate."
            )

        submitted = st.form_submit_button(
            "💾 Save Candidate Profile",
            use_container_width=True
        )

        if submitted:

            if not name.strip():

                st.error(
                    "Name is required."
                )

                return

            if not is_valid_email(
                email
            ):

                st.error(
                    "Please enter a valid email address."
                )

                return

            skills = [
                skill.strip()
                for skill in skills_text.split(",")
                if skill.strip()
            ]

            education = [
                item.strip()
                for item in education_text.split(",")
                if item.strip()
            ]

            certifications = [
                item.strip()
                for item in certifications_text.split(",")
                if item.strip()
            ]

            career_interests = [
                item.strip()
                for item in career_interests_text.split(",")
                if item.strip()
            ]

            projects = [
                item.strip()
                for item in projects_text.split(",")
                if item.strip()
            ]

            # Preserve existing resume unless a new PDF is uploaded.
            resume_text = (
                candidate.resume_text
                if candidate
                and candidate.resume_text
                else ""
            )

            if resume_file:

                extracted_resume_text = (
                    extract_resume_text(
                        resume_file
                    )
                )

                if extracted_resume_text:

                    resume_text = (
                        extracted_resume_text
                    )

            if candidate:

                updated_candidate = update_candidate(
                    candidate_id=candidate_id,
                    name=name.strip(),
                    email=email.strip(),
                    skills=skills,
                    education=education,
                    certifications=certifications,
                    career_interests=career_interests,
                    projects=projects,
                    github_username=github_username.strip(),
                    portfolio_url=portfolio_url.strip(),
                    resume_text=resume_text
                )

                if updated_candidate:

                    reset_generated_results()

                    st.success(
                        "✅ Candidate profile updated successfully."
                    )

                    if resume_file and resume_text:

                        st.success(
                            "📄 New resume uploaded and processed successfully."
                        )

                        resume_score = calculate_resume_score(
                            resume_text
                        )

                        st.session_state.resume_score = (
                            resume_score
                        )

                        st.info(
                            f"📊 Resume Quality Score: "
                            f"**{resume_score:.0f}/100**"
                        )

                        st.progress(
                            resume_score / 100
                        )

                else:

                    st.error(
                        "Unable to update candidate."
                    )

            else:

                new_candidate = create_candidate(
                    name=name.strip(),
                    email=email.strip(),
                    skills=skills,
                    education=education,
                    certifications=certifications,
                    career_interests=career_interests,
                    projects=projects,
                    github_username=github_username.strip(),
                    portfolio_url=portfolio_url.strip(),
                    resume_text=resume_text
                )

                if new_candidate:

                    st.session_state.current_candidate_id = (
                        new_candidate.id
                    )

                    reset_generated_results()

                    st.success(
                        f"✅ Candidate created successfully. "
                        f"Candidate ID: {new_candidate.id}"
                    )

                    if resume_text:

                        resume_score = calculate_resume_score(
                            resume_text
                        )

                        st.session_state.resume_score = (
                            resume_score
                        )

                        st.info(
                            f"📊 Resume Quality Score: "
                            f"**{resume_score:.0f}/100**"
                        )

                        st.progress(
                            resume_score / 100
                        )

                else:

                    st.error(
                        "Unable to create candidate."
                    )

    # ========================================================
    # RESUME ANALYSIS
    # ========================================================

    analysis_candidate = get_candidate(
        candidate_id
    )

    if analysis_candidate and analysis_candidate.resume_text:

        render_resume_analysis(
            analysis_candidate.resume_text,
            analysis_candidate
        )


# ============================================================
# INTERNSHIP RECOMMENDATIONS
# ============================================================

def internship_recommendations():

    st.title("🎯 Internship Recommendations")

    st.caption(
        "Use the existing AI recommendation engine to analyze the candidate."
    )

    candidate_id = st.number_input(
        "Candidate ID",
        min_value=1,
        value=st.session_state.current_candidate_id,
        step=1,
        key="recommendation_candidate_id"
    )

    st.session_state.current_candidate_id = candidate_id

    candidate = get_candidate(
        candidate_id
    )

    if candidate is None:

        st.warning(
            "Candidate not found. Create the candidate profile first."
        )

        return

    st.success(
        f"Candidate: **{candidate.name}** | ID: **{candidate.id}**"
    )

    if candidate.resume_text:

        resume_col1, resume_col2 = st.columns(
            [2, 1]
        )

        with resume_col1:

            st.info(
                "📄 Resume information is available for AI analysis."
            )

        with resume_col2:

            resume_score = calculate_resume_score(
                candidate.resume_text
            )

            st.metric(
                "Resume Score",
                f"{resume_score:.0f}/100"
            )

        st.progress(
            resume_score / 100
        )

        st.caption(
            get_resume_score_description(
                resume_score
            )
        )

    else:

        st.warning(
            "📄 No resume text is stored. Recommendations can still "
            "use the candidate profile information."
        )

    if st.button(
        "🤖 Generate AI Recommendations",
        use_container_width=True
    ):

        with st.spinner(
            "Analyzing candidate profile and generating recommendations..."
        ):

            try:

                recommendations = (
                    generate_real_recommendations(
                        candidate
                    )
                )

                st.session_state.recommendations = (
                    recommendations
                )

                save_recommendations(
                    candidate.id,
                    recommendations
                )

                st.session_state.mentor_recommendations = []
                st.session_state.learning_roadmap = None
                st.session_state.final_explanation = None

                st.success(
                    "✅ AI recommendations generated and saved successfully."
                )

            except Exception as error:

                st.error(
                    f"Recommendation generation failed: {error}"
                )

                return

    recommendations = (
        st.session_state.recommendations
    )

    if not recommendations:

        recommendations = (
            get_saved_recommendations(
                candidate.id
            )
        )

        st.session_state.recommendations = (
            recommendations
        )

    if not recommendations:

        st.info(
            "Generate recommendations to continue."
        )

        return

    st.divider()

    st.subheader(
        "🏆 Recommended Internship Tracks"
    )

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        track_name = recommendation.get(
            "name",
            recommendation.get(
                "track_name",
                "Unknown Track"
            )
        )

        final_score = float(
            recommendation.get(
                "final_score",
                0.0
            )
        )

        confidence_score = float(
            recommendation.get(
                "confidence_score",
                0.0
            )
        )

        with st.expander(
            f"{index}. {track_name}  •  {final_score:.2f}%"
        ):

            score_col1, score_col2, score_col3 = (
                st.columns(3)
            )

            with score_col1:

                st.metric(
                    "Final Score",
                    f"{final_score:.2f}%"
                )

            with score_col2:

                st.metric(
                    "Confidence",
                    f"{confidence_score:.2f}%"
                )

            with score_col3:

                st.metric(
                    "Matched Skills",
                    len(
                        recommendation.get(
                            "matched_skills",
                            []
                        )
                    )
                )

            st.markdown(
                "### 📊 Recommendation Factors"
            )

            factors = {
                "Skill Match": recommendation.get(
                    "skill_score",
                    0.0
                ),
                "Semantic Match": recommendation.get(
                    "semantic_score",
                    0.0
                ),
                "Project Relevance": recommendation.get(
                    "project_score",
                    0.0
                ),
                "Career Interest": recommendation.get(
                    "career_interest_score",
                    0.0
                ),
                "Education Relevance": recommendation.get(
                    "education_score",
                    0.0
                ),
                "Portfolio Relevance": recommendation.get(
                    "portfolio_score",
                    0.0
                ),
                "Certification Relevance": recommendation.get(
                    "certification_score",
                    0.0
                )
            }

            factor_col1, factor_col2 = st.columns(2)

            factor_items = list(
                factors.items()
            )

            midpoint = (
                len(factor_items) + 1
            ) // 2

            for factor, score in factor_items[:midpoint]:

                with factor_col1:

                    score = float(score)

                    st.write(
                        f"**{factor} — {score:.2f}%**"
                    )

                    st.progress(
                        min(
                            max(
                                score / 100,
                                0.0
                            ),
                            1.0
                        )
                    )

            for factor, score in factor_items[midpoint:]:

                with factor_col2:

                    score = float(score)

                    st.write(
                        f"**{factor} — {score:.2f}%**"
                    )

                    st.progress(
                        min(
                            max(
                                score / 100,
                                0.0
                            ),
                            1.0
                        )
                    )

            st.markdown(
                "### ✅ Matched Skills"
            )

            matched_skills = recommendation.get(
                "matched_skills",
                []
            )

            if matched_skills:

                skill_columns = st.columns(
                    min(
                        max(
                            len(matched_skills),
                            1
                        ),
                        4
                    )
                )

                for skill_index, skill in enumerate(
                    matched_skills
                ):

                    with skill_columns[
                        skill_index % len(skill_columns)
                    ]:

                        st.success(
                            f"✓ {skill}"
                        )

            else:

                st.info(
                    "No matched skills found."
                )

            st.markdown(
                "### ⚠️ Missing Skills"
            )

            missing_skills = recommendation.get(
                "missing_skills",
                []
            )

            if missing_skills:

                for skill in missing_skills:

                    st.warning(
                        f"• {skill}"
                    )

            else:

                st.success(
                    "No major missing skills identified."
                )

            explanation = recommendation.get(
                "explanation",
                ""
            )

            if explanation:

                st.markdown(
                    "### 💡 Why This Track?"
                )

                if isinstance(
                    explanation,
                    list
                ):

                    for item in explanation:

                        st.write(
                            f"✓ {item}"
                        )

                else:

                    st.write(
                        explanation
                    )


# ============================================================
# MENTOR RECOMMENDATION
# ============================================================

def mentor_recommendation():

    st.title("🧑‍🏫 Mentor Recommendation")

    st.caption(
        "Find mentors based on the candidate's AI profile and recommendation data."
    )

    candidate_id = st.number_input(
        "Candidate ID",
        min_value=1,
        value=st.session_state.current_candidate_id,
        step=1,
        key="mentor_candidate_id"
    )

    st.session_state.current_candidate_id = candidate_id

    candidate = get_candidate(
        candidate_id
    )

    if candidate is None:

        st.warning(
            "Candidate not found."
        )

        return

    recommendations = (
        get_saved_recommendations(
            candidate.id
        )
    )

    if not recommendations:

        st.info(
            "Generate internship recommendations first."
        )

        return

    track_names = []

    for recommendation in recommendations:

        track_name = recommendation.get(
            "name",
            recommendation.get(
                "track_name",
                "Unknown Track"
            )
        )

        track_names.append(
            track_name
        )

    selected_track = st.selectbox(
        "Select Internship Track",
        track_names,
        key="mentor_track"
    )

    selected_recommendation = None

    for recommendation in recommendations:

        track_name = recommendation.get(
            "name",
            recommendation.get(
                "track_name",
                ""
            )
        )

        if track_name == selected_track:

            selected_recommendation = recommendation

            break

    if selected_recommendation:

        st.info(
            f"Selected track: **{selected_track}**"
        )

    if st.button(
        "🔎 Find Mentors",
        use_container_width=True
    ):

        with st.spinner(
            "Finding suitable mentors..."
        ):

            try:

                mentor_results = (
                    match_candidate_with_mentors(
                        candidate
                    )
                )

                st.session_state.mentor_recommendations = (
                    mentor_results
                )

                save_mentor_recommendations(
                    candidate.id,
                    mentor_results
                )

                st.success(
                    "✅ Mentor recommendations generated and saved."
                )

            except Exception as error:

                st.error(
                    f"Mentor recommendation failed: {error}"
                )

                return

    mentor_results = (
        st.session_state.mentor_recommendations
    )

    if not mentor_results:

        mentor_results = (
            get_saved_mentor_recommendations(
                candidate.id
            )
        )

        st.session_state.mentor_recommendations = (
            mentor_results
        )

    if not mentor_results:

        st.info(
            "Find mentors to continue."
        )

        return

    st.divider()

    st.subheader(
        f"🧑‍🏫 Mentor Matches for {selected_track}"
    )

    for index, mentor_result in enumerate(
        mentor_results[:3],
        start=1
    ):

        mentor_data = mentor_result.get(
            "mentor",
            {}
        )

        mentor_name = mentor_data.get(
            "name",
            mentor_result.get(
                "mentor_name",
                "Unknown Mentor"
            )
        )

        specialization = mentor_data.get(
            "specialization",
            mentor_result.get(
                "specialization",
                "Not available"
            )
        )

        final_score = float(
            mentor_result.get(
                "final_score",
                0.0
            )
        )

        with st.expander(
            f"{index}. {mentor_name}  •  {final_score:.2f}%"
        ):

            score_col1, score_col2 = st.columns(2)

            with score_col1:

                st.metric(
                    "Final Match Score",
                    f"{final_score:.2f}%"
                )

            with score_col2:

                st.metric(
                    "Track",
                    mentor_result.get(
                        "track_name",
                        selected_track
                    )
                )

            st.write(
                f"**Mentor:** {mentor_name}"
            )

            st.write(
                f"**Specialization:** {specialization}"
            )

            st.divider()

            mentor_factors = {
                "Expertise Score": mentor_result.get(
                    "expertise_score",
                    0.0
                ),
                "Semantic Score": mentor_result.get(
                    "semantic_score",
                    0.0
                ),
                "Track Score": mentor_result.get(
                    "track_score",
                    0.0
                ),
                "Experience Score": mentor_result.get(
                    "experience_score",
                    0.0
                )
            }

            for factor, score in mentor_factors.items():

                score = float(score)

                st.write(
                    f"**{factor}: {score:.2f}%**"
                )

                st.progress(
                    min(
                        max(
                            score / 100,
                            0.0
                        ),
                        1.0
                    )
                )


# ============================================================
# LEARNING ROADMAP
# ============================================================

def learning_roadmap():

    st.title("📚 Personalized Learning Roadmap")

    st.caption(
        "Build a structured learning path from the candidate's missing skills."
    )

    candidate_id = st.number_input(
        "Candidate ID",
        min_value=1,
        value=st.session_state.current_candidate_id,
        step=1,
        key="roadmap_candidate_id"
    )

    st.session_state.current_candidate_id = candidate_id

    candidate = get_candidate(
        candidate_id
    )

    if candidate is None:

        st.warning(
            "Candidate not found."
        )

        return

    recommendations = (
        get_saved_recommendations(
            candidate.id
        )
    )

    if not recommendations:

        st.info(
            "Generate internship recommendations first."
        )

        return

    track_names = []

    for recommendation in recommendations:

        track_name = recommendation.get(
            "name",
            recommendation.get(
                "track_name",
                "Unknown Track"
            )
        )

        track_names.append(
            track_name
        )

    selected_track = st.selectbox(
        "Select Internship Track",
        track_names,
        key="roadmap_track"
    )

    selected_recommendation = None

    for recommendation in recommendations:

        track_name = recommendation.get(
            "name",
            recommendation.get(
                "track_name",
                ""
            )
        )

        if track_name == selected_track:

            selected_recommendation = recommendation

            break

    missing_skills = []

    if selected_recommendation:

        missing_skills = selected_recommendation.get(
            "missing_skills",
            []
        )

    st.subheader(
        "⚠️ Skill Gap"
    )

    if missing_skills:

        skill_columns = st.columns(
            min(
                max(
                    len(missing_skills),
                    1
                ),
                4
            )
        )

        for index, skill in enumerate(
            missing_skills
        ):

            with skill_columns[
                index % len(skill_columns)
            ]:

                st.warning(
                    skill
                )

    else:

        st.success(
            "No major missing skills identified."
        )

    if st.button(
        "🗺️ Generate Learning Roadmap",
        use_container_width=True
    ):

        with st.spinner(
            "Generating personalized learning roadmap..."
        ):

            try:

                roadmap = (
                    generate_personalized_roadmap(
                        missing_skills,
                        selected_track
                    )
                )

                st.session_state.learning_roadmap = (
                    roadmap
                )

                save_learning_roadmap(
                    candidate.id,
                    roadmap
                )

                st.success(
                    "✅ Personalized learning roadmap generated and saved."
                )

            except Exception as error:

                st.error(
                    f"Learning roadmap generation failed: {error}"
                )

                return

    roadmap = (
        st.session_state.learning_roadmap
    )

    if not roadmap:

        roadmap = (
            get_saved_learning_roadmap(
                candidate.id
            )
        )

        st.session_state.learning_roadmap = (
            roadmap
        )

    if not roadmap:

        st.info(
            "Generate a learning roadmap to continue."
        )

        return

    st.divider()

    if isinstance(
        roadmap,
        dict
    ):

        summary = roadmap.get(
            "summary",
            {}
        )

        if summary:

            st.subheader(
                "📊 Roadmap Progress"
            )

            summary_col1, summary_col2, summary_col3, summary_col4 = (
                st.columns(4)
            )

            with summary_col1:

                st.metric(
                    "Total Steps",
                    summary.get(
                        "total_steps",
                        0
                    )
                )

            with summary_col2:

                st.metric(
                    "Completed",
                    summary.get(
                        "completed_steps",
                        0
                    )
                )

            with summary_col3:

                st.metric(
                    "In Progress",
                    summary.get(
                        "in_progress_steps",
                        0
                    )
                )

            with summary_col4:

                progress = float(
                    summary.get(
                        "overall_progress",
                        0.0
                    )
                )

                st.metric(
                    "Overall Progress",
                    f"{progress:.2f}%"
                )

                st.progress(
                    min(
                        max(
                            progress / 100,
                            0.0
                        ),
                        1.0
                    )
                )

        roadmap_items = roadmap.get(
            "roadmap",
            []
        )

    else:

        roadmap_items = roadmap

    st.subheader(
        "🧭 Learning Plan"
    )

    for index, item in enumerate(
        roadmap_items,
        start=1
    ):

        skill = item.get(
            "skill",
            "Unknown Skill"
        )

        priority = item.get(
            "priority",
            "Not specified"
        )

        stage = item.get(
            "stage",
            "Not specified"
        )

        duration = item.get(
            "duration",
            "Not specified"
        )

        resource_type = item.get(
            "resource_type",
            "Not specified"
        )

        milestone = item.get(
            "milestone",
            "Not specified"
        )

        status = item.get(
            "status",
            "Not started"
        )

        with st.expander(
            f"{index}. {skill}"
        ):

            info_col1, info_col2 = st.columns(2)

            with info_col1:

                st.write(
                    f"**Priority:** {priority}"
                )

                st.write(
                    f"**Stage:** {stage}"
                )

                st.write(
                    f"**Duration:** {duration}"
                )

            with info_col2:

                st.write(
                    f"**Resource:** {resource_type}"
                )

                st.write(
                    f"**Status:** {status}"
                )

                st.write(
                    f"**Milestone:** {milestone}"
                )


# ============================================================
# AI EXPLANATION
# ============================================================

def ai_explanation():

    st.title("💡 Explainable AI Recommendation")

    st.caption(
        "Understand why the AI recommended the selected internship track."
    )

    candidate_id = st.number_input(
        "Candidate ID",
        min_value=1,
        value=st.session_state.current_candidate_id,
        step=1,
        key="explanation_candidate_id"
    )

    st.session_state.current_candidate_id = candidate_id

    candidate = get_candidate(
        candidate_id
    )

    if candidate is None:

        st.warning(
            "Candidate not found."
        )

        return

    recommendations = (
        get_saved_recommendations(
            candidate.id
        )
    )

    if not recommendations:

        st.info(
            "Generate recommendations first."
        )

        return

    top_track = recommendations[0]

    track_name = top_track.get(
        "name",
        top_track.get(
            "track_name",
            "Unknown Track"
        )
    )

    final_score = float(
        top_track.get(
            "final_score",
            0.0
        )
    )

    confidence_score = float(
        top_track.get(
            "confidence_score",
            0.0
        )
    )

    st.subheader(
        f"Why {track_name}?"
    )

    score_col1, score_col2, score_col3 = st.columns(3)

    with score_col1:

        st.metric(
            "Final Recommendation Score",
            f"{final_score:.2f}%"
        )

    with score_col2:

        st.metric(
            "Confidence",
            f"{confidence_score:.2f}%"
        )

    with score_col3:

        resume_score = calculate_resume_score(
            candidate.resume_text or ""
        )

        st.metric(
            "Resume Score",
            f"{resume_score:.0f}/100"
        )

    st.divider()

    st.subheader(
        "🎯 Skill Match Analysis"
    )

    matched_skills = top_track.get(
        "matched_skills",
        []
    )

    missing_skills = top_track.get(
        "missing_skills",
        []
    )

    skill_col1, skill_col2 = st.columns(2)

    with skill_col1:

        st.markdown(
            "### ✅ Matched Skills"
        )

        if matched_skills:

            for skill in matched_skills:

                st.success(
                    f"✓ {skill}"
                )

        else:

            st.info(
                "No matched skills found."
            )

    with skill_col2:

        st.markdown(
            "### ⚠️ Missing Skills"
        )

        if missing_skills:

            for skill in missing_skills:

                st.warning(
                    f"• {skill}"
                )

        else:

            st.success(
                "No major missing skills identified."
            )

    st.divider()

    # ========================================================
    # TRACK EXPLANATION
    # ========================================================

    track_explanation = (
        explain_track_recommendation(
            track_name,
            top_track.get(
                "final_score",
                0.0
            ),
            top_track.get(
                "skill_score",
                0.0
            ),
            top_track.get(
                "semantic_score",
                0.0
            ),
            top_track.get(
                "project_score",
                0.0
            ),
            top_track.get(
                "career_interest_score",
                0.0
            ),
            top_track.get(
                "education_score",
                0.0
            ),
            top_track.get(
                "portfolio_score",
                0.0
            ),
            top_track.get(
                "certification_score",
                0.0
            )
        )
    )

    # ========================================================
    # STRENGTHS
    # ========================================================

    strengths = analyze_strengths(
        matched_skills,
        candidate.projects or [],
        candidate.certifications or [],
        candidate.career_interests or []
    )

    # ========================================================
    # WEAKNESSES
    # ========================================================

    weaknesses = analyze_weaknesses(
        missing_skills,
        track_name
    )

    # ========================================================
    # SKILL GAP EXPLANATION
    # ========================================================

    skill_gap_explanation = (
        create_skill_gap_explanation(
            missing_skills,
            track_name
        )
    )

    # ========================================================
    # ROADMAP
    # ========================================================

    roadmap = (
        st.session_state.learning_roadmap
    )

    if not roadmap:

        roadmap = (
            get_saved_learning_roadmap(
                candidate.id
            )
        )

    roadmap_summary = ""

    if isinstance(
        roadmap,
        dict
    ):

        roadmap_summary = roadmap.get(
            "summary",
            ""
        )

    # ========================================================
    # MENTOR EXPLANATION
    # ========================================================

    saved_mentors = (
        get_saved_mentor_recommendations(
            candidate.id
        )
    )

    mentor_explanation = {
        "mentor": "No mentor selected",
        "track": track_name,
        "specialization": "Not available",
        "final_score": 0.0,
        "reason": (
            "No saved mentor recommendation "
            "was available for this candidate."
        ),
        "explanation": (
            "Generate mentor recommendations "
            "to include mentor information."
        )
    }

    if saved_mentors:

        selected_mentor = saved_mentors[0]

        mentor_data = selected_mentor.get(
            "mentor",
            {}
        )

        mentor_name = mentor_data.get(
            "name",
            selected_mentor.get(
                "mentor_name",
                "Unknown Mentor"
            )
        )

        mentor_specialization = mentor_data.get(
            "specialization",
            selected_mentor.get(
                "specialization",
                "Not available"
            )
        )

        mentor_score = float(
            selected_mentor.get(
                "final_score",
                0.0
            )
        )

        mentor_explanation = {
            "mentor": mentor_name,
            "track": selected_mentor.get(
                "track_name",
                track_name
            ),
            "specialization": mentor_specialization,
            "final_score": mentor_score,
            "reason": (
                f"{mentor_name} was selected from "
                "the saved mentor recommendations "
                "for this candidate."
            ),
            "explanation": (
                f"The mentor match score is "
                f"{mentor_score:.2f}%."
            )
        }

    # ========================================================
    # FINAL EXPLANATION
    # ========================================================

    final_explanation = (
        generate_final_explanation(
            track_explanation,
            strengths,
            weaknesses,
            skill_gap_explanation,
            mentor_explanation,
            roadmap_summary
        )
    )

    st.session_state.final_explanation = (
        final_explanation
    )

    st.subheader(
        "🧠 AI Explanation"
    )

    if isinstance(
        final_explanation,
        list
    ):

        for explanation in final_explanation:

            st.success(
                f"✓ {explanation}"
            )

    else:

        st.write(
            final_explanation
        )

    st.divider()

    # ========================================================
    # RECOMMENDATION FACTORS
    # ========================================================

    st.subheader(
        "📊 Recommendation Factors"
    )

    factors = {
        "Skill Match": top_track.get(
            "skill_score",
            0.0
        ),
        "Semantic Match": top_track.get(
            "semantic_score",
            0.0
        ),
        "Project Relevance": top_track.get(
            "project_score",
            0.0
        ),
        "Career Interest": top_track.get(
            "career_interest_score",
            0.0
        ),
        "Education Relevance": top_track.get(
            "education_score",
            0.0
        ),
        "Portfolio Relevance": top_track.get(
            "portfolio_score",
            0.0
        ),
        "Certification Relevance": top_track.get(
            "certification_score",
            0.0
        )
    }

    factor_col1, factor_col2 = st.columns(2)

    factor_items = list(
        factors.items()
    )

    midpoint = (
        len(factor_items) + 1
    ) // 2

    for factor, score in factor_items[:midpoint]:

        with factor_col1:

            score = float(score)

            st.write(
                f"**{factor}: {score:.2f}%**"
            )

            st.progress(
                min(
                    max(
                        score / 100,
                        0.0
                    ),
                    1.0
                )
            )

    for factor, score in factor_items[midpoint:]:

        with factor_col2:

            score = float(score)

            st.write(
                f"**{factor}: {score:.2f}%**"
            )

            st.progress(
                min(
                    max(
                        score / 100,
                        0.0
                    ),
                    1.0
                )
            )

    st.divider()

    st.subheader(
        "🧑‍🏫 Recommended Mentor"
    )

    if saved_mentors:

        mentor = saved_mentors[0]

        mentor_data = mentor.get(
            "mentor",
            {}
        )

        mentor_name = mentor_data.get(
            "name",
            mentor.get(
                "mentor_name",
                "Unknown Mentor"
            )
        )

        mentor_specialization = mentor_data.get(
            "specialization",
            mentor.get(
                "specialization",
                "Not available"
            )
        )

        mentor_score = float(
            mentor.get(
                "final_score",
                0.0
            )
        )

        st.info(
            f"**{mentor_name}** — "
            f"{mentor_specialization} — "
            f"Match Score: {mentor_score:.2f}%"
        )

    else:

        st.info(
            "No saved mentor recommendation available."
        )


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
    <div class="eef-header">

    <h2>🤖 EEF AI Engine</h2>

    <p>
    Intelligent Internship Recommendation
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "### Navigation"
)

page = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Candidate Profile",
        "Internship Recommendations",
        "Mentor Recommendation",
        "Learning Roadmap",
        "AI Explanation"
    ],
    label_visibility="collapsed"
)

st.sidebar.divider()

st.sidebar.markdown(
    f"""
    **Current Candidate**

    Candidate ID: **{st.session_state.current_candidate_id}**
    """
)

st.sidebar.divider()

st.sidebar.caption(
    "EEF Industry AI Case Study — AI-001"
)

st.sidebar.caption(
    "Intelligent Internship Recommendation & Candidate Matching Engine"
)


# ============================================================
# PAGE ROUTING
# ============================================================

if page == "Dashboard":

    dashboard()

elif page == "Candidate Profile":

    candidate_profile()

elif page == "Internship Recommendations":

    internship_recommendations()

elif page == "Mentor Recommendation":

    mentor_recommendation()

elif page == "Learning Roadmap":

    learning_roadmap()

elif page == "AI Explanation":

    ai_explanation()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="eef-footer">
        EEF AI-001 • Intelligent Internship Recommendation &
        Candidate Matching Engine
    </div>
    """,
    unsafe_allow_html=True
)