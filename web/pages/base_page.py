from playwright.sync_api import Page, TimeoutError

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url):
        try:
            self.page.goto(url, timeout=30000)
        except TimeoutError:
            raise Exception(f" Failed to open URL: {url}")

    def click(self, selector):
        try:
            self.page.wait_for_selector(selector, timeout=15000)
            self.page.click(selector)
        except TimeoutError:
            raise Exception(f" Element not clickable: {selector}")

    def type_text(self, selector, text):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, text)

    def get_text(self, selector):
        self.page.wait_for_selector(selector)
        return self.page.inner_text(selector)

    def wait_for_element(self, selector):
        self.page.wait_for_selector(selector, timeout=15000)

    def is_visible(self, selector):
        try:
            return self.page.is_visible(selector)
        except:
            return False
