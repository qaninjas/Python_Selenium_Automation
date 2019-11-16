from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.navigation_panel_page import NavigationPanelPage
from pages.job_post_page import JobPostPage
from pages.Settings.profile_settings_page import ProfileSettings
from pages.job_apply_page import JobApplyPage
from selenium.webdriver.common.keys import Keys
from pages.home_page import HomePage
from pages.Settings.settings import Settings
from pages.post_detail_page import PostDetailPage
from pages.Settings.my_applied_jobs import AppliedJob
import datetime
import time
# PO_005

@attr(website=['world'])
class JobApplyTest(DriverManager):
    def post_job(self):
        self.navigate = NavigationPanelPage(self.driver)
        self.profile = ProfileSettings(self.driver)
        self.service = Services(self.driver)
        self.job = JobPostPage(self.driver)
        self.home = HomePage(self.driver)
        self.apply = JobApplyPage(self.driver)
        self.post = PostDetailPage(self.driver)
        self.settings = Settings(self.driver)
        self.job_table = AppliedJob(self.driver)
        self.hire = "Lawyer"
        self.text = "Apply job test"
        self.location = 'Bangalore, Karnataka, India'
        # get tomorrow's date
        tomorrow = datetime.datetime.today() + datetime.timedelta(1)
        self.date = datetime.datetime.strftime(tomorrow, '%d ' '%B ' '%Y')
        self.login()

        # fill job form
        self.service.wait_for_element(self.navigate.writepost_submenu, 50)
        self.service.click_element(self.navigate.write_post_btn)
        self.service.click_element(self.navigate.job_lnk)
        self.service.wait_for_element(self.job.hire, 20)
        self.service.find_element(self.job.hire).send_keys(self.hire)
        self.service.wait_for_element_visible(self.job.lawyer)
        self.service.click_element(self.job.lawyer)
        self.service.wait_for_element_visible(self.job.job_title, 20)
        self.service.find_element(self.job.job_title).send_keys(self.text + Keys.ENTER)
        self.service.wait_for_element_visible(self.job.description, 20)
        self.service.click_element(self.job.description)
        self.service.find_element(self.job.description).send_keys(self.text + Keys.TAB)
        self.service.wait_for_element_visible(self.job.location, 20)
        self.service.click_element(self.job.location)
        self.service.find_element(self.job.location).send_keys(self.location)
        # sleep required for google locations to load
        time.sleep(1)
        self.service.find_element(self.job.location).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        self.service.wait_for_element_visible(self.job.company_name, 20)
        self.service.find_element(self.job.company_name).send_keys(self.text + Keys.ENTER)
        self.service.find_element(self.job.company_site).send_keys(self.text + Keys.ENTER)
        self.service.find_element(self.job.edu_skill).send_keys(self.text + Keys.ENTER)
        self.service.find_element(self.job.ext_link).send_keys(self.text + Keys.ENTER)
        self.service.find_element(self.job.app_deadline).send_keys(self.date + Keys.ENTER)
        self.service.click_element(self.job.min_experience)
        self.service.click_element(self.job.min_experience_option)
        self.service.click_element(self.job.employment_type)
        self.service.click_element(self.job.type)
        self.service.find_element(self.job.hire).clear()
        self.service.find_element(self.job.hire).send_keys(self.hire)
        self.service.wait_for_element_visible(self.job.lawyer)
        self.service.click_element(self.job.lawyer)
        self.service.click_element(self.job.post_btn)

        # check if location is the same in settings
        self.service.click_element(self.navigate.setting_btn)
        self.service.find_element(self.profile.location_txtfield).clear()
        self.service.find_element(self.profile.location_txtfield).send_keys(self.location)
        # sleep required for google locations to load
        time.sleep(1)
        self.service.find_element(self.profile.location_txtfield).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        self.service.click_element(self.profile.save_btn)

        # check if job appears in dashboard
        self.service.click_element(self.navigate.home_btn)
        self.service.wait_for_element_visible(self.home.posts, 50)
        self.service.assert_text_present(self.text, self.home.posts)

        self.post.navigate_to_post_detail_page()
        self.job_url = self.service.get_url()
        self.service.click_element(self.navigate.setting_btn)
        self.service.click_element(self.settings.logout_btn)

    def login(self, username='hello@atg.world', password='Pass@123'):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login(username, password)
        atg_login_page.validate_user_on_homepage()

    def test_job_application(self):
        # create a job
        self.post_job()

        # login with another account to apply to created job
        self.login('test@atg.world', 'Pass@123')

        # check if location is the same for both job and applicant in settings
        self.service.click_element(self.navigate.setting_btn)
        self.service.find_element(self.profile.location_txtfield).clear()
        self.service.find_element(self.profile.location_txtfield).send_keys(self.location)
        # sleep required for google locations to load
        time.sleep(1)
        self.service.find_element(self.profile.location_txtfield).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        self.service.click_element(self.profile.save_btn)

        # upload resume
        self.service.get_website(self.job_url)
        self.service.click_element(self.apply.apply_btn)
        self.service.find_element(self.apply.phone_no).send_keys('0000000000')
        self.service.find_element(self.apply.why_hire).send_keys('test')
        self.service.click_element(self.apply.resume_btn)
        self.service.click_element(self.apply.apply)
        # sleep required for POST request to be accepted
        time.sleep(1)
        self.service.wait_for_element(self.navigate.setting_btn, 50)
        self.service.click_element(self.navigate.setting_btn)
        self.service.click_element(self.settings.my_applied_jobs_btn)
        self.service.wait_for_element(self.job_table.job_table)
        self.service.assert_text_present(self.text, self.job_table.job_table)

