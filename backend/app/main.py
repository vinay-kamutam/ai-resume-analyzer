from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.resume import router as resume_router
from app.routers.ats import router as ats_router
from app.routers.job_match import router as job_match_router
from app.routers.ai import router as ai_router


app = FastAPI(
    title="AI Resume Analyzer API"
)


# -------------------------
# CORS Configuration
# -------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://34.202.213.6:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# API Routers
# -------------------------

app.include_router(resume_router)
app.include_router(ats_router)
app.include_router(job_match_router)
app.include_router(ai_router)


# -------------------------
# Health Check
# -------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer 🚀"
    }