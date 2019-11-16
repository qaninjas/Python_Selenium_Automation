from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.navigation_panel_page import NavigationPanelPage
from pages.help_page import HelpPage
# TC_0031

@attr(website=['world'])
class HelpPrivacyTermsTest(DriverManager):
    def login(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.navigate = NavigationPanelPage(self.driver)
        self.service = Services(self.driver)
        self.help = HelpPage(self.driver)

    def test_help_page(self):
        self.login()
        self.service.wait_for_element(self.navigate.help)
        self.service.click_element(self.navigate.help)
        self.service.assert_text_present("Help & FAQ", self.help.header)

    def test_privacy_page(self):
        self.login()
        self.service.wait_for_element(self.navigate.privacy)
        self.service.click_element(self.navigate.privacy)
        self.service.assert_text_present("Privacy Policy", self.help.header)

    def test_terms_page(self):
        self.login()
        self.service.wait_for_element(self.navigate.terms)
        self.service.click_element(self.navigate.terms)
        self.service.assert_text_present("Terms & Services", self.help.header)


