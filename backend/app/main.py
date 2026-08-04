from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os
import json

from app.parser.pdf_parser import extract_resume_data
from app.services.ollama_service import ask_ai
from app.prompts.resume_prompt import recruiter_prompt
from app.prompts.ats_prompt import ats_prompt
from app.prompts.job_match_prompt import job_match_prompt
from app.utils.json_parser import parse_ai_json

app = FastAPI(title="AI Resume Analyzer API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# -----------------------------------------
# Helper Function
# -----------------------------------------
def parse_ai_json(ai_response: str):
    """
    Cleans common LLM JSON mistakes before parsing.
    """

    ai_response = ai_response.replace("None", "null")
    ai_response = ai_response.replace("True", "true")
    ai_response = ai_response.replace("False", "false")

    ai_response = ai_response.strip()

    if not ai_response.endswith("}"):
        ai_response += "\n}"

    return json.loads(ai_response)


# -----------------------------------------
# Home
# -----------------------------------------
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Resume Analyzer 🚀"
    }


# -----------------------------------------
# Resume Analyzer
# -----------------------------------------
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_data = extract_resume_data(file_path)

    prompt = recruiter_prompt(resume_data["resume_text"])

    ai_response = ask_ai(prompt)

    try:
        ai_data = parse_ai_json(ai_response)

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by AI",
            "raw_response": ai_response
        }

    return {
        "filename": file.filename,
        "pages": resume_data["pages"],
        "characters": resume_data["characters"],
        "analysis": ai_data
    }


# -----------------------------------------
# ATS Score
# -----------------------------------------
@app.post("/ats-score")
async def ats_score(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_data = extract_resume_data(file_path)

    prompt = ats_prompt(resume_data["resume_text"])

    ai_response = ask_ai(prompt)

    try:
        ats_data = parse_ai_json(ai_response)

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by AI",
            "raw_response": ai_response
        }

    return {
        "filename": file.filename,
        "ats_analysis": ats_data
    }


# -----------------------------------------
# Job Match
# -----------------------------------------
@app.post("/job-match")
async def job_match(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_data = extract_resume_data(file_path)

    prompt = job_match_prompt(
        resume_data["resume_text"],
        job_description
    )

    ai_response = ask_ai(prompt)

    try:
        match_data = parse_ai_json(ai_response)

    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by AI",
            "raw_response": ai_response
        }

    return {
        "filename": file.filename,
        "job_match": match_data
    }


# -----------------------------------------
# AI Demo
# -----------------------------------------
@app.get("/ask-ai")
def ask_ai_demo():

    answer = ask_ai(
        "Say hello to Vinay in one sentence."
    )

    return {
        "answer": answer
    }