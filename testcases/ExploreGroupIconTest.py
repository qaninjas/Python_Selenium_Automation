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
# GR_0034

@attr(website=['world'])
class ValidateExploreGroupIcon(DriverManager):
    def test_explore_group_icon(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
        self.service = Services(self.driver)
        self.navigate = NavigationPanelPage(self.driver)
        self.explore = explore_tab(self.driver)
        self.service.wait_for_element(self.navigate.explore_groups_btn, 50)
        self.service.click_element(self.navigate.explore_groups_btn)
        self.old_icons = []
        ValidateExploreGroupIcon.cycle_through_groups(self)

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
                    ValidateExploreGroupIcon.verify_image(self)
            else:
                # sleep required to ensure javascript loads
                time.sleep(1)
                ValidateExploreGroupIcon.verify_image(self)

    def verify_image(self):
        icons = self.service.find_all_elements(self.explore.icon)
        new_icons = list(set(icons) - set(self.old_icons))
        for k in range(len(new_icons)):
            logging.info("## checking if icon is displayed ##")
            new_icons[k].is_displayed()
            self.old_icons.append(new_icons[k])

