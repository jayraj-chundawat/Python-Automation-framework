import json
import os

class ConfigManager:

    def __init__(self, config_path="config/config.json"):
        config_file = os.path.abspath(config_path)

        with open(config_file, "r") as file:
            self.config = json.load(file)

        self.env = self.config["env"]

    def get_base_url(self):
        return self.config[self.env]["base_url"]

    def get_env(self):
        return self.env



