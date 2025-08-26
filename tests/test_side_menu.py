import pytest
import allure

from pages.side_menu.search_tabs import SearchTabs
from pages.side_menu.double_click_copy import DoubleClickCopy
from pages.side_menu.drag_and_drop import DragAndDrop

@allure.feature("Test side menu")
@pytest.mark.side_menu
class TestSideMenu:
    def setup_method(self):
        self.search_tabs = SearchTabs(self.driver)
        self.double_copy = DoubleClickCopy(self.driver)
        self.drag_drop = DragAndDrop(self.driver)

    @allure.title("Test searching tabs")
    @pytest.mark.parametrize("search", (
        "cola", "google", "selenium", "pytest"
    ))
    def test_tabs(self, search):
        self.search_tabs.open()
        self.search_tabs.search_tabs(search)

    @allure.title("Test double click on button to copy")
    def test_double_click_copy(self):
        self.double_copy.open()
        self.double_copy.double_click_copy()

    @allure.title("Test drag element in drop area")
    def test_drag_and_drop(self):
        self.drag_drop.open()
        self.drag_drop.drag_and_drop()