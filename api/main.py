from fastapi import FastAPI
from database.database import create_tables

from api.database_routes import router as database_router
from api.recommendation_database_routes import (
    router as recommendation_database_router
)
from api.routes import router as ai_router


# =========================================================
# DATABASE INITIALIZATION
# =========================================================

create_tables()


# =========================================================
# FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="EEF Intelligent Internship Recommendation Engine",
    description=(
        "AI-powered internship recommendation "
        "and candidate matching API"
    ),
    version="1.0.0"
)


# =========================================================
# ROUTES
# =========================================================

app.include_router(database_router)
app.include_router(recommendation_database_router)
app.include_router(ai_router)


# =========================================================
# ROOT ENDPOINT
# =========================================================

@app.get("/")
def home():
    return {
        "message": "EEF API is running successfully.",
        "database": "connected"
    }


# =========================================================
# LOCAL SERVER
# =========================================================

if __name__ == "__main__":

    import os
    import uvicorn

    port = int(
        os.getenv("PORT", "8000")
    )

    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=port,
        reload=False
    )