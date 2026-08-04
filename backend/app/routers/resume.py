from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.parser.pdf_parser import extract_resume_data
from app.prompts.resume_prompt import recruiter_prompt
from app.services.ollama_service import ask_ai
from app.utils.json_parser import parse_ai_json

router = APIRouter()

UPLOAD_DIR = "uploads"


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_data = extract_resume_data(file_path)

    prompt = recruiter_prompt(
        resume_data["resume_text"]
    )

    ai_response = ask_ai(prompt)

    try:
        ai_data = parse_ai_json(ai_response)

    except Exception:

        return {
            "error": "Invalid JSON",
            "raw_response": ai_response
        }

    return {
        "filename": file.filename,
        "pages": resume_data["pages"],
        "characters": resume_data["characters"],
        "analysis": ai_data
    }