import os
from dataclasses import dataclass
from dotenv import dotenv_values

@dataclass
class ProjectSettings:
    OPENAI_API_KEY: str
    DB_SERVER: str
    DB_PORT: int
    DB_NAME: str
    COLLECTION_NAME: str

    _instance = None  # Private variable to hold the instance

    def __init__(self):
        if self._instance is not None:
            raise RuntimeError("Cannot instantiate singleton class EnvConfig")
        
        # Get the directory where the current Python file is located
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Load the .env file from the current directory
        dotenv_path = os.path.join(current_directory, '.env')

        env_values = dotenv_values(dotenv_path)
        self.OPENAI_API_KEY = env_values["OPENAI_API_KEY"]
        self.DB_SERVER = env_values["DB_SERVER"]
        self.DB_PORT = int(env_values["DB_PORT"])
        self.DB_NAME = env_values["DB_NAME"]
        self.COLLECTION_NAME = env_values["COLLECTION_NAME"]

        ProjectSettings._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

