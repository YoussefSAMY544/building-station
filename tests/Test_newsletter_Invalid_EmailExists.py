import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generate_mail import generate_random_email
@pytest.mark.usefixtures("setup")
class TestNewsletter:
    def test_subscribe_newsletter_invalid_emailExists(self):
        try:
            # Use the same email that was previously signed up
            existing_email = "yousef_sami2010@yahoo.com"  # Replace with the existing email
            print("Finding the email field...")
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="userEmail"]'))
            )
            print(f"Entering email: {existing_email}")
            email_field.send_keys(existing_email)

            # Scroll the subscribe button into view
            print("Scrolling the subscribe button into view...")
            subscribe_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '#subscribeUser'))
            )
            # Scroll to the element to ensure it is fully visible
            self.driver.execute_script("arguments[0].scrollIntoView(true);", subscribe_button)

            # Add a brief wait time for stability
            time.sleep(1)

            # Click the subscribe button
            print("Clicking the subscribe button...")
            subscribe_button.click()


            print("Waiting for the error message...")
            # Wait for the error message to be displayed
            error_message = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div > div.toast-message'))
            )

            # Assert that the correct error message is displayed
            assert error_message.text == "Email already exist", "Expected error message not displayed"

            print("Invalid subscription attempt successful!")
            print(error_message.text)

        except Exception as e:
            pytest.fail(f"An error occurred: {str(e)}")
