import logging
import os

from data.generate_random_userinfo import GenearteRandomUserInfo
from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ATGRegister:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.signup_btn_on_overlay = "id=reg-in-tab"
        self.signup_btn = "xpath=//*[text()='Sign Up']"
        self.register_firstname_txtfield = "id=first_name"
        self.register_latname_txtfield = "id=last_name"
        self.register_emailadd_txtfield = "id=user_email"
        self.register_password_txtfield = "id=user_password"
        self.register_confirm_password_txtfield = "id=cnf_user_password"
        self.register_btn = "id=btn_register"
        self.group_selector = "xpath=//*[@title='{}']"
        self.list_of_group = "xpath=//*[@class='trending-group material-shadow-2']/span"
        self.next_btn_step2 = "id=btnStep2"
        self.profession_txt = "xpath=//li[text()='{}']"
        self.next_btn_step3 = "id=next"
        self.profile_name = "id=prof-name"

    def register_user(self):
        random_user = GenearteRandomUserInfo()
        randm_user_info = random_user.random_user_data()
        self.service.wait_for_element_visible(self.signup_btn)
        self.service.find_element(self.signup_btn).click()
        self.service.wait_for_element_visible(self.signup_btn_on_overlay)
        self.service.find_element(self.register_firstname_txtfield).send_keys(randm_user_info['firstname'])
        self.service.find_element(self.register_latname_txtfield).send_keys(randm_user_info['lastname'])
        self.service.find_element(self.register_emailadd_txtfield).send_keys(randm_user_info['email'])
        os.environ['register_email'] = randm_user_info['email']
        self.service.find_element(self.register_password_txtfield).send_keys(randm_user_info['password'])
        os.environ['register_password'] = randm_user_info['password']
        self.service.find_element(self.register_confirm_password_txtfield).send_keys(
            randm_user_info['confirmpassword'])
        self.service.find_element(self.register_btn).click()

    def select_group_in_registration_flow(self):
        list_of_group = self.service.find_element(self.list_of_group)
        list_of_group.click()
        self.service.find_element(self.next_btn_step2).click()

    def select_profession(self, profession):
        profession_ele = self.profession_txt.format(profession)
        self.service.find_element(profession_ele).click()
        self.service.find_element(self.next_btn_step3).click()
        os.environ['profession'] = profession

    def validate_registered_user_on_loggedin_page(self):
        self.service.assert_element_present(self.profile_name)
