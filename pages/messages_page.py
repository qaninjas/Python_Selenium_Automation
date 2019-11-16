import time

import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class message_tab:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        
        # for sending message
        self.compose_btn = 'xpath=//i[@class="icon-Post"]'
        self.title = 'id=model_title'
        self.recipents = 'css=#recipient_ids_chosen > ul > li > input'
        self.body = 'id=message_content_modal'
        self.send_msg = 'id=compose_btn_modal'
        
        # for checking message
        self.search = 'xpath=//input[@class="form-control live-search-box"]'
        self.className = 'class=user-message-list'

        # start a coversation
        self.text = 'xpath=//textarea[@id="message_to_send"]'
        self.send_btn = 'xpath=//button[@class="btn ims-send-btn"]'
        self.emoji_btn = 'xpath=//button[@id="emojiMenuBtn"]'
        self.emoji1 = 'xpath=//a[@title="bowtie"]'
        self.attatchment = 'xpath=//i[@class="fa fa-paperclip"]'