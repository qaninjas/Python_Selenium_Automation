# Scenario: This testcase validates share with Twitter

from nose.plugins.attrib import attr
import logging
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from pages.home_page import HomePage
from utility.services import Services
from pages.Share_post_pages import ShareWith

@attr(website=['party', 'world'])
class VerifyShareWithTwitter(DriverManager):
    def test_share_with_twitter(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.dashboard = HomePage(self.driver)
        self.service=Services(self.driver)
        self.service.wait_for_element(self.dashboard.posts,50)
        share = ShareWith(self.driver)

        logging.info("## verifying share with Twitter")
        self.dashboard.share_with_twitter()
        share.validate_user_on_twitter_share_post_page()
