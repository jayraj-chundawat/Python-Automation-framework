import requests
from utils.logger import Logger


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.logger = Logger().get_logger()

    def _create_url(self, endpoint):
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return self.base_url + endpoint

    def get(self, endpoint, params=None, headers=None):
        url = self._create_url(endpoint)
        self.logger.info(f"GET Request to URL: {url}, Params: {params}, Headers: {headers}")

        response = requests.get(url, params=params, headers=headers)

        self.logger.info(f"GET Response: {response.status_code}, Body: {response.text}")
        return response

    def post(self, endpoint, data=None, json_data=None, headers=None):
        url = self._create_url(endpoint)
        self.logger.info(f"POST Request to URL: {url}, Data: {data}, JSON: {json_data}, Headers: {headers}")

        response = requests.post(url, data=data, json=json_data, headers=headers)

        self.logger.info(f"POST Response: {response.status_code}, Body: {response.text}")
        return response

    def put(self, endpoint, json_data=None, headers=None):
        url = self._create_url(endpoint)
        self.logger.info(f"PUT Request to URL: {url}, JSON: {json_data}, Headers: {headers}")

        response = requests.put(url, json=json_data, headers=headers)

        self.logger.info(f"PUT Response: {response.status_code}, Body: {response.text}")
        return response

    def delete(self, endpoint, headers=None):
        url = self._create_url(endpoint)
        self.logger.info(f"DELETE Request to URL: {url}, Headers: {headers}")

        response = requests.delete(url, headers=headers)

        self.logger.info(f"DELETE Response: {response.status_code}, Body: {response.text}")
        return response

    def _handle_response(self, response):
        """Return (status_code, json/text)"""
        try:
            status = response.status_code
            try:
                body = response.json()
            except ValueError:
                body = response.text

            return status, body
        except Exception as e:
            self.logger.error(f"Response handling failed: {e}")
            raise
