import pytest
import platform
from datetime import datetime
from api.services.post_services import PostService
from playwright.sync_api import sync_playwright


# -------------------- API FIXTURE --------------------
@pytest.fixture(scope="session")
def post_service():
    """Provides PostService instance for API test functions"""
    return PostService()


# -------------------- PLAYWRIGHT FIXTURE --------------------
@pytest.fixture(scope="function")
def browser(request):
    """
    Launch Playwright browser with anti-bot settings.
    Includes:
    - Human-like slow interactions
    - Updated user-agent
    - Auto screenshot on failure
    """
    with sync_playwright() as p:

        # Anti-bot browser launch
        browser = p.chromium.launch(
            headless=False,
            slow_mo=150,   # Slower = more human
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars",
                "--disable-dev-shm-usage",
                "--disable-gpu",
            ]
        )

        # Human-like browser context
        context = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/121.0.0.0 Safari/537.36"
            ),
            locale="en-US",
            timezone_id="Asia/Kolkata"
        )

        page = context.new_page()

        # --------- SCREENSHOT ON FAILURE ----------
        yield page

        if request.node.rep_call.failed:
            page.screenshot(path="reports/failure_screenshot.png")
            print("\n Screenshot captured: reports/failure_screenshot.png")

        browser.close()


# Introspect test outcome to detect failures
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


# -------------------- HTML REPORT TITLE --------------------
def pytest_html_report_title(report):
    report.title = "Python Automation Framework Report"


# -------------------- HTML REPORT CUSTOM METADATA --------------------
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        f"Project Name: Python API + Web Automation Framework",
        f"Tester: Jay Raj",
        f"Platform: {platform.system()}",
        f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    ])
