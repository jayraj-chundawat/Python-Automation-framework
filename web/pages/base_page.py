from playwright.sync_api import Page, TimeoutError

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url):
        try:
            self.page.goto(url, timeout=30000)
        except Exception as e:
            self._fail(f"Failed to open URL: {url}", e)

    def click(self, selector):
        try:
            self.page.wait_for_selector(selector, timeout=20000)
            self.page.click(selector)
        except Exception as e:
            self._fail(f"Failed to click element: {selector}", e)

    def type_text(self, selector, text):
        try:
            self.page.wait_for_selector(selector, timeout=15000)
            self.page.fill(selector, text)
        except Exception as e:
            self._fail(f"Failed to type text into: {selector}", e)

    def get_text(self, selector):
        try:
            self.page.wait_for_selector(selector)
            return self.page.inner_text(selector)
        except Exception as e:
            self._fail(f"Failed to get text from: {selector}", e)

    def wait_for_element(self, selector):
        try:
            self.page.wait_for_selector(selector, timeout=15000)
        except Exception as e:
            self._fail(f"Element not visible: {selector}", e)

    def _fail(self, msg, error):
        """Auto screenshot + raise readable error."""
        screenshot_path = f"reports/error_{self.page.guid}.png"
        self.page.screenshot(path=screenshot_path)
        raise Exception(f"{msg}\nScreenshot: {screenshot_path}\nDetails: {error}")
