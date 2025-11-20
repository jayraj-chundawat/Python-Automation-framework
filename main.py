from api.services.post_services import PostService

if __name__ == "__main__":
    service = PostService()

    # Test GET
    status, response = service.get_post(1)
    print("GET:", status, response)

    # Test POST
    payload = {"title": "foo", "body": "bar", "userId": 1}
    status, response = service.create_post(payload)
    print("POST:", status, response)


