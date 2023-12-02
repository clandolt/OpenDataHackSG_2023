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

    def __init__(self, url_list, server_name, server_port, database_name, collection_name):
        """
        Parameters
        ----------
        url_list : list[str]
            List of urls to the JSON-Files as string.

        server_name : str
        server_port : str
        database_name : str
            Name of the Database
        collection_name : str
            Name of the collection
        """
        self.url_list = url_list
        self.database_name = database_name
        self.collection_name = collection_name
        self.server_name = server_name
        self.server_port = server_port
        self.query_strings = [
            (78, 'Active wheelchair'), 
            (81, 'No limitations'),
            (79, 'E-wheelchair'),
            (80, 'Stroller'),
            (3951, 'Scewo BRO')
            ]

    def download_and_store(self) -> None:
        """
        This function initiates the download and storage.
        """
        for url in self.url_list:
            self._download_json(url)

    # Define a function to replace grade values with accessibility descriptions
    def _replace_accessibility(self, grade):
        if grade == 1:
            return "Completely accessible"
        elif grade == 2:
            return "Partially accessible"
        elif grade == 3:
            return "Not easily accessible"
        else:
            return "Unknown accessibility"
        
    def _traverse_and_replace(self, obj):
        if isinstance(obj, dict):
            if "accessibility" in obj and "grade" in obj["accessibility"]:
                obj["accessibility"]["grade"] = self._replace_accessibility(obj["accessibility"]["grade"])
            for value in obj.values():
                self._traverse_and_replace(value)
        elif isinstance(obj, list):
            for item in obj:
                self._traverse_and_replace(item)

    def _remove_not_needed_keys(self, obj):
        list_of_keys = [
            "version",
            "createdAt",
            "updatedAt",
            "url",
            "accessUrl",
            "approval",
            "readyForApproval",
            "ratingProfileNotice",
            "status",
            "webUrl",
            "resourceUrl",
            "changesUrl",
            "attributionUrl",
            "isOpenData",
            "license",
            "position",
            "mainImage",
            "totalClassifications",
            "companyAssignment",
            "numberOfComments",
            "structure",
            "areaClassifications"
        ]

        for key in list_of_keys:
            if key in obj:
                obj.pop(key)

        if 'accessibility' in obj and isinstance(obj['accessibility'], dict):
            grade_value = obj['accessibility'].get('grade')
            obj['accessibility'] = grade_value

    def _remove_property_values(self, obj):
        if isinstance(obj, dict):
            obj.pop("propertyValues", None)  # Remove propertyValues if present
            for value in obj.values():
                self._remove_property_values(value)
        elif isinstance(obj, list):
            for item in obj:
                self._remove_property_values(item)


    def _modify_structure(self, obj):
        if isinstance(obj, dict):
            if "accessibility" in obj and isinstance(obj["accessibility"], dict):
                obj["accessibility"] = obj["accessibility"].get("grade", None)

            obj.pop("readyForApproval", None)

            obj.pop("images", None)

            for value in obj.values():
                self._modify_structure(value)
        elif isinstance(obj, list):
            for item in obj:
                self._modify_structure(item)

    def _move_criterion_values(self, obj):
        if "pathClassifications" in obj and isinstance(obj["pathClassifications"], list):
            for item in obj["pathClassifications"]:
                if "criterion" in item:
                    criterion_values = item.pop("criterion")
                    item.update(criterion_values)



    def _download_json(self, input_url : str) -> None:
        """
        This provate function downloads the JSCOn data from a specific internet ressource and initiates the storage in the MongoDB

        Parameters
        ----------
        url : str
            url to the JSON-File
        """
        for id, description in self.query_strings:
            url = input_url + "?rating_profile_id="+str(id)
            try:
                response = requests.get(url, verify=False)
                if response.status_code == 200:
                    data = response.json()
                    self._traverse_and_replace(data)
                    self._remove_not_needed_keys(data)
                    self._remove_property_values(data)
                    self._move_criterion_values(data)
                    self._modify_structure(data)
                    data["category"] = description
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
        client = pymongo.MongoClient(f"mongodb://{self.server_name}:{self.server_port}/")
        db = client[self.database_name]
        collection = db[self.collection_name]
        collection.insert_one(data)
        client.close()