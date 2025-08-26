from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, 1)
        self.action = ActionChains(self.driver)


    def open(self):
        self.PAGE_URL = "https://testautomationpractice.blogspot.com/"
        self.driver.get(self.PAGE_URL)