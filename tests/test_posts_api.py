import os
import pytest
from utils.schema_validator import SchemaValidator
from utils.data_loader import DataLoader


def test_get_post(post_service):
    status, response = post_service.get_post(1)

    assert status == 200
    assert response["id"] == 1
    assert "title" in response


def test_get_post_schema(post_service):
    status, response = post_service.get_post(1)

    assert status == 200

    schema_path = os.path.abspath("schemas/post_schema.json")
    is_valid, error = SchemaValidator.validate_response(schema_path, response)

    assert is_valid, f"Schema validation failed: {error}"


def test_create_post(post_service):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    status, response = post_service.create_post(payload)

    assert status == 201
    assert response["title"] == "foo"
    assert response["body"] == "bar"


def test_update_post(post_service):
    payload = {"title": "updated", "body": "changed", "userId": 1}
    status, response = post_service.update_post(1, payload)

    assert status == 200
    assert response["title"] == "updated"


def test_delete_post(post_service):
    status, response = post_service.delete_post(1)

    assert status in [200,204]
    assert response is None or response == {}


#  DATA-DRIVEN TEST USING JSON FILE
@pytest.mark.parametrize("payload", DataLoader.load_json("data/post_data.json"))
def test_create_post_ddt(post_service, payload):
    status, response = post_service.create_post(payload)

    assert status == 201
    assert response["title"] == payload["title"]
    assert response["body"] == payload["body"]


#  DATA-DRIVEN TEST USING CSV FILE
@pytest.mark.parametrize("payload", DataLoader.load_csv("data/post_data.csv"))
def test_create_post_csv_ddt(post_service, payload):
    status, response = post_service.create_post(payload)

    assert status == 201
    assert response["title"] == payload["title"]
    assert response["body"] == payload["body"]
