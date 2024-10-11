import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Error: Received status code {response.status_code}")
            return None

    def load_json(self):
        body = self.get_response_body()
        if body is not None:
            return json.loads(body)
        else:
            return None