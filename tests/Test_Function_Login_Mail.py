# Fixture to initialize the WebDriver instance

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Test_Otp import fetch_otp_from_email
import time  # Add this line to import the time module

from utilities.BaseClass import BaseClass
# Test case to log in with email and OTP


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_with_email_and_otp(self):

        print("Test started: Logging in with email and OTP")

        # Wait for the loader overlay to disappear
        print("Waiting for the loader overlay to disappear...")
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-overlay'))
        )

        # Find and click on the login icon
        print("Clicking on the login icon...")
        login_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#page > div.navbar__wrapper > nav.navbar.navbar__main > div > ul > li:nth-child(4)")))
        login_icon.click()

        # Wait for the login modal to appear
        print("Waiting for the login modal to appear...")
        login_modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="Signin_modal"]/div/div')))

        # Find and click on the mail button
        print("Clicking on the mail button...")
        mail_button = WebDriverWait(login_modal, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Signin_modal"]/div/div/div[3]/div[2]/button[2]')))
        mail_button.click()

        # Wait for the email modal to appear
        print("Waiting for the email modal to appear...")
        email_modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="Signin-email_modal"]/div/div')))

        # Find the email field and enter the email address
        print("Entering the email address...")
        email_field = WebDriverWait(email_modal, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="email_auth_second"]')))
        email_field.send_keys("yousef_sami2010@yahoo.com")

        # Switch to the iframe
        print("Switching to the iframe...")
        iframe = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="signinemail-form-new"]/div[2]/div/div/div/iframe')))
        self.driver.switch_to.frame(iframe)

        # Wait for the reCAPTCHA checkbox
        print("Waiting for the reCAPTCHA checkbox...")
        recaptcha_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')))

        # Introduce a delay of 2 seconds (adjust the duration as needed)
        print("Introducing delay before clicking reCAPTCHA...")
        time.sleep(8)

        # Click on the reCAPTCHA checkbox
        recaptcha_checkbox.click()

        # Switch back to the default content (outside the iframe)
        print("Switching back to default content...")
        self.driver.switch_to.default_content()

        # Find and click on the login button
        print("Clicking on the login button...")
        login_button = WebDriverWait(email_modal, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Signin-email_modal"]/div/div/div[3]/button')))
        time.sleep(8)

        login_button.click()

        # Perform actions to trigger OTP (e.g., submit login form)
        # ...
        time.sleep(10)

        # Retrieve OTP from email
        print("Fetching OTP from email...")
        otp = fetch_otp_from_email()

        # Wait for the OTP field to become visible
        print("Waiting for the OTP field...")
        otp_field = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="otpEmail"]')))
        otp_field.send_keys(otp)

        # Submit the OTP form
        print("Submitting OTP...")
        otp_submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="submitEmailOtp"]')))
        otp_submit_button.click()

        # Wait for the unique element on the home page
        print("Waiting for the unique element on the home page...")
        unique_element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#splide05 > div.splide__arrows.splide__arrows--ltr > button.splide__arrow.splide__arrow--prev')))

        # Assert that the unique element is present, indicating the user is on the home page
        assert unique_element is not None, "User is not on the home page after successful login"

        # Optionally, you can print a message indicating the successful verification
        print("Verified that the user is on the home page after successful login")
