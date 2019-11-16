from nose.plugins.attrib import attr
from pages.backend_login_page import BackendLoginPage
from utility.drivermanager import DriverManager
from pages.backend_manage_articles_page import BackendManageArticle

@attr(website=['party', 'world'])
class VerifyEditinArticle(DriverManager):
    def backend_login(self):
        backend_login_page = BackendLoginPage(self.driver)
        backend_login_page.nav_to_login_page()
        backend_login_page.wait_for_loginpage_to_load()
        backend_login_page.login()
    def test_Edit_article(self):
        self.backend_login()
        manage_article_page = BackendManageArticle(self.driver)
        manage_article_page.nav_to_article_list()
        manage_article_page.click_edit()
        self.driver.implicitly_wait(1)
        manage_article_page.validate_user_on_edit_article_page()


