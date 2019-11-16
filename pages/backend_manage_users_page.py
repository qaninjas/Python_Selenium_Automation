import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class BackendManageUser:
    def __init__(self,driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.url = "https://www.atg.party/admin/users/list/all"
        self.manage_page_header = "xpath=//*[text()='Manage All Users']"
        self.edit_btn = "xpath=//*[@title='Edit User Details']"
        self.edit_page_tab_name = "Update User"
        self.view_btn = "xpath=//*[@title='View User Details']" 
        self.view_page_tab_name = "View User"
        self.email_verificaion = "xpath=//*[text()='Not verified']"

    def nav_to_user_list(self):
        self.driver.get(self.url)
        logging.info("## waiting for Manage User to load ##")
        self.service.wait_for_element(self.manage_page_header)
    def click_edit(self):
        first_post_edit_btn = self.service.find_element(self.edit_btn)
        first_post_edit_btn.click()

    def validate_user_on_edit_user_page(self):
        logging.info("## checking if user on edit user page ##")
        tab_name = self.service.get_tab_name()
        assert tab_name == self.edit_page_tab_name,"Edit User Page must be opened"

    def click_view(self):
        first_post_view_btn = self.service.find_element(self.view_btn)
        first_post_view_btn.click()

    def validate_user_on_view_user_page(self):
        logging.info("## checking if user on view user page ##")
        tab_name = self.service.get_tab_name()
        assert tab_name == self.view_page_tab_name ,"View User Page must be opened"

    def verify_first_not_verified_email(self):
        logging.info("## getting all the not verified users... ##")
        email = self.service.find_elements(self.email_verificaion)
        #print(len(email))
        return email

        