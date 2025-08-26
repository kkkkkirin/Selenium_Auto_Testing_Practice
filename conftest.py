import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")

    chrome_driver = webdriver.Chrome(options=options)

    request.cls.driver = chrome_driver
    yield
    chrome_driver.quit()