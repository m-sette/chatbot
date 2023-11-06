from ..db.weaviate_client import WeaviaClient
from ..utils.config import config


def get_answer_to(question) -> dict:
    client = WeaviaClient()

    answer = client.query([question])
    return {"question": question, "data": answer}