import json
import csv
import os


class DataLoader:

    @staticmethod
    def load_json(file_path):
        abs_path = os.path.abspath(file_path)
        with open(abs_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def load_csv(file_path):
        abs_path = os.path.abspath(file_path)
        data_list = []

        with open(abs_path, "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row.get("userId") and row["userId"].isdigit():
                    row["userId"] = int(row["userId"])
                data_list.append(row)

        return data_list
