import os
import allure
from enums.enums_messages import EnumMessages as EM
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class UploadFiles(BasePage):

    PAGE_URL = "https://testautomationpractice.blogspot.com/"

    # Locators for upload file
    SINGLE_FILE_INPUT_LOCATOR = ("xpath", "//form[@id='singleFileForm']/input")
    SINGLE_FILE_BUTTON_LOCATOR = ("xpath", "//form[@id='singleFileForm']/button")
    SINGLE_FILE_RESULT_LOCATOR = ("xpath", "//p[@id='singleFileStatus']")

    # Locators for upload files
    MULTI_FILES_INPUT_LOCATOR = ("xpath", "//form[@id='multipleFilesForm']/input")
    MULTI_FILES_BUTTON_LOCATOR = ("xpath", "//form[@id='multipleFilesForm']/button")
    MULTI_FILE_RESULT_LOCATOR = ("xpath", "//p[@id='multipleFilesStatus']")

    def upload_file(self, filename:str) -> None:
        with allure.step("Upload file"):
            path = f"{os.getcwd()}/src/upload_folder/{filename}"
            self.wait.until(EC.visibility_of_element_located(self.SINGLE_FILE_INPUT_LOCATOR), EM.NO_VISIBLE).send_keys(path)
            self.wait.until(EC.element_to_be_clickable(self.SINGLE_FILE_BUTTON_LOCATOR), EM.NO_CLICKABLE).click()

        with allure.step("Checking file uploads"):
            result_value = self.driver.find_element(*self.SINGLE_FILE_RESULT_LOCATOR).text
            self.wait.until(lambda driver: filename in result_value, EM.FILE_NOT_UPLOAD)


    def upload_files(self, files:list[str]) -> None:
        with allure.step("Upload files"):
            for file in files:
                path = f"{os.getcwd()}/src/upload_folder/{file}"
                self.wait.until(EC.visibility_of_element_located(self.MULTI_FILES_INPUT_LOCATOR), EM.NO_VISIBLE).send_keys(path)
            self.wait.until(EC.element_to_be_clickable(self.MULTI_FILES_BUTTON_LOCATOR), EM.NO_CLICKABLE).click()

        with allure.step("Checking files uploads"):
            result_value = self.driver.find_element(*self.MULTI_FILE_RESULT_LOCATOR).text
            self.wait.until(lambda driver: all(file in result_value for file in files), EM.FILE_NOT_UPLOAD)