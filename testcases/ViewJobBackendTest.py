from nose.plugins.attrib import attr
from pages.backend_login_page import BackendLoginPage
from utility.drivermanager import DriverManager
from pages.backend_manage_jobs_page import BackendManageJob

@attr(website=['party', 'world'])
class VerifyViewinJob(DriverManager):
    def backend_login(self):
        backend_login_page = BackendLoginPage(self.driver)
        backend_login_page.nav_to_login_page()
        backend_login_page.wait_for_loginpage_to_load()
        backend_login_page.login()
    def test_view_job(self):
        self.backend_login()
        manage_job_page = BackendManageJob(self.driver)
        manage_job_page.nav_to_job_list()
        manage_job_page.click_view()
        self.driver.implicitly_wait(1)
        manage_job_page.validate_user_on_view_job_page()


