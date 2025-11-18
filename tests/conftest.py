import pytest
from api.services.post_services import PostService

@pytest.fixture(scope="session")
def post_service():
    return PostService()

def pytest_html_report_title(report):
    """Customize the title of the HTML report"""
    report.title = "Python API Automation Test Report"


