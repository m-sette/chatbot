from weaviate import Client
from ..db.weaviate_client import WeaviaClient
from ..utils.config import config


def get_answer_to(question: str) -> dict:
    client = WeaviaClient(Client(**config), False)

    answer = client.ask_question(question)
    return {"question": question, "data": answer}