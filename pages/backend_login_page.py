import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class BackendLoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.backend_url = "https://www.atg.party/auth/admin/login"
        self.form_box = "xpath=//*[@id='login-box']"
        self.username_field = "xpath=//*[@name='user_name']"
        self.password_field = "xpath=//*[@name='user_password']"
        self.login_btn = "xpath=//*[text()='Sign In']"
        self.tab_name_on_dashboard = "Welcome to Admin Dashboard"
    def nav_to_login_page(self):
        self.driver.get(self.backend_url)

    def wait_for_loginpage_to_load(self):
        logging.info("## waiting for backend login page to load ##")
        self.service.wait_for_element(self.form_box)

    def validate_used_loggedIn(self):
        logging.info("## checking if browser on Admin Dashboard ##")
        tab_name = self.service.get_tab_name()
        assert tab_name == self.tab_name_on_dashboard

    def login(self,username = "admin",password = "Pass@123"):
        logging.info("## Login user with valid credentials ##")
        self.service.find_element(self.username_field).send_keys(username)
        self.service.find_element(self.password_field).send_keys(password)
        self.service.find_element(self.login_btn).click()
        self.validate_used_loggedIn()

