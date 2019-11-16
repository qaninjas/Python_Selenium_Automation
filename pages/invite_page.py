import time

import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class invite:
    def __init__(self,driver):
        self.driver = driver
        self.service = Services(self.driver)

        # button for facebook
        self.facebook_btn = "xpath=//i[@class='fa fa-facebook-f']"

        #button for twitter
        self.twitter_btn = "xpath=//i[@class='fa fa-twitter']"

        #button for linkedin
        self.linkedin_btn = "xpath=//i[@class='fa fa-linkedin']"

        #button for google+
        self.googlePlus_btn = "xpath=//i[@class='fa fa-google-plus']"

        #button for copying url
        self.copy_url_btn = "xpath=//i[@class='fa fa-copy']"

        #buttons for adding and validating new username
        self.new_username_input = "xpath=//input[@id='new_user_name']"
        self.save_btn = "xpath=//button[@class='save-btn btn']"
        self.condition = "xpath=//span[@class='usr_msg1']"

