# Scenario : Change Password

import os
import random
import string

from nose.plugins.attrib import attr

from pages.ATG_register_page import ATGRegister
from pages.Settings.password_setting import PasswordSetting
from pages.Settings.settings import Settings
from testcases.LoginTest import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services

ascii_lowercase_letters = string.ascii_lowercase[:12]


@attr(website=['party', 'world'])
class ChangePassword(DriverManager):
    def test_change_password(self):
        register_page = ATGRegister(self.driver)
        register_page.register_user()
        register_page.select_group_in_registration_flow()
        register_page.select_profession('Student')
        register_page.validate_registered_user_on_loggedin_page()

        setting_panel = Settings(self.driver)
        password_setting = PasswordSetting(self.driver)
        self.service = Services(self.driver)

        self.service.find_element(setting_panel.setting_lbl).click()
        self.service.find_element(setting_panel.password_setting_btn).click()
        new_password_random_str = self.get_random_string()
        os.environ['updated_password'] = new_password_random_str
        self.service.find_element(password_setting.new_pass_txtfield).send_keys(new_password_random_str)
        self.service.find_element(password_setting.cnfm_pass_txtfield).send_keys(new_password_random_str)
        self.service.find_element(password_setting.save_btn).click()

        self.logout()

        login_page = ATGLoginPage(self.driver)
        login_page.wait_for_homepage_to_load()
        login_page.login(os.environ['register_email'], os.environ['updated_password'])
        login_page.validate_user_on_homepage()

    def logout(self):
        setting_panel = Settings(self.driver)
        self.service = Services(self.driver)
        self.service.find_element(setting_panel.setting_lbl).click()
        self.service.find_element(setting_panel.logout_btn).click()

    @staticmethod
    def get_random_string():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(7))
        return random_string
