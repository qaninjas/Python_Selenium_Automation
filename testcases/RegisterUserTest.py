from nose.plugins.attrib import attr

from pages.ATG_register_page import ATGRegister
from utility.drivermanager import DriverManager


@attr(website=['party', 'world'])
class ATGRegistration(DriverManager):
    def test_register_with_random_userdata(self):
        register_page = ATGRegister(self.driver)
        register_page.register_user()
        register_page.select_group_in_registration_flow()
        register_page.select_profession('Student')
        register_page.validate_registered_user_on_loggedin_page()
