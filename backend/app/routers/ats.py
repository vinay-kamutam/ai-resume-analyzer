from fastapi import APIRouter, UploadFile, File
import os
import shutil
import json

from app.parser.pdf_parser import extract_resume_data
from app.prompts.ats_prompt import ats_prompt
from app.services.ollama_service import ask_ai
from app.utils.json_parser import parse_ai_json

router = APIRouter()

UPLOAD_DIR = "uploads"


@router.post("/ats-score")
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