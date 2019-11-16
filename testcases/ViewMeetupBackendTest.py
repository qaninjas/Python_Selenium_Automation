from nose.plugins.attrib import attr
from pages.backend_login_page import BackendLoginPage
from utility.drivermanager import DriverManager
from pages.backend_manage_meetup_page import BackendManageMeetup

@attr(website=['party', 'world'])
class VerifyViewinMeetup(DriverManager):
    def backend_login(self):
        backend_login_page = BackendLoginPage(self.driver)
        backend_login_page.nav_to_login_page()
        backend_login_page.wait_for_loginpage_to_load()
        backend_login_page.login()
    def test_view_meetup(self):
        self.backend_login()
        manage_meetup_page = BackendManageMeetup(self.driver)
        manage_meetup_page.nav_to_meetup_list()
        manage_meetup_page.click_view()
        self.driver.implicitly_wait(1)
        manage_meetup_page.validate_user_on_view_meetup_page()
