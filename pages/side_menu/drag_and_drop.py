from enums.enums_messages import EnumMessages as EM
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DragAndDrop(BasePage):
    DRAG_ELEMENT = ("xpath", "//div[@id='draggable']")
    DROP_AREA = ("xpath", "//div[@id='droppable']")

    def drag_and_drop(self) -> None:
        drag = self.driver.find_element(*self.DRAG_ELEMENT)
        drop = self.driver.find_element(*self.DROP_AREA)

        self.action.drag_and_drop(drag, drop).perform()

        # Checking that drag object in drop area
        text_drop_area_locator = ("xpath", "//div[@id='droppable']/p")
        self.wait.until(EC.text_to_be_present_in_element(text_drop_area_locator, "Dropped!"), EM.DIFF_VALUES)
