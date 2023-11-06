import weaviate
import json
import requests
from .weaviate_schema import class_obj
from ..utils.config import config, BOOKS_URL

class WeaviaClient:
    def __init__(self):
        self.client = weaviate.Client(**config)
        # self.setup() 

    def setup(self) -> None:
        # delete class "YourClassName" - THIS WILL DELETE ALL DATA IN THIS CLASS
        self.client.schema.delete_class("Book")  
        self.client.schema.create_class(class_obj)
        self._import_data()
    
    def _import_data(self) -> None:
        resp = requests.get(BOOKS_URL)
        data = json.loads(resp.text)

        self.client.batch.configure(batch_size=100)
        with self.client.batch as batch:
            for i, d in enumerate(data["books"]):
                print(f"importing question: {i+1}")
                properties = {
                    "isbn": d["isbn"],
                    "title": d["title"],
                    "subtitle": d["subtitle"],
                    "author": d["author"],
                    "published": d["published"],
                    "publisher": d["publisher"],
                    "pages": d["pages"],
                    "description": d["description"],
                    "website": d["website"]
                }
                batch.add_data_object(
                    data_object=properties,
                    class_name="Book"
                )
    
    def query(self, concepts) -> dict:
        response = (
            self.client.query
            .get("Book", ["title", "author", "description"])
            .with_near_text({"concepts": concepts})
            .with_limit(2)
            .do()
        )
        return response