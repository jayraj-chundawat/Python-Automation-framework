from api.services.post_services import PostService

if __name__ == "__main__":
    service = PostService()

    # Test GET
    status, response = service.get_post(1)
    print("GET Status:", status)
    print("GET Response:", response)

    # Test POST
    payload = {"title": "foo", "body": "bar", "userId": 1}
    status, response = service.create_post(payload)
    print("\nPOST Status:", status)
    print("POST Response:", response)

    # Test PUT
    update_payload = {"title": "updated title", "body": "updated body", "userId": 1}
    status, response = service.update_post(1, update_payload)
    print("\nPUT Status:", status)
    print("PUT Response:", response)

    # Test DELETE
    status, response = service.delete_post(1)
    print("\nDELETE Status:", status)
    print("DELETE Response:", response)



