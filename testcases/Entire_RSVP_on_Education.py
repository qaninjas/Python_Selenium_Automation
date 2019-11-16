from nose.plugins.attrib import attr


import logging
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.ATG_login_page import ATGLoginPage
from pages.education_page import EducationPage
from pages.message_page import MessagePage
from pages.RSVP_post_page import PostPage
from utility.services import Services


@attr(website=['party', 'world'])
class RSVPonEducationTest(DriverManager):
    def login(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
    def test_verify_entire_RSVP_on_education(self):
        logging.info("## Posting an Education")
        service = Services(self.driver)
        self.login()
        message_page = MessagePage(self.driver)
        message_page.nav_to_test_acc_msgs()
        initial_message_id=message_page.get_latest_message_id_no()
        logging.info("#number of messages: %s" %initial_message_id)
        education = EducationPage(self.driver)
        education.filldata_and_post()
        posted_event_link = service.get_url()
        logging.info("Education posted at %s" %posted_event_link)
        service.reset_page_and_nav_to_homepage()

    #click_RSVP_with_another_account

        logging.info("confirming RSVP with another account")
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login("asdfghjk@asdf.ghj", "asdfghjk")
        atg_login_page.validate_user_on_homepage()
        postpage=PostPage(self.driver)
        postpage.open_post_page_and_click_rsvp_yes(posted_event_link)
        service.reset_page_and_nav_to_homepage()

    #check_if_message_recieved

        logging.info("verifying if message received")
        self.login()
        message_page.nav_to_test_acc_msgs()
        final_message_id= message_page.get_latest_message_id_no()
        assert (final_message_id > initial_message_id )\
            ,"Message not received"
