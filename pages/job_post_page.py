from utility.services import Services   

class JobPostPage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.hire = 'id=hire-input'
        self.job_title = 'id=title-input'
        self.description = 'css=#descr-form > div > div.fr-wrapper > div'
        self.location = 'id=location'
        self.company_name = 'id=emp-cmp-name-input'
        self.company_site = 'id=emp-cmp-web-input'
        self.edu_skill = 'id=job-edu-skills-input'
        self.ext_link = 'id=job-ext-links-input'
        self.app_deadline = 'id=job-app-deadline-input'
        self.min_experience = 'id=job-min-exp-input'
        self.employment_type = 'id=job-emp-type-form'
        self.post_btn = 'id=post-btn'
        self.employment_type_list = 'id=job-emp-type-list'
        self.min_experience_option = 'css=#job-min-exp-input > option:nth-child(2)'
        self.calender_today = 'css=.ui-datepicker-today'
        self.type = 'css=#job-emp-type-list > li:nth-child(1) > a'
        self.lawyer = 'css=#suggestions > ul > li > a'

