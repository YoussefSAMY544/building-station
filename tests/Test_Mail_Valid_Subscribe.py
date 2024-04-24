import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generate_mail import generate_random_email
@pytest.mark.usefixtures("setup")
class TestNewsletter:
    def test_subscribe_newsletter_Valid(self):
        try:
            # Generate a random email
            email = generate_random_email()

            # Find the email field and enter the generated email
            print("Finding the email field...")
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="userEmail"]'))
            )
            print(f"Entering email: {email}")
            email_field.send_keys(email)

            # Scroll the subscribe button into view
            # Scroll the subscribe button into view
            print("Scrolling the subscribe button into view...")
            subscribe_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '#subscribeUser'))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", subscribe_button)

            # Add a sleep to wait for stability
            time.sleep(2)  # Wait for 2 seconds

            # Click the subscribe button
            print("Clicking the subscribe button...")
            subscribe_button.click()

            print("Waiting for the confirmation message...")
            # Replace the existing line where you wait for the confirmation message
            confirmation_message = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '#toast-container > div > div.toast-message'))
            )

            assert confirmation_message.text == "Subscription successfully processed.", "Subscription was not successful"

            print("Subscription successful!")
            print(confirmation_message.text)

        except Exception as e:
            pytest.fail(f"An error occurred: {str(e)}")





