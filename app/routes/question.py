from fastapi import APIRouter
from pydantic import BaseModel
from ..services.question import get_answer_to

router = APIRouter()

class Question(BaseModel):
    q: str

@router.post('/question')
async def ask_question_route(question: Question):
    return get_answer_to(question.q)