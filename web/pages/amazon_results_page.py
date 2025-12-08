from .base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class AmazonResultsPage(BasePage):

    # Product title selector
    product_title = "h2.a-size-medium.a-spacing-none.a-color-base.a-text-normal span"

    # Price selectors
    price_whole = "span.a-price-whole"
    price_offscreen = "span.a-offscreen"

    def auto_scroll(self):
        self.page.evaluate(
            """() => {
                window.scrollBy({
                    top: window.innerHeight,
                    left: 0,
                    behavior: 'smooth'
                });
            }"""
        )

    def get_results(self):
        for _ in range(14):
            self.auto_scroll()
            self.page.wait_for_timeout(600)

        try:
            self.page.wait_for_selector(self.product_title, timeout=30000)
        except PlaywrightTimeoutError:
            raise Exception(" Product titles not visible — Amazon may be blocking.")

        titles = self.page.locator(self.product_title).all_inner_texts()
        cleaned = [t.strip() for t in titles if t.strip()]

        if not cleaned:
            raise Exception(" No product titles found — Amazon changed UI.")

        return cleaned

    def get_prices(self):
        prices = []

        try:
            self.page.wait_for_selector(self.price_whole, timeout=15000)
            whole_prices = self.page.locator(self.price_whole).all_inner_texts()
            for p in whole_prices:
                c = p.replace(",", "").replace("₹", "").strip()
                if c.isdigit():
                    prices.append(int(c))
        except:
            pass

        try:
            off_prices = self.page.locator(self.price_offscreen).all_inner_texts()
            for p in off_prices:
                c = (
                    p.replace("₹", "")
                     .replace(",", "")
                     .replace(".00", "")
                     .strip()
                )
                if c.isdigit():
                    prices.append(int(c))
        except:
            pass

        if not prices:
            raise Exception(" No prices found — Amazon changed selectors.")

        return prices
