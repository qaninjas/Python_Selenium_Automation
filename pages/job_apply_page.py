from utility.services import Services

class JobApplyPage:
    def __init__(self, driver):
        self.driver = driver
        self.service = Services(self.driver)
        self.apply_btn = 'id=jobApply'
        self.phone_no = 'id=phone'
        self.email = 'id=email'
        self.why_hire = 'id=why_hire'
        self.resume_btn = 'css=.resume-group'
        self.upload = 'id=file'
        self.apply = 'id=btn_job_apply'