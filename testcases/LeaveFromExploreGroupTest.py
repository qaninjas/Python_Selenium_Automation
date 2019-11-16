from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.navigation_panel_page import NavigationPanelPage
from pages.explore_groups_page import explore_tab
from pages.my_groups_page import my_group_tab
import time
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)
# GR_0039

@attr(website=['world'])
class LeaveFromExploreGroupTest(DriverManager):
    def test_leave_group(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.service = Services(self.driver)
        self.navigate = NavigationPanelPage(self.driver)
        self.explore = explore_tab(self.driver)
        self.my = my_group_tab(self.driver)
        self.service.wait_for_element(self.navigate.explore_groups_btn, 50)
        self.service.click_element(self.navigate.explore_groups_btn)
        left = LeaveFromExploreGroupTest.cycle_through_groups(self)
        if not left:
            logging.info("## All groups have already been left ##")
            raise AssertionError
        self.service.click_element(self.navigate.my_groups_btn)
        self.service.wait_for_element(self.my.groups, 30)
        self.service.assert_text_not_present(self.name_of_group, self.my.my_groups_div)

    # this function cycles through the group tabs in the explore group page
    def cycle_through_groups(self):
        tabs = self.service.find_all_elements(self.explore.has_child)
        for i in range(len(tabs)):
            logging.info("## clicking on " + tabs[i].text + " ##")
            tabs[i].click()
            # sleep required to ensure javascript loads
            time.sleep(1)
            tabs_hidden = self.service.find_all_elements(self.explore.has_child)
            tabs_hidden = list(set(tabs_hidden) - set(tabs))
            if len(tabs_hidden) > 0:
                for j in range(len(tabs_hidden)):
                    logging.info("## clicking on " + tabs_hidden[j].text + " ##")
                    tabs_hidden[j].click()
                    # sleep required to ensure javascript loads
                    time.sleep(1)
                    left = LeaveFromExploreGroupTest.leave_group(self)
                    if left:
                        return True
            else:
                # sleep required to ensure javascript loads
                time.sleep(1)
                left = LeaveFromExploreGroupTest.leave_group(self)
                if left:
                    return True
            return False

    # this function finds and leaves a group that has been joined
    def leave_group(self):

            joined_groups = self.service.find_all_elements(self.explore.has_joined)

            # if no such group is found return and continue cycling the through the group tabs
            if len(joined_groups) == 0:
                return False

            # if found click on the group at a location with no links to make sure it is loaded
            self.service.click_at_a_position(joined_groups[0], 240, 30)
            # find the number of joined groups prior to clicking on the + icon
            joined_groups = self.service.find_all_elements(self.explore.has_joined)
            # click on the plus icon
            self.service.click_at_a_position(joined_groups[0], 225.625, 29)

            # save the name of the group joined to check if it has been left
            self.name_of_group = joined_groups[0].text
            # sleep required to ensure javascript loads
            time.sleep(1)
            # find the number of joined groups to assert that the tick icon has become the plus icon
            new_joined_groups = self.service.find_all_elements(self.explore.has_joined)
            # checks by asserting if the number classes for the tick icons have decreased
            assert len(new_joined_groups) < len(joined_groups)
            return True

