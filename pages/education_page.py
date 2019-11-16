import logging
from utility.services import Services
from data.data_for_education_post import DataForEducation
from selenium.webdriver.common.keys import Keys


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class EducationPage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.url = "https://www.atg.party/education"
        self.title_of_edu_txtfield = "id=title"
        self.edu_textarea = "xpath=//*[@class='fr-element fr-view']"
        self.types = "xpath=//*[@class='btn btn-primary btn-primary-type']"
        self.website_field = "id=website"
        self.add_cost_btn = "id=btn_cost"
        self.cost_free_btn = "xpath=//*[@class='title']"
        self.cost_done_btn = "id=nextbtn"
        self.tags_field = "id=tag-tokenfield"
        self.group_field = "xpath=//*[@class='popover-tag-wrapper']"
        self.onclick_group_python = "xpath=//li[@data-value='181']"
        self.post_btn = "xpath=//button[text()='Post']"

    def filldata_and_post(self):
        self.driver.get(self.url)
        data = DataForEducation()
        title = self.service.find_element(self.title_of_edu_txtfield)
        title.send_keys(data.title)
        text = self.service.find_element(self.edu_textarea)
        text.send_keys(data.text)
        types_to_select = self.service.find_elements(self.types)
        types_to_select[1].click()
        types_to_select[3].click()
        website = self.service.find_element(self.website_field)
        website.send_keys(data.website)
        tags = self.service.find_element(self.tags_field)
        tags.send_keys(data.tags)
        self.service.click_element(self.group_field)
        self.service.click_element(self.onclick_group_python)
        self.service.click_element(self.add_cost_btn)
        self.service.click_element(self.cost_free_btn)
        self.service.click_element(self.cost_done_btn)
        self.service.click_element(self.post_btn)
