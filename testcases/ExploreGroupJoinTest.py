from nose.plugins.attrib import attr
from pages.ATG_login_page import ATGLoginPage
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.navigation_panel_page import NavigationPanelPage
from pages.explore_groups_page import explore_tab
import time
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)
# GR_0035

@attr(website=['world'])
class TimeToJoinGroupTest(DriverManager):
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
        group_found = TimeToJoinGroupTest.cycle_through_groups(self)
        if not group_found:
            logging.info("## All groups have already been joined ##")
            raise AssertionError
        self.service.switch_tab(1)
        self.service.wait_for_element(self.explore.join_button)
        start = time.time()
        self.service.click_element(self.explore.join_button)
        self.service.wait_for_element(self.explore.joined_green_button, 60)
        end = time.time()
        logging.info("## TIME TAKEN FOR BUTTON TO TURN GREEN = " + str(end - start) + " ##")

        # to check if the group is added to my groups we retrieve group name from url
        group_joined = self.service.url()
        group_joined = group_joined.replace('https://www.atg.world/go/', '')
        if '%' in group_joined:
            group_joined = group_joined.replace('%20', ' ')

        self.service.switch_tab(0)
        self.service.click_element(self.explore.my_groups_tab)
        self.service.wait_for_element(self.explore.my_groups_div)
        self.service.assert_text_present(group_joined, self.explore.my_groups_div)

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
                    group_found = TimeToJoinGroupTest.find_group(self)
                    if group_found:
                        return True

            else:
                # sleep required to ensure javascript loads
                time.sleep(1)
                group_found = TimeToJoinGroupTest.find_group(self)
                if group_found:
                    return True
            return False

    def find_group(self):
        all_groups = self.service.find_all_elements(self.explore.group)
        joined_groups = self.service.find_all_elements(self.explore.has_joined)
        children_groups = self.service.find_all_elements(self.explore.has_child)
        group_not_joined = list((set(all_groups) - set(children_groups)) - set(joined_groups))
        if len(group_not_joined) == 0:
            return False
        self.service.click_at_a_position(group_not_joined[0], 60, 20)
        return True
