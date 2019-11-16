from nose.plugins.attrib import attr


import logging
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.ATG_login_page import ATGLoginPage
from pages.event_page import EventPage
from pages.message_page import MessagePage
from pages.RSVP_post_page import PostPage


@attr(website=['party', 'world'])
class RSVPonEventTest(DriverManager):
    def login(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
    def test_verify_rsvp_on_event(self):
        logging.info("## Posting an Event")
        service = Services(self.driver)
        self.login()
        message_page=MessagePage(self.driver)
        message_page.nav_to_test_acc_msgs()
        initial_message_id=message_page.get_latest_message_id_no()
        logging.info("#number of messages: %s" %initial_message_id)
        event = EventPage(self.driver)
        event.post_as_free()
        posted_event_link = service.get_url()
        logging.info("event posted at %s" %posted_event_link)
        service.reset_page_and_nav_to_homepage()

    # click_RSVP_with_another_account

        logging.info("# Confirming RSVP with another account")
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login("asdfghjk@asdf.ghj", "asdfghjk")
        atg_login_page.validate_user_on_homepage()
        postpage=PostPage(self.driver)
        postpage.open_post_page_and_click_rsvp_yes(posted_event_link)
        service.reset_page_and_nav_to_homepage()

    # check_if_message_recieved

        logging.info("# verifying if message received")
        self.login()
        message_page.nav_to_test_acc_msgs()
        final_message_id=message_page.get_latest_message_id_no()
        assert (final_message_id > initial_message_id )\
            ,"Message not received"
