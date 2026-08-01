from fastapi import FastAPI, UploadFile, File
import shutil
import os
import json

from app.parser.pdf_parser import extract_resume_data
from app.services.ollama_service import ask_ai
from app.prompts.resume_prompt import recruiter_prompt

app = FastAPI(title="AI Resume Analyzer API")

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer 🚀"
    }


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_data = extract_resume_data(file_path)

    prompt = recruiter_prompt(
    resume_data["resume_text"]
    )

    ai_summary = ask_ai(prompt)
    print(ai_summary)
    ai_data = json.loads(ai_summary)

    return {
        "filename": file.filename,
        "pages": resume_data["pages"],
        "characters": resume_data["characters"],
        "analysis": ai_data
    }
    
@app.get("/ask-ai")
def ask_ai_demo():

    answer = ask_ai(
        "Say hello to Vinay in one sentence."
    )

    return {
        "answer": answer
    }