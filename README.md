
# Python Automation Framework

A complete end-to-end automation framework combining API testing, Web UI testing, and data-driven testing using:
1.Python 3.12
2.PyTest framework
3.Playwright (Web Automation)
4.Requests library (API Testing)
5.Schema validation (JSON Schema)
6.Data-driven testing (CSV/JSON)
7.HTML Reporting + Screenshot on Failure
8.Page Object Model (POM) for Web Automation

# Project Folder Structure

automation-framework/
│
├── api/
│   ├── services/
│   │   ├── client.py
│   │   ├── post_services.py
│
├── config/
│   ├── config.json
│   ├── config_manager.py
│
├── data/
│   ├── post_data.csv
│   ├── post_data.json
│
├── reports/      
│      (HTML reports + screenshots auto-generated here)
│
├── schemas/
│   ├── post_schemas.json
│
├── tests/
│   ├── test_posts_api.py
│
├── utils/
│   ├── data_loader.py
│   ├── logger.py
│   ├── schema_validator.py
│
├── web/
│   ├── data/
│   │   ├── search_data.json
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── amazon_home_page.py
│   │   ├── amazon_results_page.py
│   ├── tests/
│   │   ├── test_amazon_search.py
│   │   ├── test_amazon_search_data_driven.py
│   │   ├── test_amazon_price_check.py
│
├── conftest.py
├── main.py
├── pytest.ini
├── requirements.txt
├── README.md


# Folder-by-Folder Explanation

1.api - Contains the API automation module.
 a) services/client.py - Generic API client (GET/POST/PUT/DELETE wrapper) 
                         Uses requests
                         Reads base URL from configuration
 b) services/post_services.py - API class for working with /posts API
                                Methods → get_post, create_post, update_post, etc.

2.config - Contains configuration files.
 a) config.json - Stores base URLs, environment, and other variables.
 b) config_manager.py - Loads config file and exposes values to the framework.

3.data - Contains test data for data-driven API testing.
 a) post_data.csv - test cases for API POST operations
 b) post_data.json → JSON format of sample API payloads

4.reports - remains empty,At runtime → Playwright + PyTest HTML reports + screenshots saved here.
            HTML Report: After execution → report saved in - reports/report.html
                                                             reports/failure_screenshot.png
                                                             
5.schemas - Contains JSON schema files for validating API response structures,Used with jsonschema validator.

6.tests - Contains API test scripts.
          GET request validation
          POST request using CSV/JSON data
          Schema validation
          Status code + response checks

7.utils - Helper utilities.
 a) data_loader.py - Loads CSV/JSON test data,Provides reusable data-driven methods
 b) logger.py - Logger for debugging & reporting
 c) schema_validator.py - Validates API responses using JSON schema

8. web - Playwright-based Web Automation module.
   web/data/ - Holds datasets for web data-driven tests.
   web/pages/ - Implements Page Object Model (POM).
    a) base_page.py - Common methods, (open_url, click, type_text, wait, visibility check)
    b) amazon_home_page.py - Opens Amazon,Handles "Continue shopping" anti-bot screen,Searches products
    c) amazon_results_page.py - Auto-scroll,Extract product titles,Extract product prices,Handles Amazon anti-bot behavior
   web/tests/ - Contains web automation test cases.
    a) test_amazon_search.py - Validates that search returns results,Uses POM,Handles Amazon anti-bot page
    b) test_amazon_search_data_driven.py - Data-driven web search,Iterates search terms from search_data.json

9. conftest.py - Global PyTest configuration:API fixture (post_service),Browser fixture (Playwright),Screenshot on failure,HTML report customization
10. main.py - Entry point to run framework modules .
11. pytest.ini - Stores PyTest settings:HTML report path,Logging,Test discovery patterns
12. requirements.txt - framework requirement details (libraries).

# How to Run Tests
 1. Run API tests - py -m pytest tests/test_posts_api.py -v
 2. Run Web search test - py -m pytest web/tests/test_amazon_search.py -v
 3. Run Data-driven web test - py -m pytest web/tests/test_amazon_search_data_driven.py -v
 4. Run entire framework - py -m pytest -v

    
                 

                      
