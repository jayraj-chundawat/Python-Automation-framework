import pytest
import platform
from datetime import datetime
from api.services.post_services import PostService  # Adjust if needed

@pytest.fixture(scope="session")
def post_service():
    """Provides PostService instance for test functions"""
    return PostService()

def pytest_html_report_title(report):
    """Customize the title of the HTML report"""
    report.title = "Python API Automation Test Report"

def pytest_html_results_summary(prefix, summary, postfix):
    """Add metadata or details to the summary section of the report"""
    prefix.extend([f"Project Name: Python API Automation Framework"])
    prefix.extend([f"Tester: Jay raj"])  # Replace with your name
    prefix.extend([f"Platform: {platform.system()}"])
    prefix.extend([f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])




