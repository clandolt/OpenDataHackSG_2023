import pymongo
from bson import ObjectId

class DataHandler:
    """
    This class is a abstraction-Layer between the application and the database.
    
    ...

    Attributes
    ----------
    _instance : DataHandler
        This variable contains the singelton object of the DataHandler Class.

    Methods
    -------
    get_places()
        Returns a list of all places which are in the Database
    close_connection()
        Closes the connection to the Database
    """
    _instance = None

    def __new__(cls, server_name : str, server_port : str, database_name : str, collection_name : str):
        """
        This method is singelton and creates a unique database connection

        Parameters
        ----------
        server_name : str
            Name of the Database-Server
        server_port : str
            Port of the Database
        database_name : str
            Name of the Database
        collection_name : str
            Name of the JSON-File Collection

        Returns
        -------
        DataHandler
            Returns a singelton Object of the DataHandler-Class
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = pymongo.MongoClient(f"mongodb://{server_name}:{server_port}/")
            cls._instance.db = cls._instance.client[database_name]
            cls._instance.collection = cls._instance.db[collection_name]
        return cls._instance

    def get_places(self) -> list:
        """
        This method returns a list of tuples containing the id and name of the place

        Returns
        -------
        list(tuple)
            Returns a list of tuples like the following: (id, name)
        """
        results = self.collection.find({}, {"_id": 1, "name": 1})
        places = []
        for result in results:
            places.append((result['_id'], result.get('name', 'N/A')))
        return list(set(name for _, name in places if name != 'N/A'))
    
    def get_json_values(self, id : str):
        # Example ObjectId (replace with your specific _id)
        document_id = ObjectId(id)

        # Find document by _id
        result = self.collection.find_one({"_id": document_id})

        if result:
            return result
        else:
            raise Exception("Document not found")


    def get_document_id(self, search_name, search_category):
        result = self.collection.find_one({"name": search_name, "category": search_category})

        if result:
            return str(result["_id"])

    def close_connection(self) -> None:
        """
        This method closes the database connection
        """
        self.client.close()
