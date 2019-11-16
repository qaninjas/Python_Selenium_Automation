from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
import logging
from utility.services import Services
from pages.post_detail_page import PostDetailPage
#task 10

@attr(website=['party', 'world'])
class PostDetailShareTest(DriverManager):
    def login(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.post = PostDetailPage(self.driver)
        self.post.navigate_to_post_detail_page()
        self.service = Services(self.driver)

    def test_facebook(self):
        PostDetailShareTest.login(self)
        self.post.click_share_facebook()
        check = self.service.check_tab('Facebook')
        assert check
        logging.info("sharing link works")

    def test_twitter(self):
        PostDetailShareTest.login(self)
        self.post.click_share_twitter()
        check = self.service.check_tab('Share a link on Twitter')
        assert check
        logging.info("sharing link works")

    def test_reddit(self):
        PostDetailShareTest.login(self)
        self.post.click_share_reddit()
        check = self.service.check_tab('reddit.com: Log in')
        assert check
        logging.info("sharing link works")

    def test_linkedin(self):
        PostDetailShareTest.login(self)
        self.post.click_share_linkedin()
        check = self.service.check_tab('LinkedIn')
        assert check
        logging.info("sharing link works")

