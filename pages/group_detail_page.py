from utility.services import Services

class GroupDetail:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.join_button = 'id=permJoin'
        self.joined_green_button = 'css=.joined-group'
        self.has_joined = 'css=.group.has-joined'
        self.leave = 'id=leave'
        self.confirm_leave = 'css=.confirm'
        self.write_a_post = 'id=dropdownMenuButton'
        self.article = 'css=#dropdownmenu2 > a:nth-child(1)'
        self.question = 'css=#dropdownmenu2 > a:nth-child(2)'
        self.event = 'css=#dropdownmenu2 > a:nth-child(3)'
        self.education = 'css=#dropdownmenu2 > a:nth-child(4)'
        self.jobs = 'css=#dropdownmenu2 > a:nth-child(5)'
        self.meetup = 'css=#dropdownmenu2 > a:nth-child(6)'
        self.group_tag = 'css=.popover-select-tags'
        self.title = 'id=title'
