from utility.services import Services
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class my_group_tab:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.my_groups_tab = 'id=m-group'
        self.explore_groups_tab = 'id=exp-group'
        self.my_groups_div = 'css=.inner-group-tab'
        self.recommended_group = 'css=.recomended-g-inner'
        self.group_header = 'css=.my_group_li'
        self.groups = 'css=.my_group_li_chlid'