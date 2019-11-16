# upload pdf/doc resume file and validate updated resume after applying to save changes
# Scenario : Upload a profile picture for a newly signed up user
from nose.plugins.attrib import attr

from pages.ATG_register_page import ATGRegister
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.Settings.manage_resume import ManageResume
from pages.Settings.settings import Settings
import os


@attr(website=['party', 'world'])
class UploadProfilePictureForNewUser(DriverManager):
    def test_upload_resume_and_validate_uploaded_resume(self):
        register_page = ATGRegister(self.driver)
        register_page.register_user()
        register_page.select_group_in_registration_flow()
        register_page.select_profession('Student')
        register_page.validate_registered_user_on_loggedin_page()

        setting_panel = Settings(self.driver)
        self.service = Services(self.driver)
        manage_resume_page = ManageResume(self.driver)
        self.service.find_element(setting_panel.setting_lbl).click()
        self.service.find_element(setting_panel.manage_resume_btn).click()
        self.service.assert_element_present(manage_resume_page.upload_resume_lbl)
        self.service.find_element(manage_resume_page.choose_fle_btn).send_keys(os.environ['resume_path'])
        self.service.find_element(manage_resume_page.upload_resumes_btn).click()
        self.service.wait_for_element(manage_resume_page.uploaded_resume_section)

        self.assertTrue(self.service.is_element_present(manage_resume_page.uploaded_resume_section),
                        'Resume is uploaded successfully')
