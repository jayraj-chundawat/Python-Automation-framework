from jsonschema import validate, ValidationError

class SchemaValidator:

    @staticmethod
    def validate_response(schema, response_data):
        try:
            validate(instance=response_data, schema=schema)
            return True, None

        except ValidationError as ve:
            return False, f"Schema validation error: {ve.message}"

