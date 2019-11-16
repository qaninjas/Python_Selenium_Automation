from nose.plugins.attrib import attr


import logging
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.ATG_login_page import ATGLoginPage
from pages.message_page import MessagePage
from pages.meetup_page import MeetupPage
from pages.RSVP_post_page import PostPage


@attr(website=['party', 'world'])
class RSVPonMeetupTest(DriverManager):
    def login(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
    def test_1_post_a_mettup(self):
        logging.info("## Posting an Meetup")
        service = Services(self.driver)
        self.login()
        message_page = MessagePage(self.driver)
        message_page.nav_to_test_acc_msgs()
        initial_message_id=message_page.get_latest_message_id_no()
        logging.info("# Number of messages: %s" %initial_message_id)
        meetup = MeetupPage(self.driver)
        meetup.post_as_free()
        posted_meetup_link = service.get_url()
        logging.info("# Meetup posted at %s" %posted_meetup_link)
        service.reset_page_and_nav_to_homepage()

    # click_RSVP_with_another_account

        logging.info("# Confirming RSVP with another account")
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login("asdfghjk@asdf.ghj", "asdfghjk")
        atg_login_page.validate_user_on_homepage()
        postpage = PostPage(self.driver)
        postpage.open_post_page_and_click_rsvp_yes(posted_meetup_link)
        service.reset_page_and_nav_to_homepage()

    # check_if_message_recieved

        logging.info("# Verifying if message received")
        self.login()
        message_page.nav_to_test_acc_msgs()
        final_message_id= message_page.get_latest_message_id_no()
        assert (final_message_id > initial_message_id )\
            ,"Message not received"
