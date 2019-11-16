# Scenario : Upload a All fields of profile settings and validates updated fields
# validation is pending
import random
import string
import time

from nose.plugins.attrib import attr

from pages.ATG_register_page import ATGRegister
from pages.home_page import HomePage
from utility.services import Services

from utility.drivermanager import DriverManager
from pages.ATG_login_page import ATGLoginPage
from pages.navigation_panel_page import NavigationPanelPage
from pages.article_page import ArticlePage

ARTICLE_TITLE_CONST = "Test Article: "
ARTICLE_DESC_CONST = "Test Description: "
ascii_lowercase_letters = string.ascii_lowercase[:12]


@attr(website=['party', 'world'])
class WriteArticleTest(DriverManager):
    def test_update_all_fields_of_profile_settings(self):
        # register_page = ATGRegister(self.driver)
        # register_page.register_user()
        # register_page.select_group_in_registration_flow()
        # register_page.select_profession('Student')
        # register_page.validate_registered_user_on_loggedin_page()
        atg_login_page = ATGLoginPage(self.driver)
        self.service = Services(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        #         Navigate to profile setting screen
        navigation_panel_page = NavigationPanelPage(self.driver)
        article_page = ArticlePage(self.driver)
        self.service.find_element(navigation_panel_page.write_post_btn).click()
        self.service.find_element(navigation_panel_page.article_lnk).click()
        self.service.assert_element_present(article_page.title_of_article_txtfield)

        #         write an article
        self.service.find_element(article_page.title_of_article_txtfield).send_keys(self.get_random_title_of_article())
        self.service.find_element(article_page.article_textarea).send_keys(self.get_random_content_of_Article())
        self.service.find_element(article_page.save_And_close_btn)
        time.sleep(10)

    @staticmethod
    def get_random_title_of_article():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(7))
        return ARTICLE_TITLE_CONST + random_string

    @staticmethod
    def get_random_content_of_Article():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(12))
        return ARTICLE_DESC_CONST + random_string

