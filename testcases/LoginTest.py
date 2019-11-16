from nose.plugins.attrib import attr

from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager


@attr(website=['party', 'world'])
class ATGLoginTest(DriverManager):
    def test_login_with_valid_credentails(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
