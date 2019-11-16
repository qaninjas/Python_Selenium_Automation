from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services
from selenium.webdriver.common.keys import Keys
from pages.navigation_panel_page import NavigationPanelPage
from pages.messages_page import message_tab
import time
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


@attr(website=['party'])

class startConversation(DriverManager):
    def test_conversation(self, Message='Hello, how are you?'):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.service = Services(self.driver)
        self.navigate = NavigationPanelPage(self.driver)
        self.mssg = message_tab(self.driver)
        self.service.wait_for_element(self.navigate.messages_btn)
        self.service.click_element(self.navigate.messages_btn)

        self.service.wait_for_element(self.mssg.send_btn)
        self.service.find_element(self.mssg.text).send_keys(Message)
        
        self.service.find_element(self.mssg.emoji_btn).click()
        self.service.find_element(self.mssg.emoji1).click()
        self.service.find_element(self.mssg.emoji_btn).click()

        self.service.find_element(self.mssg.send_btn).click()
        self.service.find_element(self.mssg.attatchment).click()