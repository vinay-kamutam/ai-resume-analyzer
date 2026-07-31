from fastapi import FastAPI

app = FastAPI(
    title="AI Resume Analyzer API",
    version="1.0.0",
    description="Backend API for AI Resume Analyzer"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer 🚀"
    }

@app.get("/hello")
def hello():
    return {
        "message": "Hello Vinay 👋"
    }

@app.get("/health")
def health():
    return {
        "status": "UP"
    }