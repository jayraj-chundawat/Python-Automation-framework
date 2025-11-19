import json
from jsonschema import validate, ValidationError
import os

class SchemaValidator:

    @staticmethod
    def validate_response(schema_path, response_data):
        try:
            with open(schema_path, 'r') as schema_file:
                schema = json.load(schema_file)

            validate(instance=response_data, schema=schema)
            return True, None

        except ValidationError as ve:
            return False, f"Schema validation error: {ve.message}"


