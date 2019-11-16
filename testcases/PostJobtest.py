from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.navigation_panel_page import NavigationPanelPage
from pages.job_post_page import JobPostPage
from pages.Settings.profile_settings_page import ProfileSettings
from selenium.webdriver.common.keys import Keys
from pages.home_page import HomePage
import datetime
import time
# PO_003

@attr(website=['world'])
class JobPostTest(DriverManager):
    def login(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()

    def test_job_post(self):
        self.navigate = NavigationPanelPage(self.driver)
        self.profile = ProfileSettings(self.driver)
        self.service = Services(self.driver)
        self.job = JobPostPage(self.driver)
        self.home = HomePage(self.driver)
        self.hire = "Lawyer"
        self.text = "post job test"
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

