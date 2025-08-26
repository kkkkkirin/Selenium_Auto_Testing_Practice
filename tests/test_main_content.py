import pytest
import allure
import json

from pages.main_content.gui_elements import GuiElemPage
from pages.main_content.upload_files import UploadFiles
from pages.main_content.date_pickers import DatePickers

def load_test_data(category):
    with open(f'src/test_data/{category}_data.json', 'r') as file:
        data = json.load(file)
        return data[category]

@allure.feature("Test GUI Elements on main content")
@pytest.mark.main_content
class TestGuiElements:
    def setup_method(self):
        self.gui_page = GuiElemPage(self.driver)
        self.gui_page.open()

    @pytest.mark.parametrize("user_data", load_test_data("users"))
    def test_fill_the_form(self, user_data):
        self.gui_page.enter_name(user_data["name"])
        self.gui_page.enter_email(user_data["email"])
        self.gui_page.enter_phone(user_data["phone"])
        self.gui_page.enter_address(user_data["address"])
        self.gui_page.choose_gender(user_data["gender"])
        self.gui_page.choose_days(user_data["days"])

    @pytest.mark.parametrize("dropdown_data", load_test_data("dropdown"))
    def test_dropdowns(self,dropdown_data):
        self.gui_page.choose_country(dropdown_data["country"])
        self.gui_page.choose_color(dropdown_data["color"])
        self.gui_page.choose_animal(dropdown_data["animal"])

@allure.feature("Test date pickers")
@pytest.mark.main_content
class TestDatePickers:
    def setup_method(self):
        self.date_pickers = DatePickers(self.driver)
        self.date_pickers.open()

    @pytest.mark.parametrize("date_data", load_test_data("date"))
    def test_date_pickers(self, date_data):
        self.date_pickers.choose_date_picker_one(date_data["day"], date_data["month"], date_data["year"])
        self.date_pickers.choose_date_picker_two(date_data["day"], date_data["month"], date_data["year"])

@allure.feature("Test upload files")
@pytest.mark.main_content
class TestUploadFiles:
    def setup_method(self):
        self.load_files = UploadFiles(self.driver)
        self.load_files.open()

    def test_upload_file(self):
        self.load_files.upload_file("text_info.txt")

    def test_upload_files(self):
        self.load_files.upload_files(["text_info.txt", "json_info.json"])