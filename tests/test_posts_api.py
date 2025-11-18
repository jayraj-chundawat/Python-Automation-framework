def test_get_post(post_service):
    status, response = post_service.get_post(1)

    assert status == 200
    assert response["id"] == 1
