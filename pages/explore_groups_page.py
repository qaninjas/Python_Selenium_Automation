import logging

from utility.services import Services

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)

class explore_tab:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.my_groups_tab = 'id=m-group'
        self.explore_groups_tab = 'id=exp-group'
        self.arrow = 'css=.group-left-icon'
        self.has_child = 'css=.group.has-child'
        self.group = 'css=.group'
        self.group_wrapper = 'css=.group-wrapper'
        self.icon = 'css=.group-icon'
        self.join_button = 'id=permJoin'
        self.joined_green_button = 'css=.joined-group'
        self.has_joined = 'css=.group.has-joined'
        self.leave = 'id=leave'
        self.confirm_leave = 'css=.confirm'
        self.my_groups_div = 'css=.inner-group-tab'
        self.recommended_group = 'css=.recomended-g-inner'




