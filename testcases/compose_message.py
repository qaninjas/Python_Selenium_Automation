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

class sendMessage(DriverManager):
    def test_sending_message(self, title='Hello', recipent='john wick', text='How are you?'):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.service = Services(self.driver)
        self.navigate = NavigationPanelPage(self.driver)
        self.mssg = message_tab(self.driver)
        self.service.wait_for_element(self.navigate.messages_btn)
        self.service.click_element(self.navigate.messages_btn)

        self.service.wait_for_element(self.mssg.compose_btn)
        self.service.click_element(self.mssg.compose_btn)

        # static wait added
        time.sleep(1)

        self.service.wait_for_element(self.mssg.send_msg)
        self.service.find_element(self.mssg.title).send_keys(title)
        
        send_to = self.service.find_element(self.mssg.recipents)
        send_to.click()
        send_to.send_keys(recipent)
        send_to.send_keys(Keys.RETURN)
        self.service.find_element(self.mssg.body).send_keys(text)

        self.service.find_element(self.mssg.send_msg).click()

        logging.info("## sending message... ##")

        if self.service.is_element_present(self.mssg.send_msg) == False:
            logging.info("## message sent. ##")

        else:
            logging.info("## message not sent. ##")