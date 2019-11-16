import logging
from utility.services import Services
from selenium.webdriver.common.keys import Keys
from data.data_for_meetup import DataForMeetup


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class MeetupPage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.url = "https://www.atg.party/meetup"
        self.title_of_meetup_txtfield = "id=title"
        self.meetup_textarea = "xpath=//*[@class='fr-element fr-view']"
        self.contact_name_field = "id=contact_name"
        self.contact_number_field = "id=contact_number"
        self.email_field = "id=email_address"
        self.venue_field = "id=venue"
        self.add_cost_btn = "id=btn_cost"
        self.cost_free_btn = "xpath=//*[@class='title']"
        self.cost_paid_btn = "xpath=(//*[@class='title'])[2]"
        self.single_cost_btn = "xpath=(//*[@class='title'])[3]"
        self.multi_cost_btn = "xpath=(//*[@class='title'])[4]"
        self.online_btn = "xpath=(//*[@class='title'])[5]"
        self.next_btn_in_cost = "id=nextbtn"
        self.price_field_single_ticket = "id=cost"
        self.category_field1_multi = "xpath=//*[@name='advanced_opt_category[0]']"
        self.description_field1_multi = "xpath=//*[@name='advanced_opt_description[0]']"
        self.price_field1_multi_ticket = "id=advanced_opt_cost"
        self.category_field2_multi = "xpath=//*[@name='advanced_opt_category[2]']"
        self.description_field2_multi = "xpath=//*[@name='advanced_opt_description[2]']"
        self.price_field2_multi_ticket = "id=advanced_opt_cost2"
        self.new_ticket_btn_multi = "id=btAdd"
        self.cost_done_btn = "id=nextbtn"
        self.start_date_field = "id=start_dt"
        self.start_time = "id=start_tm"
        self.tags_field = "id=tag-tokenfield"
        self.group_field = "xpath=//*[@class='popover-tag-wrapper']"
        self.onclick_group_python = "xpath=//li[@data-value='181']"
        self.post_btn = "xpath=//button[text()='Post']"

    def click_post(self):
        self.service.click_element(self.post_btn)

    def filldata(self):
        self.driver.get(self.url)
        data = DataForMeetup()
        title = self.service.find_element(self.title_of_meetup_txtfield)
        title.send_keys(data.title)
        text = self.service.find_element(self.meetup_textarea)
        text.send_keys(data.text)
        contact_name = self.service.find_element(self.contact_name_field)
        contact_name.send_keys(data.name)
        contact_number = self.service.find_element(self.contact_number_field)
        contact_number.send_keys(data.number)
        email = self.service.find_element(self.email_field)
        email.send_keys(data.email)
        venue = self.service.find_element(self.venue_field)
        venue.send_keys(data.venue)
        self.service.click_element(self.start_date_field)
        date = self.service.find_element(self.start_date_field)
        date.send_keys(Keys.RETURN)
        self.service.click_element(self.start_time)
        start_time = self.service.find_element(self.start_time)
        start_time.send_keys(Keys.RETURN)
        tags = self.service.find_element(self.tags_field)
        tags.send_keys(data.tags)
        self.service.click_element(self.group_field)
        self.service.click_element(self.onclick_group_python)

    def post_as_free(self):
        self.filldata()
        self.service.click_element(self.add_cost_btn)
        self.service.click_element(self.cost_free_btn)
        self.service.click_element(self.cost_done_btn)
        self.click_post()

    def post_as_paid_single_ticket(self):
        self.filldata()
        self.service.click_element(self.add_cost_btn)
        self.service.click_element(self.cost_paid_btn)
        self.service.click_element(self.single_cost_btn)
        price = self.service.find_element(self.price_field_single_ticket)
        data = DataForMeetup()
        price.send_keys(data.price_for_single_ticket)
        (self.service.find_element(self.online_btn)).click()
        self.service.click_element(self.cost_done_btn)
        self.click_post()

    def post_as_paid_multi_ticket(self):
        self.filldata()
        self.service.click_element(self.add_cost_btn)
        self.service.click_element(self.cost_paid_btn)
        self.service.wait_for_element(self.multi_cost_btn)
        self.service.click_element(self.multi_cost_btn)
        data = DataForMeetup()
        price1 = self.service.find_element(self.price_field1_multi_ticket)
        price1.send_keys(data.price_category1)
        cat1 = self.service.find_element(self.category_field1_multi)
        cat1.send_keys(data.multi_category1)
        des1 = self.service.find_element(self.description_field1_multi)
        des1.send_keys(data.description_multi_category1)
        self.service.click_element(self.new_ticket_btn_multi)
        price2 = self.service.find_element(self.price_field2_multi_ticket)
        price2.send_keys(data.price_category2)
        cat2 = self.service.find_element(self.category_field2_multi)
        cat2.send_keys(data.multi_category2)
        des2 = self.service.find_element(self.description_field2_multi)
        des2.send_keys(data.description_multi_category2)
        opt_online = self.service.find_element(self.online_btn)
        self.driver.execute_script("arguments[0].click();", opt_online)
        self.service.click_element(self.cost_done_btn)
        self.click_post()