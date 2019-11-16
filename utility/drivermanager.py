import logging
import os
import sys
import time
import unittest
import urllib

import requests
from selenium import webdriver
import configparser

from config import Config

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class DriverManager(unittest.TestCase):
    """
    This class is for instantiating web driver instances.
    """

    def setUp(self):
        """
        This method is to instantiate the web driver instance.
        """
        r = requests.get("https://www.atg.party/")
        web_status_code = r.status_code
        if web_status_code == 200:
            logging.info("## WEB APPLICATION IS UP AND RUNNING ##")
            logging.info("## SETUP METHOD ##")
            logging.info("# Initializing the webdriver.")

            Config().set_driver_path()

            # load ini file
            prop = configparser.ConfigParser()
            prop.read(os.environ['config_file_path'])
            application_env = prop['atg.env']['env']

            chromedriver = os.environ['chrome_driver_path']
            os.environ["webdriver.chrome.driver"] = chromedriver
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            # options.add_argument('headless')
            options.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
            
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

            if application_env == 'ATGWorld':
                self.driver.get("https://www.atg.world/")
            else:
                self.driver.get("https://www.atg.party/")
            load_time = self.driver.execute_script(
                """
                 var loadTime = ((window.performance.timing.domComplete- window.performance.timing.navigationStart)/1000)+" sec.";
                 return loadTime;
                 """
            )

            error_log = self.driver.get_log('browser')
            error_log_size = len(error_log)
            if error_log_size > 1:
                logging.info("## WEB APPLICATION CONTENET IS NOT LOADED PROPERLY. HENCE TERMINATING EXECUTION ##")
                self.assertFalse(False)
            logging.info("## WEB APPLICATION LOADING TIME : %s" % load_time)
            load_time = load_time.split(' ')

            if float(load_time[0]) > 10.000:
                logging.info("## WEB APPLICATION PERFORMANCE IS SLOW, sSO STOPPING EXECUTION HERE ##")
                self.assertFalse(False)
        else:
            logging.info("## WEB APPLICATION IS DOWN AND NOT RUNNING ##")
            self.assertFalse(True, 'Given web application is down')

    def tearDown(self):
        """
        This is teardown method.
        It is to capture the screenshots for failed test cases,
        & to remove web driver object.
        """
        logging.info("## TEARDOWN METHOD ##")

        if sys.exc_info()[0]:
            logging.info("# Taking screenshot.")
            test_method_name = self._testMethodName
            self.driver.save_screenshot("./../screenshots/%s.png" % test_method_name)

        if self.driver is not None:
            logging.info("# Removing the webdriver.")
            self.driver.quit()

    def create_ffprofile(self):
        """
        This function is to create firefox profile.
        :return: firefox profile.
        """
        logging.info("# Setting up firefox profile.")
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)  # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', os.getcwd())
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                               'text/csv,application/octet-stream,application/pdf,application/vnd.ms-excel')
        profile.set_preference("pdfjs.disabled", True)

        return profile


if __name__ == '__main__':
    unittest.main()
