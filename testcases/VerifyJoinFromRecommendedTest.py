from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.navigation_panel_page import NavigationPanelPage
from pages.explore_groups_page import explore_tab
# GR_0037

@attr(website=['world'])
class VerifyRecommendedGroup(DriverManager):
    def test_join_from_recommendation(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.service = Services(self.driver)
        self.navigate = NavigationPanelPage(self.driver)
        self.explore = explore_tab(self.driver)
        self.service.wait_for_element(self.navigate.my_groups_btn, 30)
        self.service.click_element(self.navigate.my_groups_btn)
        self.service.click_element(self.explore.recommended_group)
        self.service.wait_for_element(self.explore.join_button,30)
        self.service.click_element(self.explore.join_button)
        self.service.wait_for_element(self.explore.joined_green_button, 30)
        # to check if the group is added to my groups we retrieve group name from url
        group_joined = self.service.url()
        group_joined = group_joined.replace('https://www.atg.world/go/', '')
        if '%' in group_joined:
            group_joined = group_joined.replace('%20', ' ')

        self.service.go_back()
        self.service.wait_for_element(self.explore.my_groups_div)
        self.service.assert_text_present(group_joined, self.explore.my_groups_div)



