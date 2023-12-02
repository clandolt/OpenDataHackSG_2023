from settings import ProjectSettings
from json_query_engine import QueryEngine
from json_query_engine import json_value, json_schema
from data_handler import DataHandler
if __name__ == '__main__':
    print("Project entry point")
    # Usage
    config = ProjectSettings.get_instance()

    # Accessing the variables
    print(config.OPENAI_API_KEY)
    print(config.DB_SERVER)
    print(config.DB_PORT)
    print(config.DB_NAME)
    print(config.COLLECTION_NAME)

    #query_engine = QueryEngine(config.OPENAI_API_KEY, json_value, json_schema)
    #print(query_engine.get_nl_response("How old is Anna Smith?"))
    #print(query_engine.get_raw_response("How old is Anna Smith?"))

    data_handler = DataHandler(config.DB_SERVER, config.DB_PORT, config.DB_NAME, config.COLLECTION_NAME)
    places = data_handler.get_places()
    for id, place in places:
        print(place)

    data_handler.close_connection()

