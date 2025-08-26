from enums.enums_messages import EnumMessages as EM
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DoubleClickCopy(BasePage):
    COPY_TEXT_BUTTON = ("xpath", "//button[@ondblclick]")
    COPY_TEXTBOX_SOURCE = ("xpath", "//input[@id='field1']")
    COPY_TEXTBOX_RESULT = ("xpath", "//input[@id='field2']")

    def double_click_copy(self) -> None:
        copy_button = self.wait.until(EC.element_to_be_clickable(self.COPY_TEXT_BUTTON), EM.NO_CLICKABLE)
        self.action.double_click(copy_button).perform()

        # Checking that value has been copied
        compare_text = self.driver.find_element(*self.COPY_TEXTBOX_SOURCE).get_attribute("value")
        self.wait.until(EC.text_to_be_present_in_element_value(self.COPY_TEXTBOX_RESULT, compare_text), EM.DIFF_VALUES)