from fastapi import APIRouter

from app.services.ollama_service import ask_ai

router = APIRouter()


@router.get("/ask-ai")
def ask_ai_demo():

    answer = ask_ai(
        "Say hello to Vinay in one sentence."
    )

    return {
        "answer": answer
    }