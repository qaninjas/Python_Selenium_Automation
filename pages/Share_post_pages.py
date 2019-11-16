from utility.drivermanager import DriverManager
from utility.services import Services

class ShareWith:
    def __init__(self,driver):
        self.driver = driver
        self.facebook_title = "Facebook"
        self.twitter_title = "Share a link on Twitter"
        self.reddit_title = 'reddit.com: Log in'
        self.linkedin_title = 'LinkedIn'
    def validate_user_on_facebook_share_post_page(self):
        Services(self.driver).assert_new_tab_opened(self.facebook_title)

    def validate_user_on_twitter_share_post_page(self):
        Services(self.driver).assert_new_tab_opened(self.twitter_title)

    def validate_user_on_reddit_share_post_page(self):
        Services(self.driver).assert_new_tab_opened(self.reddit_title)

    def validate_user_on_linkedin_share_post_page(self):
        Services(self.driver).assert_new_tab_opened(self.linkedin_title)