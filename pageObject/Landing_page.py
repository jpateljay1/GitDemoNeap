from selenium.webdriver.common.by import By
import logger
import logging

class Landing_page:
    LP_GI_NEAP_logo_xpath = "(//img)[3]" # NEAP logo
    LP_Welcome_text_xpath = "/html[1]/body[1]/div[1]/div[3]/section[2]/div[1]/div[2]/p[1]" # Welcome text " Welcome!Login to your account"
    LP_GI_global_ID_tag_CSS = "span[for='userId']" # Global ID tag text
    LP_GI_global_ID_input_field_CSS = "#userId" # Global ID input field
    LP_GI_termandConditions_text_xpath = "//div[@class='sc-zzdIa derPWs']" # Termand condition and privacy policy text
    LP_GI_term_and_condition_hyperlink_xpath = "//span[normalize-space()='Terms & Conditions']" # term and condition hyper link button
    LP_GI_privacy_policy_hyperlink_xpath = "//span[normalize-space()='Privacy Policy']" # Privacy policy hyper link button
    LP_GI_proceed_CTA_CSS = "button[type='submit']" # Proceed CTA
    LP_carousel_progress_bar_one_xpath = "//body[1]/div[1]/div[3]/section[1]/div[1]/div[4]/div[2]/div[1]/div[1]/span[1]/span[1]" # Carousel progress bar one
    LP_carousel_progress_bar_two_xpath = "//body[1]/div[1]/div[3]/section[1]/div[1]/div[4]/div[2]/div[1]/div[2]/span[1]/span[1]" # Carousel progress bar two
    LP_carousel_progress_bar_three_xpath = "//body[1]/div[1]/div[3]/section[1]/div[1]/div[4]/div[2]/div[1]/div[3]/span[1]/span[1]" # Carousel progress bar three
    LP_carousel_images_xpath = "//section[@class='left']//div[contains(@style,'background-image')]" # carousel images


# OTP Section
    LP_OTP_header_xpath = "//div[@class='sc-kpXpMQ gJZzxf']" # OTP Verification header text
    LP_OTP_description_text_xpath = "//div[@class='sc-czgevV giohnb']" # After OTP verification header description text
    LP_OTP_entered_global_id_in_description_text_xpath = "//span[@class='id']" # In the description text, entered global ID text
    LP_not_your_ID_btn_xpath = "//button[normalize-space()='Not your ID?']" # Not your ID button Text
    LP_OTP_tag_xpath = "//span[@class='sc-bQVmPH cROQXQ']" # Enter OTP Tag
    LP_OTP_fild_xpath = "//input[@type='password']" # OTP digit Field all four
    LP_OTP_error_text_xpath = "/html/body/div[1]/div[3]/section[2]/div/form/div/div[2]/span[2]" # Invalid otp error text xpath
    LP_OTP_resend_button_xpath = "//button[normalize-space()='Resend']" # OTP Resend button xpath
    LP_OTP_login_CTA_xpath = "//button[normalize-space()='Login']" # Login CTA


    def __init__(self, driver):  # initialize the driver & locators
        self.driver = driver
        self.log = logging.getLogger(__name__)

    # Actions methods for each Locator

    def neap_logo_is_displayed(self): # Neap logo display method
        neap_logo = self.driver.find_element(By.XPATH, self.LP_GI_NEAP_logo_xpath)
        if neap_logo.is_displayed():
            print("✅ NEAP Logo is displayed")
            self.log.info("NEAP Logo is displayed")
            return True
        else:
            print("❌ NEAP logo is not displayed")
            self.log.info("NEAP Logo is not displayed")
            return False

    # Welcome text display and text verification
    def welcome_text_is_displayed(self):
        welcome_text = self.driver.find_element(By.XPATH, self.LP_Welcome_text_xpath)
        actual_welcome_text = welcome_text.text
        expected_welcome_text = "Welcome!login to your account"
        if welcome_text.is_displayed():
            print("✅ Welcome text is displayed" + actual_welcome_text)
            self.log.info("Welcome text is displayed" + actual_welcome_text)
            if actual_welcome_text == expected_welcome_text:
                print("✅ Expected text is displayed for the Welcome text as " + actual_welcome_text)
                self.log.info("Expected text is displayed for the Welcome text as " + actual_welcome_text)
                return True
            else:
                print("❌ Expected text is not displayed for the Welcome text as " + actual_welcome_text)
                self.log.info("Expected text is not displayed for the Welcome text as " + actual_welcome_text)
                return False
        else:
            print("❌ Welcome text is not displayed" + actual_welcome_text)
            self.log.info("Welcome text is not displayed" + actual_welcome_text)
            return False

    # Global ID tag display
    def global_id_tag_is_displayed(self):
        global_id_tag = self.driver.find_element(By.CSS_SELECTOR, self.LP_GI_global_ID_tag_CSS)
        if global_id_tag.is_displayed():
            print("✅ Global ID tag text is displayed: " + global_id_tag.text)
            self.log.info("Global ID tag text is displayed: " + global_id_tag.text)
            return True
        else:
            print("❌ Global ID tag text is not displayed")
            self.log.info("Global ID tag text is not displayed")
            return False

    # Enter global iD field display
    def enter_global_id_field_is_displayed(self):
        input_field = self.driver.find_element(By.CSS_SELECTOR, self.LP_GI_global_ID_input_field_CSS)
        if input_field.is_displayed():
            print("✅ Global ID text field is displayed ")
            self.log.info("Global ID text field is displayed  ")
            return True
        else:
            print("❌ Global ID text field is not displayed ")
            self.log.info("Global ID text field is not displayed ")
            return False

    # Enter global iD
    def enter_global_id(self, user_id):
        input_field = self.driver.find_element(By.CSS_SELECTOR, self.LP_GI_global_ID_input_field_CSS)
        assert input_field.is_enabled(), "❌ Global ID input field is NOT enabled!"
        input_field.clear()
        input_field.send_keys(user_id)
        print("Entered Global ID: " + user_id)
        self.log.info("Entered Global ID: " + user_id)

    # Terms and condition text is displayed
    def terms_and_conditions_text_is_displayed(self):
        terms_text = self.driver.find_element(By.XPATH, self.LP_GI_termandConditions_text_xpath)
        if terms_text.is_displayed():
            print("Terms and Conditions / Privacy Policy text is displayed: " + terms_text.text)
            self.log.info("Terms and Conditions / Privacy Policy text is displayed: " + terms_text.text)
            return True
        else:
            print("❌ Terms and Conditions / Privacy Policy text is not displayed")
            self.log.info("Terms and Conditions / Privacy Policy text is not displayed")
            return False

    # Click on term and condition hyperlink
    def click_terms_and_conditions_link(self):
        tnc_link = self.driver.find_element(By.XPATH, self.LP_GI_term_and_condition_hyperlink_xpath)
        if tnc_link.is_displayed() and tnc_link.is_enabled():
            tnc_link.click()
            print("✅ Clicked on Terms & Conditions link")
            self.log.info("Clicked on Terms & Conditions link")
            return True
        else:
            print("❌ Terms & Conditions link is NOT clickable")
            self.log.error("Terms & Conditions link is NOT clickable")
            return False

    # Click on Privacy policy hyperlink
    def click_privacy_policy_link(self):
        privacy_link = self.driver.find_element(By.XPATH, self.LP_GI_privacy_policy_hyperlink_xpath)
        if privacy_link.is_displayed() and privacy_link.is_enabled():
            privacy_link.click()
            print("✅ Clicked on Privacy Policy link")
            self.log.info("Clicked on Privacy Policy link")
            return True
        else:
            print("❌ Privacy Policy link is NOT clickable")
            self.log.error("Privacy Policy link is NOT clickable")
            return False

# Proceed button display method
    def proceed_button_is_displayed(self):
        proceed_button = self.driver.find_element(By.CSS_SELECTOR, self.LP_GI_proceed_CTA_CSS)
        if proceed_button.is_displayed():
            print("✅ Proceed CTA button is displayed")
            self.log.info("Proceed CTA button is displayed")
            return True
        else:
            print("❌ Proceed CTA button is NOT displayed")
            self.log.error("Proceed CTA button is NOT displayed")
            return False

# Proceed button enable status on global ID section
    def proceed_button_is_enabled(self):
        proceed_button = self.driver.find_element(By.CSS_SELECTOR, self.LP_GI_proceed_CTA_CSS)
        assert proceed_button.is_enabled(), "❌ Proceed CTA button is NOT enabled!"
        print("✅ Proceed CTA button is enabled")
        self.log.info("Proceed CTA button is enabled")
        return True

# Proceed CTA shown on Global ID section
    def proceed_button_is_disabled(self):
        proceed_button = self.driver.find_element(By.CSS_SELECTOR, self.LP_GI_proceed_CTA_CSS)
        assert not proceed_button.is_enabled(), "❌ Proceed CTA button is ENABLED, but expected DISABLED!"
        print("✅ Proceed CTA button is disabled")
        self.log.info("Proceed CTA button is disabled")
        return True

# click action on proceed CTA on global id section
    def click_proceed_button(self):
        # First verify displayed and enabled before clicking
        self.proceed_button_is_enabled()

        proceed_button = self.driver.find_element(By.CSS_SELECTOR, self.LP_GI_proceed_CTA_CSS)
        proceed_button.click()
        print("✅ Clicked on Proceed CTA")
        self.log.info("Clicked on Proceed CTA")

    # OTP Page Methods

    def otp_header_is_displayed(self):
        otp_header = self.driver.find_element(By.XPATH, self.LP_OTP_header_xpath)
        actual_otp_header_text = otp_header.text
        expected_otp_header_text = "OTP Verification"
        if otp_header.is_displayed():
            print("✅ OTP Verification header is displayed: " + otp_header.text)
            self.log.info("OTP Verification header is displayed: " + otp_header.text)

            if actual_otp_header_text == expected_otp_header_text:
                print("✅ OTP Verification header text is displayed as expected: " + otp_header.text)
                self.log.info("OTP Verification header text is displayed as expected:" + otp_header.text)
                return True
            else:
                print("✅ OTP Verification header text is not displayed as expected: " + otp_header.text)
                self.log.info("OTP Verification header text is not displayed as expected:" + otp_header.text)
                return False
        else:
            print("❌ OTP Verification header is NOT displayed")
            self.log.error("OTP Verification header is NOT displayed")
            return False

# OTP description text is displayed
    def otp_description_text_is_displayed(self):
        otp_description = self.driver.find_element(By.XPATH, self.LP_OTP_description_text_xpath)
        if otp_description.is_displayed():
            print("✅ OTP Verification description text is displayed: " + otp_description.text)
            self.log.info("OTP Verification description text is displayed: " + otp_description.text)
            return otp_description.text
        else:
            print("❌ OTP Verification description text is NOT displayed")
            self.log.error("OTP Verification description text is NOT displayed")
            return False

# Enter Otp description text is displayed
    def otp_entered_global_id_in_description_text_is_displayed(self):
        otp_global_id = self.driver.find_element(By.XPATH, self.LP_OTP_entered_global_id_in_description_text_xpath)
        if otp_global_id.is_displayed():
            print("✅ Entered Global ID is displayed: " + otp_global_id.text)
            self.log.info("Entered Global ID is displayed: " + otp_global_id.text)
            return otp_global_id.text
        else:
            print("❌ Entered Global ID is NOT displayed")
            self.log.error("Entered Global ID is NOT displayed")
            return False

# Masked phone number displayed
    def otp_masked_phone_number_is_displayed(self):
        otp_masked_phone = self.driver.find_element(By.XPATH, self.LP_OTP_masked_phone_number_xpath)
        if otp_masked_phone.is_displayed():
            print("✅ Masked phone number is displayed: " + otp_masked_phone.text)
            self.log.info("Masked phone number is displayed: " + otp_masked_phone.text)
            return otp_masked_phone.text
        else:
            print("❌ Masked phone number is NOT displayed")
            self.log.error("Masked phone number is NOT displayed")
            return False

#  Not your ID button is displayed
    def not_your_id_button_is_displayed(self):
        not_id_btn = self.driver.find_element(By.XPATH, self.LP_not_your_ID_btn_xpath)
        if not_id_btn.is_displayed():
            print("✅ 'Not your ID?' button is displayed")
            self.log.info("'Not your ID?' button is displayed")
            return True
        else:
            print("❌ 'Not your ID?' button is NOT displayed")
            self.log.error("'Not your ID?' button is NOT displayed")
            return False

# Click action on Not your ID button
    def click_not_your_id_button(self):
        not_id_btn = self.driver.find_element(By.XPATH, self.LP_not_your_ID_btn_xpath)
        if not_id_btn.is_displayed() and not_id_btn.is_enabled():
            not_id_btn.click()
            print("✅ Clicked on 'Not your ID?' button")
            self.log.info("Clicked on 'Not your ID?' button")
            return True
        else:
            print("❌ 'Not your ID?' button is NOT clickable")
            self.log.error("'Not your ID?' button is NOT clickable")
            return False

# OTP tag display method
    def otp_tag_is_displayed(self):
        otp_tag = self.driver.find_element(By.XPATH, self.LP_OTP_tag_xpath)
        actual_otp_tag_text = otp_tag.text
        expected_otp_tag_text = "Enter OTP"
        if otp_tag.is_displayed():
            if actual_otp_tag_text == expected_otp_tag_text:
                print("✅ OTP Tag text is displayed as expected:" + otp_tag.text)
                self.log.info("✅ OTP Tag text is displayed as expected:" + otp_tag.text)
                return otp_tag.text
            else:
                print("❌ OTP Tag text is not displayed as expected: " + otp_tag.text)
                self.log.info("OTP Tag text is not displayed as expected: " + otp_tag.text)
                return False
        else:
            print("❌ OTP Tag is NOT displayed")
            self.log.error("OTP Tag is NOT displayed")
            return False

    # entering otp digits in single method
    def enter_otp_digits(self, otp_digits):
        otp_inputs = self.driver.find_elements(By.XPATH,self.LP_OTP_fild_xpath )

        # Verify OTP input boxes are present
        if len(otp_inputs) == 0:
            print("❌ No OTP input fields found on the page")
            self.log.error("No OTP input fields found on the page")
            assert False, "OTP input fields are not available"

        if len(otp_inputs) < len(otp_digits):
            print(f"❌ Not enough OTP input boxes. Found {len(otp_inputs)}, expected {len(otp_digits)}")
            self.log.error(f"Not enough OTP input boxes. Found {len(otp_inputs)}, expected {len(otp_digits)}")
            assert False, "OTP input field count mismatch"

        # Enter OTP
        for box, digit in zip(otp_inputs, otp_digits):
            if box.is_displayed() and box.is_enabled():
                box.clear()
                box.send_keys(digit)
                print(f"✅ Entered digit: {digit}")
                self.log.info(f"Entered digit: {digit}")
            else:
                print(f"❌ OTP input box for digit '{digit}' is not interactable")
                self.log.error(f"OTP input box for digit '{digit}' is not interactable")
                assert False, f"OTP input box for digit '{digit}' is not interactable"

        print("✅ Successfully entered OTP")
        self.log.info("Successfully entered OTP")

    def invalid_otp_error_text(self):
        otp_error = self.driver.find_element(By.XPATH, self.LP_OTP_error_text_xpath)
        actual_otp_error_text = otp_error.text
        expected_otp_error_text = "OTP invalid! Please enter correct OTP."
        if otp_error.is_displayed():
            print("✅ OTP error text is displayed")
            self.log.info("OTP error text is displayed")
            if actual_otp_error_text == expected_otp_error_text:
                print("Invalid OTP error text is as expected: " + actual_otp_error_text)
                self.log.info("Invalid OTP error text is as expected: " + actual_otp_error_text)
                return True
            else:
                print("Invalid OTP error text is not as expected: " + actual_otp_error_text)
                self.log.info("Invalid OTP error text is not as expected: " + actual_otp_error_text)
                return False
        else:
            print("❌ OTP error text is NOT displayed")
            self.log.error("OTP error text is NOT displayed")
            return False

    # OTP Resend Button Methods
    def otp_resend_button_is_displayed(self):
        resend_btn = self.driver.find_element(By.XPATH, self.LP_OTP_resend_button_xpath)
        if resend_btn.is_displayed():
            print("✅ OTP Resend button is displayed")
            self.log.info("OTP Resend button is displayed")
            return True
        else:
            print("❌ OTP Resend button is NOT displayed")
            self.log.error("OTP Resend button is NOT displayed")
            return False

    # Otp resend button click
    def click_otp_resend_button(self):
        resend_btn = self.driver.find_element(By.XPATH, self.LP_OTP_resend_button_xpath)
        if resend_btn.is_displayed() and resend_btn.is_enabled():
            resend_btn.click()
            print("✅ Clicked on OTP Resend button")
            self.log.info("Clicked on OTP Resend button")
            return True
        else:
            print("❌ OTP Resend button is NOT clickable")
            self.log.error("OTP Resend button is NOT clickable")
            return False

    # OTP Login CTA Methods
    def otp_login_cta_is_displayed(self):
        login_cta = self.driver.find_element(By.XPATH, self.LP_OTP_login_CTA_xpath)
        if login_cta.is_displayed():
            print("✅ OTP Login CTA is displayed")
            self.log.info("OTP Login CTA is displayed")
            return True
        else:
            print("❌ OTP Login CTA is NOT displayed")
            self.log.error("OTP Login CTA is NOT displayed")
            return False

    # click on login button
    def click_otp_login_cta(self):
        login_cta = self.driver.find_element(By.XPATH, self.LP_OTP_login_CTA_xpath)
        if login_cta.is_displayed() and login_cta.is_enabled():
            login_cta.click()
            print("✅ Clicked on OTP Login CTA")
            self.log.info("Clicked on OTP Login CTA")
            return True
        else:
            print("❌ OTP Login CTA is NOT clickable")
            self.log.error("OTP Login CTA is NOT clickable")
            return False

    # Carousel images displayed
    def carousel_images_is_displayed(self):
        images = self.driver.find_elements(By.XPATH, self.LP_carousel_images_xpath)
        if len(images) > 0:
            print(f"✅ Found {len(images)} carousel images")
            self.log.info(f"Found {len(images)} carousel images")
            return True
        else:
            print("❌ No carousel images found")
            self.log.error("No carousel images found")
            return False

 # active carousel image
    def verify_active_carousel_image(self):
        images = self.driver.find_elements(By.XPATH, self.LP_carousel_images_xpath)
        active_found = False

        for idx, img in enumerate(images, start=1):
            style = img.get_attribute("style")
            if "opacity: 1" in style:
                print(f"✅ Carousel Image {idx} is active")
                self.log.info(f"Carousel Image {idx} is active")
                active_found = True
                break

        if not active_found:
            print("❌ No active carousel image found")
            self.log.error("No active carousel image found")
            return False