from settings import ProjectSettings
from json_query_engine import QueryEngine
from json_query_engine import json_schema
from data_handler import DataHandler
if __name__ == '__main__':
    print("Project entry point")
    # Usage
    config = ProjectSettings.get_instance()

    """
    query_engine = QueryEngine(config.OPENAI_API_KEY, json_value, json_schema)
    print(query_engine.get_nl_response("What is the accessibility of the Foyer?"))
    #print(query_engine.get_raw_response("How old is Anna Smith?"))

    """
    data_handler = DataHandler(config.DB_SERVER, config.DB_PORT, config.DB_NAME, config.COLLECTION_NAME)
    places = data_handler.get_places()

    try:
        json_document = data_handler.get_json_values('656b62ad6fada3f2c0b08d5c')
        query_engine = QueryEngine(config.OPENAI_API_KEY, json_document, json_schema)
        print(query_engine.get_nl_response("Quel est le degré d'accessibilité de l'escalier du Naturmuseum St. Gallen?"))
    except Exception as e:
        print(e)
    data_handler.close_connection()

