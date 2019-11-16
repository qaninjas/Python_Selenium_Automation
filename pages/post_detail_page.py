from utility.services import Services

class PostDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.share_facebook = 'xpath=//*[@id="fb_share"]'
        self.share_twitter = 'css=.btn.twictt'
        self.share_linkedin = 'css=.btn.link-eple'
        self.share_reddit = 'css=.btn.gogle-pluet'
        self.random_post = 'css=.media-heading'

    def navigate_to_post_detail_page(self):
        self.service.wait_for_element(self.random_post, 60)
        self.service.click_element(self.random_post)

    def click_share_facebook(self):
        self.service.wait_for_element(self.share_facebook, 30)
        self.service.click_element(self.share_facebook)

    def click_share_twitter(self):
        self.service.wait_for_element(self.share_twitter, 30)
        self.service.click_element(self.share_twitter)

    def click_share_linkedin(self):
        self.service.wait_for_element(self.share_linkedin, 30)
        self.service.click_element(self.share_linkedin)

    def click_share_reddit(self):
        self.service.wait_for_element(self.share_reddit, 30)
        self.service.click_element(self.share_reddit)
