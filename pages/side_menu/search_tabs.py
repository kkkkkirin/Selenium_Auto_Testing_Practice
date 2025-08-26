import pytest
import allure

from enums.enums_messages import EnumMessages as EM
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SearchTabs(BasePage):
    # Locators for search_tabs
    SEARCH_FIELD = ("xpath", "//input[@class='wikipedia-search-input']")
    SEARCH_BUTTON = ("xpath", "//input[@class='wikipedia-search-button']")
    RESULT_SEARCH = ("xpath", "(//div[@id='wikipedia-search-result-link'][1]/a)")

    def search_tabs(self, search_input):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD), EM.NO_CLICKABLE).send_keys(search_input)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON), EM.NO_CLICKABLE).click()

        if self.driver.find_element("xpath", "//div[@class='wikipedia-search-results']").text != EM.NO_RESULTS:
            self.wait.until(EC.element_to_be_clickable(self.RESULT_SEARCH), EM.NO_CLICKABLE).click()

            tabs = self.driver.window_handles
            self.driver.switch_to.window(tabs[1])

            with allure.step("Checking that opened expected tab"):
                # Checking that opened expected tab
                self.wait.until(lambda driver: search_input.lower() in self.driver.title.lower(), EM.DIFF_VALUES)