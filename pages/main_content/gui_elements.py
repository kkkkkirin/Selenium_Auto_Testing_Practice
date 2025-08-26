import allure

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from enums.enums_messages import EnumMessages as EM
from selenium.webdriver.support.ui import Select

class GuiElemPage(BasePage):
    # Locators for forms
    NAME_FIELD = ("xpath", "//input[@id='name']")
    EMAIL_FIELD = ("xpath", "//input[@id='email']")
    PHONE_FIELD = ("xpath", "//input[@id='phone']")
    ADDRESS_FIELD = ("xpath", "//textarea[@id='textarea']")

    # Locators for dropdown selectors
    SELECT_COUNTRY_SELECTOR = ("xpath", "//select[@id='country']")
    SELECT_COLOR_SELECTOR = ("xpath", "//select[@id='colors']")
    SELECT_ANIMAL_SELECTOR = ("xpath", "//select[@id='animals']")

    # Functions to fill the fields in forms

    def enter_value(self, locator: tuple[str, str], value:str) -> None:
        with allure.step(f"Enter the {value}"):
            self.wait.until(EC.element_to_be_clickable(locator), EM.NO_CLICKABLE).send_keys(value)
        with allure.step("Сhecking that the required value has been entered"):
            self.wait.until(EC.text_to_be_present_in_element_value(locator, value), EM.DIFF_VALUES)

    def enter_name(self, name:str) -> None:
        self.enter_value(self.NAME_FIELD, name)

    def enter_email(self, email:str) -> None:
        self.enter_value(self.EMAIL_FIELD, email)

    def enter_phone(self, phone:str) -> None:
        self.enter_value(self.PHONE_FIELD, phone)

    def enter_address(self, address:str) -> None:
        self.enter_value(self.ADDRESS_FIELD, address)

    # Functions to work with dropdowns

    def choose_gender(self, gender:str) -> None:
        gender_selector = ("xpath", f"//input[@id='{gender.lower()}']")
        self.wait.until(EC.element_to_be_clickable(gender_selector), EM.NO_CLICKABLE).click()

    def choose_days(self, days:list[str]) -> None:
        for day in days:
            if EC.visibility_of_element_located(("xpath", f"//label[@for='{day.lower()}']")):
                self.wait.until(EC.element_to_be_clickable(("xpath", f"//input[@id='{day.lower()}']")),
                                EM.NO_CLICKABLE).click()


    def choose_from_dropdown(self, locator:tuple[str, str], value:str) -> None:
        with allure.step("Choose dropdown element"):
            drop_down = Select(self.driver.find_element(*locator))
            drop_down.select_by_value(value)

        with allure.step(f"Check if dropdown select expected value: {value}"):
            self.wait.until(EC.text_to_be_present_in_element_value(locator, value),EM.DIFF_VALUES)

    def choose_country(self, country:str) -> None:
        self.choose_from_dropdown(self.SELECT_COUNTRY_SELECTOR, country.lower())

    def choose_color(self, color:str) -> None:
        self.choose_from_dropdown(self.SELECT_COLOR_SELECTOR, color.lower())

    def choose_animal(self, animal:str) -> None:
        self.choose_from_dropdown(self.SELECT_ANIMAL_SELECTOR, animal.lower())