import pytest
from api.services.post_services import PostService

@pytest.fixture(scope="session")
def post_service():
    """Provides PostService instance for test functions"""
    return PostService()

