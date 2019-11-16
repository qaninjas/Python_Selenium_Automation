import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class AppliedJob:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.job_table = 'id=example1'