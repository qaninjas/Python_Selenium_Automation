from nose.plugins.attrib import attr
from pages.backend_login_page import BackendLoginPage
from utility.drivermanager import DriverManager
from pages.backend_manage_education_page import BackendManageEducation

@attr(website=['party', 'world'])
class VerifyEditinEducation(DriverManager):
    def backend_login(self):
        backend_login_page = BackendLoginPage(self.driver)
        backend_login_page.nav_to_login_page()
        backend_login_page.wait_for_loginpage_to_load()
        backend_login_page.login()
    def test_Edit_education(self):
        self.backend_login()
        manage_education_page = BackendManageEducation(self.driver)
        manage_education_page.nav_to_education_list()
        manage_education_page.click_edit()
        self.driver.implicitly_wait(1)
        manage_education_page.validate_user_on_edit_education_page()