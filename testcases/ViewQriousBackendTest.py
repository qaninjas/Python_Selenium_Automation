from nose.plugins.attrib import attr
from pages.backend_login_page import BackendLoginPage
from utility.drivermanager import DriverManager
from pages.backend_manage_qrious_page import BackendManageQrious

@attr(website=['party', 'world'])
class VerifyViewinQrious(DriverManager):
    def backend_login(self):
        backend_login_page = BackendLoginPage(self.driver)
        backend_login_page.nav_to_login_page()
        backend_login_page.wait_for_loginpage_to_load()
        backend_login_page.login()
    def test_view_qrious(self):
        self.backend_login()
        manage_qrious_page = BackendManageQrious(self.driver)
        manage_qrious_page.nav_to_qrious_list()
        manage_qrious_page.click_view()
        self.driver.implicitly_wait(1)
        manage_qrious_page.validate_user_on_view_qrious_page()