import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class PasswordSetting:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.my_account_summary_lbl = "xpath=//div[@class='clearfix']//preceding::*[text()='My Account Summary']"
        self.new_pass_txtfield = "id=new_password"
        self.cnfm_pass_txtfield = "id=confirm_password"
        self.save_btn = "id=btn_noti_setting"
