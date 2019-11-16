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

class checkMessage(DriverManager):
    def test_checking_message(self, recipent='Rahul Gupta'):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.service = Services(self.driver)
        self.navigate = NavigationPanelPage(self.driver)
        self.mssg = message_tab(self.driver)
        self.service.wait_for_element(self.navigate.messages_btn)
        self.service.click_element(self.navigate.messages_btn)

        self.service.wait_for_element(self.mssg.search)
        self.service.find_element(self.mssg.search).send_keys(recipent)
        l = []
        l.append(self.service.find_all_elements(self.mssg.className))
        #print(len(l))
        #print(l)
        logging.info("## checking for recipent... ##")
        if len(l[0])>0:
            logging.info("## message found ##")

        else:
            logging.info("## message not found ##")