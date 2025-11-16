import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _create_url(self, endpoint):
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return self.base_url + endpoint

    def get(self, endpoint, params=None, headers=None):
        url = self._create_url(endpoint)
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(self, endpoint, data=None, json_data=None, headers=None):
        url = self._create_url(endpoint)
        response = requests.post(url, data=data, json=json_data, headers=headers)
        return response

