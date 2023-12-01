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

# Define the list of URLs
url_list = [
    'https://api.ginto.guide/entries/b840c301-5c17-455b-9768-e67c0e9812f0',
    'https://api.ginto.guide/entries/54c949b4-19cd-4e39-89a2-df95a1b49725',
    'https://api.ginto.guide/entries/4192b1be-329f-45e7-93bc-1494656f5655',
    'https://api.ginto.guide/entries/6b1bf6a5-06de-4817-9f26-0855f38f26ff',
    'https://api.ginto.guide/entries/ecdef361-3994-433d-87c2-b2ceaba36cfe',
    'https://api.ginto.guide/entries/1ed2dce2-8710-4b72-8658-5ac1787adafa',
    'https://api.ginto.guide/entries/6b1c627f-c2f8-4bc7-9e6c-e782962d1ad7',
    'https://api.ginto.guide/entries/f06b9f7e-8682-420e-a7d2-fee63bddc129',
    'https://api.ginto.guide/entries/980c7456-b97f-414f-bf4e-0c507b28bd1f',
    'https://api.ginto.guide/entries/f9286e20-ec0f-4386-8e0c-eea1d28536f8',
    'https://api.ginto.guide/entries/c2f05729-cf92-4821-af64-c34e24c5b89a',
    'https://api.ginto.guide/entries/f19a2773-858e-4e85-ba17-e04029dd1283',
    'https://api.ginto.guide/entries/d783678b-e680-4d1a-8ee4-88b6ca4b0cc6',
    'https://api.ginto.guide/entries/8dd99fab-df77-41fc-9b04-d1c9a6e7eb3d',
    'https://api.ginto.guide/entries/a7a0ed75-d11b-43c5-82f1-757a751cdc52'

]
# Create the Web Crawler object
crawler = WebCrawler(url_list, "my_database", "my_collection")
# Download and store the Data
crawler.download_and_store()