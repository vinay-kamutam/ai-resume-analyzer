from fastapi import FastAPI

from app.routers.resume import router as resume_router
from app.routers.ats import router as ats_router
from app.routers.job_match import router as job_match_router
from app.routers.ai import router as ai_router

app = FastAPI(
    title="AI Resume Analyzer API"
)

app.include_router(resume_router)
app.include_router(ats_router)
app.include_router(job_match_router)
app.include_router(ai_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer 🚀"
    }