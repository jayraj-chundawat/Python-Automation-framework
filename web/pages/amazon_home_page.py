from .base_page import BasePage
from playwright.sync_api import TimeoutError

class AmazonHomePage(BasePage):

    url = "https://www.amazon.in/"

    continue_shopping_btn = "text=Continue shopping"
    search_box = "input#twotabsearchtextbox"
    search_button = "input#nav-search-submit-button"

    def open_amazon(self):
        self.open_url(self.url)
        try:
            if self.page.is_visible(self.continue_shopping_btn):
                self.page.click(self.continue_shopping_btn)
        except TimeoutError:
            pass

    def search_product(self, text):
        try:
            if self.page.is_visible(self.continue_shopping_btn):
                self.page.click(self.continue_shopping_btn)
        except TimeoutError:
            pass

        self.page.wait_for_selector(self.search_box, timeout=15000)
        self.page.fill(self.search_box, text)
        self.page.click(self.search_button)
