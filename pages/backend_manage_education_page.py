import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class BackendManageEducation:
    def __init__(self,driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.url = "https://www.atg.party/admin/education/list"
        self.manage_page_header = "xpath=//*[text()='Manage Education']"
        self.edit_btn = "xpath=//*[@title='Edit Article Details']"
        self.edit_page_tab_name = "Edit Education Details"
        self.view_btn = "xpath=//*[@title='View Article Details']"
        self.view_page_tab_name = "View Education Details"

    def nav_to_education_list(self):
        self.driver.get(self.url)
        logging.info("## waiting for Manage Education to load ##")
        self.service.wait_for_element(self.manage_page_header)
    def click_edit(self):
        first_post_edit_btn = self.service.find_element(self.edit_btn)
        first_post_edit_btn.click()

    def validate_user_on_edit_education_page(self):
        logging.info("## checking if user on edit Education page ##")
        tab_name = self.service.get_tab_name()
        assert tab_name == self.edit_page_tab_name ,"Edit Education Page must be opened"

    def click_view(self):
        first_post_view_btn = self.service.find_element(self.view_btn)
        first_post_view_btn.click()

    def validate_user_on_view_education_page(self):
        logging.info("## checking if user on view Education page ##")
        tab_name = self.service.get_tab_name()
        assert tab_name == self.view_page_tab_name ,"View Education Page must be opened"


