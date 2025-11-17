from api.services.client import APIClient
from config.config_manager import ConfigManager


class PostService(APIClient):

    def __init__(self):
        config = ConfigManager()
        base_url = config.get_base_url()

        super().__init__(base_url)

    def get_post(self, post_id):
        return self._handle_response(self.get(f"/posts/{post_id}"))

    def create_post(self, payload):
        return self._handle_response(self.post("/posts", json_data=payload))

    def update_post(self, post_id, payload):
        return self._handle_response(self.put(f"/posts/{post_id}", json_data=payload))

    def delete_post(self, post_id):
        return self._handle_response(self.delete(f"/posts/{post_id}"))



