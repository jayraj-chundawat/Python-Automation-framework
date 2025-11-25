from playwright.sync_api import Page, expect

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url):
        """Open a given URL."""
        self.page.goto(url)

    def open(self, url):
        """Compatibility method for open() calls."""
        self.page.goto(url)

    def click(self, selector):
        """Click an element using a CSS/XPath/Role selector."""
        self.page.click(selector)

    def type_text(self, selector, text):
        """Type text in an input field."""
        self.page.fill(selector, text)

    def get_text(self, selector):
        """Return the inner text of an element."""
        return self.page.inner_text(selector)

    def wait_for_element(self, selector):
        """Wait until element is visible."""
        self.page.wait_for_selector(selector)

    def is_visible(self, selector):
        """Check if an element is visible."""
        return self.page.is_visible(selector)
