import time
from nose.plugins.attrib import attr
from pages.backend_login_page import BackendLoginPage
from utility.drivermanager import DriverManager
from pages.backend_manage_users_page import BackendManageUser

@attr(website=['party', 'world'])
class VerifyEmail(DriverManager):
    def test_verify_email(self):
        backend_login_page = BackendLoginPage(self.driver)
        backend_login_page.nav_to_login_page()
        backend_login_page.wait_for_loginpage_to_load()
        backend_login_page.login()

    	link = BackendManageUser(self.driver)
        link.nav_to_user_list()
        email = link.verify_first_not_verified_email() 
        i=0
        for i in range(len(email)):
            try:
                email[i].click()
                check=1
            except:
                continue