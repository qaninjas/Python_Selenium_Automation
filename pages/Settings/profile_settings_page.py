import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ProfileSettings:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.my_account_summary_lbl = "xpath=//div[@class='clearfix']//preceding::*[text()='My Account Summary']"
        self.about_you_dropdown = "id=user_type"
        self.about_you_selected_option = "xpath=//select[@id='user_type']/option[@selected='selected']"
        self.aboutuserfiled_update_error_message = "xpath=//*[@id='usr_ut_msg' and @class='hide']"
        self.username_txtfield = "id=user_name"
        self.firstname_txtfield = "id=first_name"
        self.lastname_txtfield = "id=last_name"
        self.email_txtfield = "id=email"
        self.mobileno_txtfield = "id=mob_no"
        self.phoneno_txtfield = "id=phone_no"
        self.location_txtfield = "id=location"
        self.about_me_txtfield = "id=about_me"
        self.tagline_txtfield = "id=tagline"
        self.profession_dropdown = "id=profession"
        self.male_radiobtn = "xpath=//*[@name='gender' and @value='0']"
        self.dob_txtfield = "id=dob"
        self.is_google_crawalable_checkbox = "id=is_google_crawalable"
        self.save_btn = "id=btn_account_setting"

