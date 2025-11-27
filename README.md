# Python Automation Framework

A complete end-to-end automation framework combining:

- **Python 3.12**  
- **PyTest** (Automation framework)  
- **Playwright** (Web UI Automation)  
- **Requests** (API Testing)  
- **JSON Schema Validation**  
- **Data-driven Testing (CSV + JSON)**  
- **HTML Reporting + Screenshot on Failure**  
- **Page Object Model (POM)** for Web Automation  

---

# Project Folder Structure

```
automation-framework/
│
├── api/
│   └── services/
│       ├── client.py
│       └── post_services.py
│
├── config/
│   ├── config.json
│   └── config_manager.py
│
├── data/
│   ├── post_data.csv
│   └── post_data.json
│
├── reports/
│      (HTML reports + screenshots auto-generated here)
│
├── schemas/
│   └── post_schemas.json
│
├── tests/
│   └── test_posts_api.py
│
├── utils/
│   ├── data_loader.py
│   ├── logger.py
│   └── schema_validator.py
│
├── web/
│   ├── data/
│   │   └── search_data.json
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── amazon_home_page.py
│   │   └── amazon_results_page.py
│   └── tests/
│       ├── test_amazon_search.py
│       ├── test_amazon_search_data_driven.py
│       └── test_amazon_price_check.py
│
├── conftest.py
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Folder-by-Folder Explanation

### **1. api/**
API automation module:

- `client.py` → Generic API client (GET, POST, PUT, DELETE)  
- `post_services.py` → Wrapper for `/posts` API actions  

---

### **2. config/**
Configuration files:

- `config.json` → Base URLs & environment variables  
- `config_manager.py` → Loads config values  

---

### **3. data/**
Data for **API data-driven testing**:

- `post_data.csv`  
- `post_data.json`  

---

### **4. reports/**
Auto-generated during execution:

- HTML reports  
- Failure screenshots (Playwright)

---

### **5. schemas/**
JSON schema files for response validation:

- `post_schemas.json`

---

### **6. tests/**
API tests:

- `test_posts_api.py` → GET, POST, schema validation, DDT

---

### **7. utils/**
Helper utilities:

- `data_loader.py`  
- `logger.py`  
- `schema_validator.py`  

---

### **8. web/**
Playwright Web Automation

#### **web/data/**
- Test data for web DDT  
  - `search_data.json`

#### **web/pages/**
Page Object Model:

- `base_page.py` → Common browser actions  
- `amazon_home_page.py` → Search page  
- `amazon_results_page.py` → Scroll, extract results, extract prices  

#### **web/tests/**
UI tests:

- `test_amazon_search.py`  
- `test_amazon_search_data_driven.py`  
- `test_amazon_price_check.py`

---

# ▶ How to Run Tests

### **1. Run API Tests**
```
py -m pytest tests/test_posts_api.py -v
```

### **2. Run Amazon Search Test**
```
py -m pytest web/tests/test_amazon_search.py -v
```

### **3. Run Data-driven Web Search Test**
```
py -m pytest web/tests/test_amazon_search_data_driven.py -v
```

### **4. Run Price Check Test**
```
py -m pytest web/tests/test_amazon_price_check.py -v
```

### **5. Run Entire Framework**
```
py -m pytest -v
```

---




