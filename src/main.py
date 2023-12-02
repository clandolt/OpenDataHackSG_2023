from settings import ProjectSettings
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