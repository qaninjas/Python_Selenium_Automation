# Scenario : Choose a username for a new user

import os
import random
import string

from nose.plugins.attrib import attr

from pages.ATG_login_page import ATGLoginPage
from pages.ATG_register_page import ATGRegister
from pages.Settings.profile_settings_page import ProfileSettings
from pages.Settings.settings import Settings
from utility.drivermanager import DriverManager
from utility.services import Services

ascii_lowercase_letters = string.ascii_lowercase[:12]


@attr(website=['party', 'world'])
class ChooserUserName(DriverManager):
    def test_choose_username_for_new_user(self):
        self.choose_username()
        self.set_random_username()
        self.logout()
        self.login_user(os.environ['register_email'], os.environ['register_password'])
        self.validate_choosen_username()

    def choose_username(self):
        register_page = ATGRegister(self.driver)
        register_page.register_user()
        register_page.select_group_in_registration_flow()
        register_page.select_profession('Student')
        print(os.environ['register_email'])
        print(os.environ['register_password'])

    def set_random_username(self):
        setting_panel = Settings(self.driver)
        profile_setting = ProfileSettings(self.driver)
        self.service = Services(self.driver)
        self.service.find_element(setting_panel.setting_lbl).click()
        self.service.find_element(setting_panel.profile_setting_btn).click()
        new_password_random_str = self.get_random_string()
        os.environ['random_str_username'] = new_password_random_str
        self.service.find_element(profile_setting.username_txtfield).send_keys(os.environ['random_str_username'])
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script('document.getElementById("btn_account_setting").removeAttribute("disabled")')
        self.service.find_element(profile_setting.save_btn).click()

    def logout(self):
        setting_panel = Settings(self.driver)
        self.service = Services(self.driver)
        self.service.find_element(setting_panel.setting_lbl).click()
        self.service.find_element(setting_panel.logout_btn).click()

    def login_user(self, userid, password):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login(userid, password)

    def validate_choosen_username(self):
        setting_panel = Settings(self.driver)
        profile_setting = ProfileSettings(self.driver)
        self.service = Services(self.driver)
        self.service.find_element(setting_panel.setting_lbl).click()
        self.service.find_element(setting_panel.profile_setting_btn).click()
        username = self.service.find_element(profile_setting.username_txtfield).get_attribute('value')
        self.assertTrue(username == os.environ['random_str_username'],
                        'UserName is updated successfully !!!')

    @staticmethod
    def get_random_string():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(7))
        return random_string
