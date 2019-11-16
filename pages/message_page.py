import logging
from utility.services import Services


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class MessagePage:
    def __init__(self,driver):
        self.driver =driver
        self.messages="xpath=//*[@class ='media']"
        self.message_page_link="https://www.atg.party/message"
        self.test_acc = "xpath=//*[text()='asdf ghjk']"
        self.service = Services(self.driver)
    def get_latest_message_id_no(self):
        message_elements = self.service.find_elements(self.messages)
        return (message_elements[len(message_elements)-1
                                 ].get_attribute('id')).replace('message_div','')
    def nav_to_test_acc_msgs(self):
        self.driver.get(self.message_page_link)
        service= Services(self.driver)
        test_acc_msgs = service.find_element(self.test_acc)
        self.driver.execute_script("arguments[0].click();",test_acc_msgs )
