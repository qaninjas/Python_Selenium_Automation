import logging
import os
import time

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.profile_img = "id=main_profile1"
        self.username = "css=div.insaan_ka_naam"
        self.upload_picture_btn = "id=upload"
        self.profile_submit_btn = "id=profile_submit"

    def tap_on_file_upload(self):
        self.service.click_element(self.profile_img)
        self.profile_url_avtar = self.service.find_element(self.profile_img).get_attribute("src")
        self.service.wait_for_element(self.upload_picture_btn)

    def upload_profile_image(self, mg_path):
        self.service.find_element(self.upload_picture_btn).send_keys(mg_path)
        self.service.wait_for_element_visible(self.profile_submit_btn)
        self.service.click_element(self.profile_submit_btn)
        time.sleep(10)

    def validate_uploaded_profile_pic(self):
        self.service.wait_for_element_visible(self.username)
        self.service.wait_for_element_visible(self.profile_img)
        self.uploaded_profile_url = self.service.find_element(self.profile_img).get_attribute("src")
        return self.profile_url_avtar, self.uploaded_profile_url
