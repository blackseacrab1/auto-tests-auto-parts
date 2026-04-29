import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # Можно добавить аргументы, если нужно, например:
    # options.add_argument("--headless=new") 
    
    # Selenium Manager сам найдет и запустит ChromeDriver
    driver = webdriver.Chrome(options=options)
    
    driver.maximize_window()
    yield driver
    driver.quit()