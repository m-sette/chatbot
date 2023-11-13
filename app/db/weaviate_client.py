from pydantic import Json
import weaviate
import json
import requests
from .weaviate_schema import class_obj
from ..utils.config import BOOKS_URL

class WeaviaClient:
    def __init__(self, client: weaviate.Client ,recreate: bool = False):
        self._client = client
        
        if recreate:
            self._setup() 
        
    def ask_question(self, concepts) -> dict:
        """Queries Weaviate for books related to the given concepts."""
        try:
            response = (
                self._client.query
                .get("Book", ["title", "author", "description"])
                .with_near_text({"concepts" : concepts})
                .with_limit(2)
                .do()
            )
            return response
        except Exception as e:
            print(f"Error querying Weaviate: {e}")
            return {}
    
    def _setup(self) -> None:
        """Sets up the Weaviate schema and imports data."""
        try:
            self._client.schema.delete_class("Book")  
            self._client.schema.create_class(class_obj)
            self._import_data()
        except Exception as e:
            print(f"Error setting up Weaviate schema: {e}")
    
    def _import_data(self) -> None:
        """Imports data from the BOOKS_URL into Weaviate."""
        try:
            data = json.loads(requests.get(BOOKS_URL).text)
        except Exception as e:
            print(f"Error fetching data from {BOOKS_URL}: {e}")
            return

        self._client.batch.configure(batch_size=100)
        with self._client.batch as batch:
            for i, book in enumerate(data["books"]):
                print(book)
                # print(f"importing book: {i+1}")
                batch.add_data_object(
                    data_object=book,
                    class_name="Book"
                )