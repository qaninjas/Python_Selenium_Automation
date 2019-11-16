import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ATGLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.logo_img = "xpath=//*[@class='navbar-brand']"
        self.login_btn = "xpath=//*[text()='Login']"
        self.signin_tab = "id=log-in-tab"
        self.email_txtfiled = "xpath=(//*[@id='email'])[1]"
        self.password_txtfield = "xpath=(//*[@id='password'])[1]"
        self.signin_btn = "xpath=(//button[text()='Sign in'])[1]"
        self.username_lbl = "xpath=//a[@id='prof-name']/b"

    def wait_for_homepage_to_load(self):
        logging.info("## waiting for home-screen to be loaded ##")
        self.service.wait_for_element(self.logo_img)

    def login(self, userid = 'hello@atg.world', password='Pass@123'):
        logging.info("## Login user with valid credentials ##")
        self.service.find_element(self.login_btn).click()
        self.service.wait_for_element_visible(self.signin_tab)
        self.service.find_element(self.email_txtfiled).send_keys(userid)
        self.service.find_element(self.password_txtfield).send_keys(password)
        self.service.find_element(self.signin_btn).click()

    def validate_user_on_homepage(self):
        self.service.assert_element_present(self.username_lbl)
