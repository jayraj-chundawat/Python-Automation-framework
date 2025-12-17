import json
import pytest
from web.pages.amazon_home_page import AmazonHomePage
from web.pages.amazon_results_page import AmazonResultsPage

# Load data from JSON
with open("web/data/search_data.json") as f:
    test_data = json.load(f)

@pytest.mark.parametrize("data", test_data)
def test_amazon_search_data(browser, data):

    product = data["product"]

    home = AmazonHomePage(browser)
    home.open_amazon()
    home.search_product(product)

    results_page = AmazonResultsPage(browser)
    results = results_page.get_results()

    assert len(results) > 0, f"No results found for {product}"
    assert any(
        product.lower() in r.lower() or
        "galaxy" in r.lower()
        for r in results
    ), f"{product} related products not found!"

