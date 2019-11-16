from nose.plugins.attrib import attr


import logging
from utility.drivermanager import DriverManager
from utility.services import Services
from pages.ATG_login_page import ATGLoginPage
from pages.meetup_page import MeetupPage

@attr(website=['party', 'world'])
class PostPaidMeetupTest(DriverManager):
    def login(self):
        atg_login_page = ATGLoginPage(self.driver)
        atg_login_page.wait_for_homepage_to_load()
        atg_login_page.login()
        atg_login_page.validate_user_on_homepage()
    def test_post_a_single_ticket_paid_meetup(self):
        logging.info("## Posting an Event")
        service = Services(self.driver)
        self.login()
        meetup = MeetupPage(self.driver)
        meetup.post_as_paid_single_ticket()
        posted_meetup_link = service.get_url()
        logging.info("meetup posted at %s" %posted_meetup_link)

    def test_post_a_multi_ticket_paid_meetup(self):
        logging.info("## Posting an Event")
        service = Services(self.driver)
        self.login()
        meetup = MeetupPage(self.driver)
        meetup.post_as_paid_multi_ticket()
        posted_meetup_link = service.get_url()
        logging.info("meetup posted at %s" % posted_meetup_link)

