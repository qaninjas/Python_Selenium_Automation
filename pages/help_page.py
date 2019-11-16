from utility.services import Services

class HelpPage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.header = "css=#content > section.contact-sec > div > h1"

