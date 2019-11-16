# Scenario : Verify aNavigation element (Left navigation panel)
from nose.plugins.attrib import attr
from utility.services import Services
from utility.drivermanager import DriverManager
from pages.ATG_login_page import ATGLoginPage
from pages.navigation_panel_page import NavigationPanelPage


@attr(website=['party', 'world'])
class VerifyNavigationPanelElementTest(DriverManager):
    def test_verify_navigation_panel_element(self):
        atg_login_page = ATGLoginPage(self.driver)
        self.service = Services(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()

        navigation_panel_page = NavigationPanelPage(self.driver)
        self.service.assert_element_present(navigation_panel_page.home_btn)
        self.service.assert_element_present(navigation_panel_page.write_post_btn)
        self.service.assert_element_present(navigation_panel_page.messages_btn)
        self.service.assert_element_present(navigation_panel_page.my_groups_btn)
        self.service.assert_element_present(navigation_panel_page.explore_groups_btn)
        self.service.assert_element_present(navigation_panel_page.my_posts_btn)
        self.service.assert_element_present(navigation_panel_page.invite_friends_btn)
        self.service.assert_element_present(navigation_panel_page.upcomings_btn)
        self.service.assert_element_present(navigation_panel_page.explore_groups_btn)
        self.service.assert_element_present(navigation_panel_page.setting_btn)
