from ..db.weaviate_client import WeaviaClient
from ..utils.config import config


def get_answer_to(question) -> dict:
    client = WeaviaClient()

    answer = client.ask_question([question])
    return {"question": question, "data": answer}