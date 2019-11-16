# validate user profession on profile setting page with registration flow
import time

from nose.plugins.attrib import attr
from selenium.webdriver.support.select import Select

from pages.ATG_register_page import ATGRegister
from pages.Settings.profile_settings_page import ProfileSettings
from pages.Settings.settings import Settings
from utility.services import Services
from utility.drivermanager import DriverManager
import os


@attr(website=['party', 'world'])
class ValidateErrorOnUpdateUserInfo(DriverManager):
    def test_validate_error_message_on_user_info_update(self):
        self.register_user_with_random_data()
        self.validate_profession_of_registered_user()
        self.validates_error_message_on_userinfo_change()

    def register_user_with_random_data(self):
        register_page = ATGRegister(self.driver)
        register_page.register_user()
        register_page.select_group_in_registration_flow()
        register_page.select_profession('Student')

    def validate_profession_of_registered_user(self):
        setting_panel = Settings(self.driver)
        profile_setting = ProfileSettings(self.driver)
        self.service = Services(self.driver)
        self.service.find_element(setting_panel.setting_lbl).click()
        self.service.find_element(setting_panel.profile_setting_btn).click()
        about_user = self.service.find_element(profile_setting.about_you_selected_option).text
        print(about_user)
        self.assertTrue(os.environ['profession'] == about_user,
                        'User profession is %s set as expected... ' % about_user)

    def validates_error_message_on_userinfo_change(self):
        profile_setting = ProfileSettings(self.driver)
        select = Select(self.service.find_element(profile_setting.about_you_dropdown))
        # select by visible text
        select.select_by_visible_text('Professional')
        self.service.assert_element_is_not_present(profile_setting.aboutuserfiled_update_error_message)
