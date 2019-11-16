from nose.plugins.attrib import attr
from pages.backend_login_page import BackendLoginPage
from utility.drivermanager import DriverManager
from pages.backend_manage_users_page import BackendManageUser

@attr(website=['party', 'world'])
class VerifyEditInUser(DriverManager):
    def backend_login(self):
        backend_login_page = BackendLoginPage(self.driver)
        backend_login_page.nav_to_login_page()
        backend_login_page.wait_for_loginpage_to_load()
        backend_login_page.login()
    def test_Edit_user(self):
        self.backend_login()
        manage_user_page = BackendManageUser(self.driver)
        manage_user_page.nav_to_user_list()
        manage_user_page.click_edit()
        self.driver.implicitly_wait(1)
        manage_user_page.validate_user_on_edit_user_page()