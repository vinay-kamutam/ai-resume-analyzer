from fastapi import APIRouter, UploadFile, File, Form
import os
import shutil
import json

from app.parser.pdf_parser import extract_resume_data
from app.prompts.job_match_prompt import job_match_prompt
from app.services.ollama_service import ask_ai
from app.utils.json_parser import parse_ai_json

router = APIRouter()

UPLOAD_DIR = "uploads"


@router.post("/job-match")
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