from json_query_engine import QueryEngine
from json_query_engine import json_schema
from data_handler import DataHandler
from settings import ProjectSettings

# Frontend Observer
class FrontendObserver:
    def update(self, data):
        print(f"Received data in frontend: {data}")
        # Perform actions based on received data


# Backend Observer
class BackendObserver:

    def __init__(self):
        self.config = ProjectSettings.get_instance()
        self.data_handler = DataHandler(self.config.DB_SERVER, self.config.DB_PORT, self.config.DB_NAME, self.config.COLLECTION_NAME)

    def update(self, data):
        print(f"Received data in backend: {data[2]}")
        try:
            json_document = self.data_handler.get_json_values('656b62ad6fada3f2c0b08d5c')
            query_engine = QueryEngine(self.config.OPENAI_API_KEY, json_document, json_schema)
            print(query_engine.get_nl_response("Quel est le degré d'accessibilité de l'escalier du Naturmuseum St. Gallen?"))
        except Exception as e:
            print(e)
        self.data_handler.close_connection()
        # Process data and take necessary actions
