import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class Settings:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.setting_lbl = "xpath=//li[text()='Settings']"
        self.account_setting_lbl = "id=settings"
        self.profile_setting_btn = "id=profile_setting"
        self.manage_resume_btn = "id=manage_resume"
        self.notification_setting_btn = "id=notification_setting"
        self.password_setting_btn = "id=pwd_setting"
        self.my_applied_jobs_btn = "id=my_job_student"
        self.logout_btn = "xpath=//*[contains(text(),'Logout')]"

    def navigate_to_settings(self):
        self.service.find_element(self.account_setting_lbl).click()
