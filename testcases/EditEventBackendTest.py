from nose.plugins.attrib import attr
from pages.backend_login_page import BackendLoginPage
from utility.drivermanager import DriverManager
from pages.backend_manage_events_page import BackendManageEvent

@attr(website=['party', 'world'])
class VerifyEditinEvent(DriverManager):
    def backend_login(self):
        backend_login_page = BackendLoginPage(self.driver)
        backend_login_page.nav_to_login_page()
        backend_login_page.wait_for_loginpage_to_load()
        backend_login_page.login()
    def test_Edit_event(self):
        self.backend_login()
        manage_event_page = BackendManageEvent(self.driver)
        manage_event_page.nav_to_event_list()
        manage_event_page.click_edit()
        self.driver.implicitly_wait(1)
        manage_event_page.validate_user_on_edit_event_page()