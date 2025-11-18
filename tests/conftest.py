import pytest
import platform
from api.services.post_services import PostService

@pytest.fixture(scope="session")
def post_service():
    return PostService()

def pytest_html_report_title(report):
    report.title = "Python API Automation Test Report"

def pytest_html_results_summary(prefix, summary, postfix):
    """Add metadata or details to the summary section of the report"""
    prefix.extend([f"Project Name: Python API Automation Framework"])
    prefix.extend([f"Tester: Jay raj"])  # Replace as needed
    prefix.extend([f"Platform: {platform.system()}"])



