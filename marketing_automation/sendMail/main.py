from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import configparser
from config import Config
import os


Config().set_driver_path()

prop = configparser.ConfigParser()
prop.read(os.environ['config_file_path'])
application_env = prop['atg.env']['env']

chromedriver = os.environ['chrome_driver_path']
os.environ["webdriver.chrome.driver"] = chromedriver
prefs = {"profile.default_content_setting_values.notifications": 2}
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
options.add_experimental_option("prefs", prefs)

def sendGmail(mailId,password,subject,text,recipients):
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
    browser.maximize_window()
    browser.get('http://gmail.com')

    browser.find_element_by_id('identifierId').send_keys(mailId)
    browser.find_element_by_id('identifierNext').click()
    time.sleep(2)

    browser.find_element_by_name('password').send_keys(password)
    browser.find_element_by_id('passwordNext').click()
    time.sleep(5)

    # Open compose email
    for recepient in recipients:
        browser.find_element_by_css_selector('.z0 div').click()
        time.sleep(4)

        # Class name of "to" field of email composer might be changed
        recpnt = browser.find_element_by_class_name('vO')
        recpnt.click()
        recpnt.send_keys(recepient)
        time.sleep(1)

        # Email Subject
        browser.find_element_by_name('subjectbox').send_keys(subject)
        time.sleep(1)

        content = browser.find_element_by_class_name('editable')
        content.send_keys(text)
        content.send_keys(Keys.CONTROL+Keys.RETURN)
        time.sleep(1)
    browser.quit

mailId='atgtasksdinesh@gmail.com'
password = 'tisIscool'
sub='Test Email via selenium automation'
recipients = ['mail1@gmail.com','mail2@gmail.com']
sendGmail(mailId,password,sub,'content',recipients)
