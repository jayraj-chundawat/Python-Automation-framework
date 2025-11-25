from .base_page import BasePage

class AmazonResultsPage(BasePage):

    product_title = "h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal span"

    def auto_scroll(self):
        self.page.evaluate("() => window.scrollBy(0, window.innerHeight)")

    def get_results(self):
        for _ in range(10):
            self.auto_scroll()
            self.page.wait_for_timeout(500)

        self.page.wait_for_selector(self.product_title)
        return self.page.locator(self.product_title).all_inner_texts()
