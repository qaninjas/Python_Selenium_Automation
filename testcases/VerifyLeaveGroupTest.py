from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.navigation_panel_page import NavigationPanelPage
from pages.explore_groups_page import explore_tab
import time
# GR_0036


@attr(website=['world'])
class VerifyLeaveGroup(DriverManager):
    def test_time_taken_to_join(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.service = Services(self.driver)
        self.navigate = NavigationPanelPage(self.driver)
        self.explore = explore_tab(self.driver)
        self.service.wait_for_element(self.navigate.explore_groups_btn, 50)
        self.service.click_element(self.navigate.explore_groups_btn)

        joined_group = self.service.find_all_elements(self.explore.has_joined)
        self.service.click_at_a_position(joined_group[0], 60, 20)
        self.service.switch_tab(1)
        self.service.wait_for_element(self.explore.joined_green_button, 30)
        self.service.click_element(self.explore.leave)
        self.service.wait_for_element(self.explore.confirm_leave, 30)
        # sleep required to ensure javascript loads
        time.sleep(1)
        self.service.click_element(self.explore.confirm_leave)
        # to check if the group is added to my groups we retrieve group name from url
        group_joined = self.service.url()
        group_joined = group_joined.replace('https://www.atg.world/go/', '')
        if '%' in group_joined:
            group_joined = group_joined.replace('%20', ' ')
        self.service.wait_for_element_invisible(self.explore.joined_green_button)

        self.service.switch_tab(0)
        # self.service.refresh_page()
        self.service.wait_for_element(self.explore.my_groups_tab)
        self.service.click_element(self.explore.my_groups_tab)
        self.service.assert_text_not_present(group_joined, self.explore.my_groups_div)



