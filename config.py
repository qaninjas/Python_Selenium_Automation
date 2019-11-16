import os


class Config:

    def set_driver_path(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        chrome_driver_path = os.path.join(ROOT_DIR, 'drivers\chromedriver.exe')
        profile_pic_path = os.path.join(ROOT_DIR, 'testrun_evidences\Images\profile_pic.jpg')
        updated_profile_pic_path = os.path.join(ROOT_DIR, 'testrun_evidences\Images\profile_updated_picture.jpg')
        resume_path = os.path.join(ROOT_DIR, 'testrun_evidences\PDF\ATGPythonAutomation.pdf')
        config_file_path = os.path.join(ROOT_DIR, 'config.ini')

        os.environ["chrome_driver_path"] = chrome_driver_path
        os.environ['profile_pic_path'] = profile_pic_path
        os.environ['updated_profile_pic_path'] = updated_profile_pic_path
        os.environ['resume_path'] = resume_path
        os.environ['config_file_path'] = config_file_path
