import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ManageResume:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.choose_fle_btn = "xpath=//*[@name='file']"
        self.upload_resume_lbl = "xpath=//h4[text()='Upload Resumes']"
        self.upload_resumes_btn = "id=btn_upload_resumes"
        self.uploaded_resume_section = "xpath=//*[@title='See Resume']"
        self.delete_resume_btn = "xpath=//*[@class='remores']"
