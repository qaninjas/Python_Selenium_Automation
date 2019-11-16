import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class BackendManageArticle:
    def __init__(self,driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.url = "https://www.atg.party/admin/article/article-list"
        self.manage_page_header = "xpath=//*[text()='Manage Articles']"
        self.edit_btn = "xpath=//*[@title='Edit Article Details']"
        self.edit_page_tab_name = "Edit Article Details"
        self.view_btn = "xpath=//*[@title='View Article Details']"
        self.view_page_tab_name = "View Article Details"

    def nav_to_article_list(self):
        self.driver.get(self.url)
        logging.info("## waiting for Manage Article to load ##")
        self.service.wait_for_element(self.manage_page_header)
    def click_edit(self):
        first_post_edit_btn = self.service.find_element(self.edit_btn)
        first_post_edit_btn.click()

    def validate_user_on_edit_article_page(self):
        logging.info("## checking if user on edit article page ##")
        tab_name = self.service.get_tab_name()
        assert tab_name == self.edit_page_tab_name,"Edit Article Page must be opened"

    def click_view(self):
        first_post_view_btn = self.service.find_element(self.view_btn)
        first_post_view_btn.click()

    def validate_user_on_view_article_page(self):
        logging.info("## checking if user on view article page ##")
        tab_name = self.service.get_tab_name()
        assert tab_name == self.view_page_tab_name ,"View Article Page must be opened"


