from settings import ProjectSettings
from data_handler import DataHandler
from dash_app import OpenDataDashApp
from observer import FrontendObserver, BackendObserver
if __name__ == '__main__':
    print("Project entry point")
    # Usage
    config = ProjectSettings.get_instance()

    # Creating observers
    frontend_observer = FrontendObserver()
    backend_observer = BackendObserver()

    """
    query_engine = QueryEngine(config.OPENAI_API_KEY, json_value, json_schema)
    print(query_engine.get_nl_response("What is the accessibility of the Foyer?"))
    #print(query_engine.get_raw_response("How old is Anna Smith?"))

    """
    data_handler = DataHandler(config.DB_SERVER, config.DB_PORT, config.DB_NAME, config.COLLECTION_NAME)
    places = data_handler.get_places()
    print(places)

    open_data_app = OpenDataDashApp(places)
    open_data_app.attach(backend_observer)
    
    open_data_app.run_server()
