import allure

from enums.enums_messages import EnumMessages as EM
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DatePickers(BasePage):

    # Locators for calendars
    DATE_PICKER_ONE_LOCATOR = ("xpath", "//input[@id='datepicker']")

    DATE_PICKER_TWO_LOCATOR = ("xpath", "//input[@id='txtDate']")
    PICKER_TWO_MONTH_LOCATOR = ("xpath", "//select[@class='ui-datepicker-month']")
    PICKER_TWO_YEAR_LOCATOR = ("xpath", "//select[@class='ui-datepicker-year']")


    def choose_date_picker_one(self, day:int, month:int, year:int) -> None:
        with allure.step("Enter the date"):
            date = f"{month}/{day}/{year}"
            self.wait.until(EC.element_to_be_clickable(self.DATE_PICKER_ONE_LOCATOR), EM.NO_CLICKABLE).send_keys(date)

        # Check if the date is entered correctly
        with allure.step("Check if the date is entered correctly"):
            self.wait.until(EC.text_to_be_present_in_element_value(self.DATE_PICKER_ONE_LOCATOR, date), EM.DIFF_VALUES)


    def choose_date_picker_two(self, day:int, month:int, year:int) -> None:
        with allure.step("Choose date"):
            self.wait.until(EC.element_to_be_clickable(self.DATE_PICKER_TWO_LOCATOR), EM.NO_CLICKABLE).click()

            drop_down_month = Select(self.driver.find_element(*self.PICKER_TWO_MONTH_LOCATOR))
            drop_down_month.select_by_value(str(month - 1))

            drop_down_year = Select(self.driver.find_element(*self.PICKER_TWO_YEAR_LOCATOR))
            drop_down_year.select_by_value(str(year))

            day_locator = ("xpath", f"//td[@data-handler='selectDay']/a[@data-date='{day}']")
            self.wait.until(EC.element_to_be_clickable(day_locator), EM.NO_CLICKABLE).click()

        # Check if the date is entered correctly
        with allure.step("Check if the date is entered correctly"):
            date = f"{day:02}/{month:02}/{year}"
            self.wait.until(EC.text_to_be_present_in_element_value(self.DATE_PICKER_TWO_LOCATOR, date), EM.DIFF_VALUES)