from fastapi import APIRouter
from ..services.question import get_answer_to

router = APIRouter()

@router.get('/question')
async def ask_question_route(question):
    return get_answer_to(question)