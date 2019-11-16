from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.navigation_panel_page import NavigationPanelPage
from pages.invite_page import invite
import time
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

@attr(website=['party'])

class InviteFromFacebook(DriverManager):
    def test_invite_from_facebook(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.service = Services(self.driver)
        self.navigate = NavigationPanelPage(self.driver)
        self.invite_btn = invite(self.driver)
        self.service.wait_for_element(self.navigate.invite_friends_btn)
        self.service.click_element(self.navigate.invite_friends_btn)

        self.service.wait_for_element(self.invite_btn.facebook_btn)
        self.service.click_element(self.invite_btn.facebook_btn)
        self.service.wait(2)
        self.service.switch_tab(1)