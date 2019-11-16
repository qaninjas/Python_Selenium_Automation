# Scenario : Verify UI element of Post an article page
from nose.plugins.attrib import attr
from pages.article_page import ArticlePage
from utility.services import Services
from utility.drivermanager import DriverManager
from pages.navigation_panel_page import NavigationPanelPage
from pages.ATG_login_page import ATGLoginPage


@attr(website=['party', 'world'])
class VerifyUIOfPostArticlePage(DriverManager):
    def test_verify_ui_of_post_article_screen(self):
        atg_login_page = ATGLoginPage(self.driver)
        self.service = Services(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()

        #         navigate to post an article page
        navigation_panel_page = NavigationPanelPage(self.driver)
        article_page = ArticlePage(self.driver)
        self.service.find_element(navigation_panel_page.write_post_btn).click()
        self.service.find_element(navigation_panel_page.article_lnk).click()
        self.service.assert_element_present(article_page.ask_question_lnk)
        self.service.assert_element_present(article_page.post_event_lnk)
        self.service.assert_element_present(article_page.post_article_lnk)
        self.service.assert_element_present(article_page.post_meetup_lnk)
        self.service.assert_element_present(article_page.post_education_lnk)
        self.service.assert_element_present(article_page.post_job_lnk)

        self.service.assert_element_present(article_page.ask_question_lnk)
        self.service.assert_element_present(article_page.post_job_lnk)
        self.service.assert_element_present(article_page.post_event_lnk)
        self.service.assert_element_present(article_page.post_article_lnk)
        self.service.assert_element_present(article_page.post_meetup_lnk)
        self.service.assert_element_present(article_page.post_education_lnk)
        self.service.assert_element_present(article_page.post_job_lnk)

        self.service.assert_element_present(article_page.title_of_article_txtfield)
        self.service.assert_element_present(article_page.image_uploader)
        self.service.assert_element_present(article_page.tag_lbl)
        self.service.assert_element_present(article_page.group_lbl)
        self.service.assert_element_present(article_page.save_And_close_btn)
        self.service.assert_element_present(article_page.post_btn)
