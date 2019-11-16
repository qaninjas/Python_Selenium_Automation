import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class ArticlePage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.ask_question_lnk = "xpath=//a[text()=' Ask Question']"
        self.post_event_lnk = "xpath=//a[text()=' Post Event']"
        self.post_article_lnk = "xpath=//a[text()=' Post Article']"
        self.post_meetup_lnk = "xpath=//a[text()=' Post Meetup']"
        self.post_education_lnk = "xpath=//a[text()=' Post Education']"
        self.post_job_lnk = "xpath=//a[text()=' Post Job']"
        self.title_of_article_txtfield = "id=title"
        self.image_uploader = "xpath=//*[@class='uploar-imger']"
        self.article_textarea = "xpath=//*[@class='fr-element fr-view']"
        self.tag_lbl = "xpath=//label[text()='TAGS']"
        self.tag_txtfield = "id=tags-tokenfield"
        self.group_txtfield = "//*[@class='popover-tag-wrapper']"
        self.group_lbl = "xpath=//label[text()='GROUP']"
        self.save_And_close_btn = "xpath=//button[text()='Save & Close']"
        self.post_btn = "xpath=//button[text()='Post']"

