import requests
import pymongo

class WebCrawler:
    """
    This class handles the download of the JSON Data and the storage of the data in a MongoDB

    ...

    Attributes
    ----------
    url_list : list[str]
        List of url to the JSON-Data
    database_name : str
        The name of the Database
    collection_name : str
        The name of the Collection where the JSON-Data is stored.

    Methods
    -------
    download_and_store()
        This function initiates the download of the Data
    _download_json()
        This Function donloads the JSON File and initiates the storage.
    store_in_mongodb(data : dict)
        This function stores the JSON-Data
    """

    def __init__(self, url_list, database_name, collection_name):
        """
        Parameters
        ----------
        url_list : list[str]
            List of urls to the JSON-Files as string.
        database_name : str
            Name of the Database
        collection_name : str
            Name of the collection
        """
        self.url_list = url_list
        self.database_name = database_name
        self.collection_name = collection_name

    def download_and_store(self) -> None:
        """
        This function initiates the download and storage.
        """
        for url in self.url_list:
            self._download_json(url)


    def _download_json(self, url : str) -> None:
        """
        This provate function downloads the JSCOn data from a specific internet ressource and initiates the storage in the MongoDB

        Parameters
        ----------
        url : str
            url to the JSON-File
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.store_in_mongodb(data)
            else:
                print(f"Failed to download JSON. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
        
    def store_in_mongodb(self, data : dict) -> None:
        """
        This function stores the downloaded JSON-File in the MongoDB

        Parameters
        ----------
        data : dict
            The JSON-File as dict
        """
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client[self.database_name]
        collection = db[self.collection_name]
        collection.insert_one(data)
        client.close()