import logging
from time import sleep

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class FileUpLoadingPage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.xpathUploadBtn = "//input[@id='file-submit']"

    def verify_uploaded_file(self):
        self.driver.find_element_by_xpath(self.xpathChooseFile).send_keys(
            "E:\\eclipse\\selLearning\\download\\menu.pdf")

        sleep(2)
        self.services.assert_and_click_by_xpath(self.xpathUploadBtn)
        self.services.wait_for_element(self.xpathUploadedFiles)
        assert "menu.pdf" == self.services.get_text_by_xpath(self.xpathUploadedFiles)
