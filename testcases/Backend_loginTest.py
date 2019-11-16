from nose.plugins.attrib import attr
from pages.backend_login_page import BackendLoginPage
from utility.drivermanager import DriverManager

@attr(website=['party', 'world'])
class BackendLogin(DriverManager):
    def backend_login_test(self):
        backend_login_page = BackendLoginPage(self.driver)
        backend_login_page.nav_to_login_page()
        backend_login_page.wait_for_loginpage_to_load()
        backend_login_page.login()