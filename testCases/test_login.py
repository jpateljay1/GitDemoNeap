import time

from Utilities.ReadProperties import ReadConfig
from pageObject.Landing_page import Landing_page
import pytest
from Utilities.BaseClass import BaseClass
import logging


@pytest.mark.usefixtures("setup")
class TestLogin(BaseClass):  # Inherit BaseClass
    baseURL = ReadConfig.getApplicationUrl()
    path = "/Users/jaypatel/PycharmProjects/NEAP Demo/TestData/NEAPusercredentials.xlsx"
    sheetName = "NEAPCredentials"

    def setup_method(self, method):  # will run before each test
        self.log = logging.getLogger(__name__)

    # CASE ID: 258946, Verify that user should launch the NEAP website portal.
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_launch_neap_website(self, setup):
        self.driver = setup
        self.log.info("Browser launched successfully")
        self.driver.get(self.baseURL)  # Open Base URL
        time.sleep(3)
        self.log.info(f"Opened the NEAP website: {self.baseURL}")
        self.log.info("Case ID: 258946, Successfully launched the NEAP website")

    # CASE ID: 258947, Verify that user should land on the Login page after launching the website.
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_launch_neap_website_and_land_on_login_page(self, setup):
        self.driver = setup
        self.log.info("Browser launched successfully")
        self.driver.get(self.baseURL)  # Open Base URL
        time.sleep(3)
        self.log.info(f"Opened the NEAP website: {self.baseURL}")
        LP = Landing_page(self.driver)
        LP.carousel_images_is_displayed()
        print("Case ID: 258947, Successfully launched the NEAP website and login page is shown")
        self.log.info("Case ID: 258947, Successfully launched the NEAP website and login page is shown")

    # Case ID: 258949, Verify that user should login into the NEAT application with the registered organisation employee id.
    @pytest.mark.regression
    def test_UI_elements_on_landing_page(self, setup):
        self.driver = setup
        self.log.info("Browser launched successfully")
        self.driver.get(self.baseURL)  # Open Base URL
        time.sleep(3)
        lp = Landing_page(self.driver)
        assert lp.neap_logo_is_displayed(), "NEAP logo is not displayed"
        assert lp.welcome_text_is_displayed(), "Welcome text is not displayed correctly"
        assert lp.global_id_tag_is_displayed(), "Global Id tag is not shown"
        assert lp.enter_global_id_field_is_displayed(), "enter global id field is not displayed"
        assert lp.terms_and_conditions_text_is_displayed(), "Term and condition descriptive text is not displayed"
        assert lp.proceed_button_is_disabled(), "Proceed CTA is not displayed"

    # Case ID: 258949,  Verify that user should login into the NEAT application with the registered organisation employee id.
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_successful_login(self, setup):
        self.driver = setup
        self.log.info("Browser launched successfully")
        self.driver.get(self.baseURL)  # Open Base URL
        time.sleep(3)
        lp = Landing_page(self.driver)
        lp.enter_global_id('test12345')
        time.sleep(3)
        lp.click_proceed_button()
        time.sleep(3)
        lp.enter_otp_digits('1111')
        time.sleep(3)
        lp.click_otp_login_cta()

    # Verification on exam page is pending

    # Case ID: 258951, Verify that if user enter's the wrong OTP in the OTP input fields, "Invalid Code" text should be shown on the OTP verification page in a red colour.
    @pytest.mark.regression
    def test_invalid_otp_verification(self, setup):
        global_id = self.read_excel_data(self.path, self.sheetName, 2, 2)
        otp_value = str(self.read_excel_data(self.path, self.sheetName, 2, 3))

        self.driver = setup
        self.log.info("Browser launched successfully")
        self.driver.get(self.baseURL)  # Open Base URL
        time.sleep(3)
        lp = Landing_page(self.driver)
        lp.enter_global_id(global_id)
        time.sleep(3)
        lp.click_proceed_button()
        time.sleep(3)
        lp.enter_otp_digits(otp_value)
        time.sleep(3)
        lp.click_otp_login_cta()
        time.sleep(3)
        assert lp.invalid_otp_error_text()



