from api.services.post_services import PostService

if __name__ == "__main__":
    service = PostService()
    status, response = service.get_post(1)

    print("GET Status:", status)
    print("GET Response:", response)

