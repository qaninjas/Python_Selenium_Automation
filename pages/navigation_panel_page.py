import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class NavigationPanelPage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.home_btn = "xpath=//*[text()='Home']"
        self.write_post_btn = "xpath=//li[contains(text(),'Write a Post')]"
        self.messages_btn = "xpath=//li[contains(text(),'Messages')]"
        self.my_groups_btn = "xpath=//li[contains(text(),'My Groups')]"
        self.explore_groups_btn = "xpath=//li[contains(text(),'Explore Groups')]"
        self.my_posts_btn = "xpath=//li[contains(text(),'My Posts')]"
        self.invite_friends_btn = "xpath=//li[contains(text(),'Invite Friends')]"
        self.upcomings_btn = "xpath=//li[contains(text(),'Upcoming')]"
        self.setting_btn = "xpath=//li[contains(text(),'Settings')]"

        self.writepost_submenu = "xpath=//*[@class='submenu list-group']"
        self.event_lnk = "xpath=//a[text()='Event']"
        self.meetup_lnk = "xpath=//a[text()='Meetup']"
        self.article_lnk = "xpath=//a[text()='Article']"
        self.education_lnk = "xpath=//a[text()='Education' and @class]"
        self.Qrious = "xpath=//a[text()='Qrious']"
        self.job_lnk = "xpath=//a[text()='Job']"

        self.privacy = "css=#sidebar-exp > div > p > a:nth-child(1)"
        self.help = "css=#sidebar-exp > div > p > a:nth-child(2)"
        self.terms = "css=#sidebar-exp > div > p > a:nth-child(3)"
