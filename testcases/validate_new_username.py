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

class NewUsername(DriverManager):   
    def test_adding_new_username(self, user='bygbyrd'):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.service = Services(self.driver)
        self.navigate = NavigationPanelPage(self.driver)
        self.invite_btn = invite(self.driver)
        self.service.wait_for_element(self.navigate.invite_friends_btn)
        self.service.click_element(self.navigate.invite_friends_btn)

        check = self.service.is_element_present(self.invite_btn.save_btn)

        if check==True:
            self.service.wait_for_element(self.invite_btn.save_btn)
            self.service.find_element(self.invite_btn.new_username_input).send_keys(user)
            
            val = self.service.is_element_present(self.invite_btn.condition)

            if val==True:
                e = self.service.find_element(self.invite_btn.condition)
                error = e.text
                if e.text=="":
                    error = None
                logging.info("## Fault in username: <"+ str(error) +"> ##")

                if error == None:
                    self.service.find_element(self.invite_btn.save_btn).click()
