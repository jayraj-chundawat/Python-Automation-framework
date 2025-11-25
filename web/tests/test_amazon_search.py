import pytest
from web.pages.amazon_home_page import AmazonHomePage
from web.pages.amazon_results_page import AmazonResultsPage

def test_amazon_search(browser):
    home = AmazonHomePage(browser)

    # Open Amazon homepage
    home.open_amazon()

    # Perform search
    home.search_product("iPhone")

    # Navigate to results page
    results_page = AmazonResultsPage(browser)
    results = results_page.get_results()

    # Assertions
    assert results is not None and len(results) > 0, " No search results found!"

    assert any("iphone" in result.lower() for result in results), \
        " Expected product 'iPhone' not found in Amazon results"
