import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.site_logo_img = "xpath=//*[@alt='SITE-LOGO']"
        self.notification_img = "xpath=//*[@title='Notification']"
        self.profile_name_lbl = "xpath=//*[@id='prof-name']/b"
        self.logged_profile_img = "id=main_profile"
        self.filter_txt_on_homescreen = "css=.filter-text"
        self.filter_options = "xpath=//a[text()='{}' and @onclick]"
        self.posts = "css=.white-panel"
        self.share_btn = "class=fa-share-alt"
        self.share_wfacebook = "class=fa-facebook"
        self.share_wtwitter = "class=fa-twitter"
        self.share_wreddit = "class=fa-reddit"
        self.share_wlinkedin = "class=fa-linkedin"
        # self.list_of_posts = self.get_posts()

    def navigate_to_main_profile(self):
        self.service.wait_for_element(self.profile_name_lbl)
        self.service.click_element(self.logged_profile_img)

    def get_posts(self):
        return self.service.find_elements(self.posts)

    def click_share(self):
        list_of_posts = self.get_posts()
        list_of_posts[1].find_element_by_class_name(self.share_btn.replace("class=","")).click()
    def share_with_facebook(self):
        self.click_share()
        list_of_posts = self.get_posts()
        list_of_posts[1].find_element_by_class_name(self.share_wfacebook.replace("class=", "")).click()
    def share_with_twitter(self):
        self.click_share()
        list_of_posts = self.get_posts()
        list_of_posts[1].find_element_by_class_name(self.share_wtwitter.replace("class=", "")).click()
    def share_with_reddit(self):
        self.click_share()
        list_of_posts = self.get_posts()
        list_of_posts[1].find_element_by_class_name(self.share_wreddit.replace("class=", "")).click()
    def share_with_linkedin(self):
        self.click_share()
        list_of_posts = self.get_posts()
        list_of_posts[1].find_element_by_class_name(self.share_wlinkedin.replace("class=", "")).click()
