from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.navigation_panel_page import NavigationPanelPage
from pages.explore_groups_page import explore_tab
from pages.group_detail_page import GroupDetail



@attr(website=['world'])
class JobPostTest(DriverManager):
    def login(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.navigate = NavigationPanelPage(self.driver)
        self.service = Services(self.driver)
        self.explore = explore_tab(self.driver)
        self.group = GroupDetail(self.driver)
        self.service.wait_for_element(self.navigate.explore_groups_btn, 50)
        self.service.click_element(self.navigate.explore_groups_btn)
        self.service.wait_for_element(self.navigate.explore_groups_btn, 50)
        self.service.click_element(self.navigate.explore_groups_btn)
        joined_group = self.service.find_all_elements(self.explore.has_joined)
        # click box is small
        self.service.click_at_a_position(joined_group[0], 60, 20)
        self.service.switch_tab(1)
        self.service.wait_for_element(self.group.write_a_post, 30)
        # to check if the post event is from the correct group
        self.group_joined = self.service.url()
        self.group_joined = self.group_joined.replace('https://www.atg.world/go/', '')
        if '%' in self.group_joined:
            self.group_joined = self.group_joined.replace('%20', ' ')
        self.service.click_element(self.group.write_a_post)

    def test_article(self):
        self.login()
        self.service.click_element(self.group.article)
        self.service.assert_element_present(self.group.title)
        self.service.assert_text_present(self.group_joined, self.group.group_tag)

    def test_question(self):
        self.login()
        self.service.click_element(self.group.question)
        self.service.assert_element_present(self.group.title)
        self.service.assert_text_present(self.group_joined, self.group.group_tag)

    def test_event(self):
        self.login()
        self.service.click_element(self.group.event)
        self.service.assert_element_present(self.group.title)
        self.service.assert_text_present(self.group_joined, self.group.group_tag)

    def test_education(self):
        self.login()
        self.service.click_element(self.group.question)
        self.service.assert_element_present(self.group.title)
        self.service.assert_text_present(self.group_joined, self.group.group_tag)

    # currently not working (produces 404 error)
    # def test_jobs(self):
    #     self.login()
    #     self.service.click_element(self.group.jobs)
    #     self.service.assert_text_present(self.group_joined, self.group.group_tag)

    def test_meetup(self):
        self.login()
        self.service.click_element(self.group.meetup)
        self.service.assert_element_present(self.group.title)
        self.service.assert_text_present(self.group_joined, self.group.group_tag)
