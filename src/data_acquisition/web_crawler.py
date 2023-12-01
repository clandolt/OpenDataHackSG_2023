import requests
import json

class WebCrawler:
    def __init__(self, url):
        self.url = url

    def download_json(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Failed to download JSON. Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

# Example usage:
url_list = [
    'https://api.ginto.guide/entries/b840c301-5c17-455b-9768-e67c0e9812f0',
    'https://api.ginto.guide/entries/54c949b4-19cd-4e39-89a2-df95a1b49725',
    'https://api.ginto.guide/entries/4192b1be-329f-45e7-93bc-1494656f5655',
    'https://api.ginto.guide/entries/6b1bf6a5-06de-4817-9f26-0855f38f26ff',
    'https://api.ginto.guide/entries/ecdef361-3994-433d-87c2-b2ceaba36cfe',
    'https://api.ginto.guide/entries/1ed2dce2-8710-4b72-8658-5ac1787adafa',
    
]
url_to_crawl = "https://example.com/data.json"  # Replace with your desired URL
crawler = WebCrawler(url_to_crawl)
downloaded_data = crawler.download_json()

if downloaded_data:
    # Do something with the downloaded data
    print(json.dumps(downloaded_data, indent=4))