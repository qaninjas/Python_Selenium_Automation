import logging
from utility.services import Services


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class PostPage:
    def __init__(self,driver):
        self.driver=driver
        self.service = Services(self.driver)
        self.rsvp_yes = "id=status_no"
    def open_post_page_and_click_rsvp_yes(self,post_link):
        self.driver.get(post_link)
        rsvp_yes_btn = self.service.find_element(self.rsvp_yes)
        rsvp_yes_btn.click()
