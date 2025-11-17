import json
import os

class ConfigManager:

    def __init__(self, config_path="config/config.json"):
        config_file = os.path.abspath(config_path)
        with open(config_file, "r") as file:
            self.config = json.load(file)

