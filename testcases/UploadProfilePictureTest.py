# Scenario : Upload a profile picture for a newly signed up user
from nose.plugins.attrib import attr

from pages.ATG_register_page import ATGRegister
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from utility.drivermanager import DriverManager
import os


@attr(website=['party', 'world'])
class UploadProfilePictureForNewUser(DriverManager):
    def test_upload_profile_picture(self):
        register_page = ATGRegister(self.driver)
        register_page.register_user()
        register_page.select_group_in_registration_flow()
        register_page.select_profession('Student')
        register_page.validate_registered_user_on_loggedin_page()

        HomePage(self.driver).navigate_to_main_profile()
        profile_page = ProfilePage(self.driver)
        profile_page.tap_on_file_upload()
        profile_page.upload_profile_image(os.environ['profile_pic_path'])
        before_url, after_url = profile_page.validate_uploaded_profile_pic()
        self.assertTrue(before_url != after_url,
                        'User Profile picture is updated successfully !!!')
