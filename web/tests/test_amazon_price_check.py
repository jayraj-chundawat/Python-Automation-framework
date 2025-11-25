from web.pages.amazon_home_page import AmazonHomePage
from web.pages.amazon_results_page import AmazonResultsPage

def test_amazon_price_display(browser):

    home = AmazonHomePage(browser)
    home.open_amazon()
    home.search_product("iPhone")

    results = AmazonResultsPage(browser)

    titles = results.get_results()
    prices = results.get_prices()

    assert len(titles) > 0
    assert len(prices) > 0
    assert len(titles) == len(prices) or len(prices) > 5

    print("Sample prices:", prices[:5])
