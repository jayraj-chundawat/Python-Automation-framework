from .base_page import BasePage

class AmazonHomePage(BasePage):

    url = "https://www.amazon.in/"
    
    continue_shopping_btn = "text=Continue shopping"
    search_box = "input#twotabsearchtextbox"
    search_button = "input#nav-search-submit-button"

    def open_amazon(self):
        self.open_url(self.url)
        if self.page.is_visible(self.continue_shopping_btn):
            self.page.click(self.continue_shopping_btn)

    def search_product(self, text):
        if self.page.is_visible(self.continue_shopping_btn):
            self.page.click(self.continue_shopping_btn)

        self.page.wait_for_selector(self.search_box)
        self.page.fill(self.search_box, text)
        self.page.click(self.search_button)
