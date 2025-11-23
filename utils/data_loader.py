import json
import os

class DataLoader:

    @staticmethod
    def load_json(file_path):
        abs_path = os.path.abspath(file_path)
        with open(abs_path, "r") as file:
            return json.load(file)
