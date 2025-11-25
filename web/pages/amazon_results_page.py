from .base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class AmazonResultsPage(BasePage):

    product_title = "h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal span"

    def auto_scroll(self):
        self.page.evaluate(
            "() => window.scrollBy({top: window.innerHeight, behavior: 'smooth'})"
        )

    def get_results(self):
        for _ in range(12):
            self.auto_scroll()
            self.page.wait_for_timeout(600)

        try:
            self.page.wait_for_selector(self.product_title, timeout=25000)
        except PlaywrightTimeoutError:
            raise Exception(" Product titles not visible.")

        titles = self.page.locator(self.product_title).all_inner_texts()
        cleaned = [t.strip() for t in titles if t.strip()]

        if not cleaned:
            raise Exception(" No titles found.")

        return cleaned
