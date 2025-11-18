def test_get_post(post_service):
    status, response = post_service.get_post(1)

    assert status == 200
    assert response["id"] == 1

def test_create_post(post_service):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    status, response = post_service.create_post(payload)

    assert status == 201
    assert response["title"] == "foo"

def test_update_post(post_service):
    payload = {"title": "updated", "body": "changed", "userId": 1}
    status, response = post_service.update_post(1, payload)

    assert status == 200
    assert response["title"] == "updated"

def test_delete_post(post_service):
    status, response = post_service.delete_post(1)

    assert status == 200
    assert response in ({}, None)  # Depends on API response

