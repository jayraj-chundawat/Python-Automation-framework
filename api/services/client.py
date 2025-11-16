import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _create_url(self, endpoint):
        """Combine base URL + endpoint correctly"""
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return self.base_url + endpoint

