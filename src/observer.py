from json_query_engine import QueryEngine
from json_query_engine import json_schema
from data_handler import DataHandler
from settings import ProjectSettings

# Frontend Observer
class FrontendObserver:
    def __init__(self):
        self.dash_app = None

    def update(self, data):
        print(f"Received data in frontend: {data}")
        self.dash_app.set_answer(data)
        # Perform actions based on received data

    def set_dash_app(self, dash_app):
        self.dash_app = dash_app


# Backend Observer
class BackendObserver:

    def __init__(self, frontend_observer):
        self.frontend_observer = frontend_observer
        self.config = ProjectSettings.get_instance()
        self.data_handler = DataHandler(self.config.DB_SERVER, self.config.DB_PORT, self.config.DB_NAME, self.config.COLLECTION_NAME)

    def update(self, data):
        print(f"Received data in backend: {data[2]}")
        query_string = data[2]
        document_id = self.data_handler.get_document_id(data[0], data[1])
        try:
            json_document = self.data_handler.get_json_values(document_id)
            query_engine = QueryEngine(self.config.OPENAI_API_KEY, json_document, json_schema)
            query_engine.attach(self.frontend_observer)
            response = query_engine.get_nl_response(query_string)
            query_engine.notify(response)
        except Exception as e:
            print(e)
        9#self.data_handler.close_connection()
        # Process data and take necessary actions
