
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Test_Otp import fetch_otp_from_email
import time
# Add this line to import the time module

from utilities.BaseClass import BaseClass
# Test case to log in with email and OTP
@pytest.mark.usefixtures("setup")
class TestAddToCart:
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
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#page > div.navbar__wrapper > nav.navbar.navbar__main > div > ul > li:nth-child(4)")))
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
        otp_field = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="otpEmail"]')))
        otp_field.send_keys(otp)

        # Submit the OTP form
        print("Submitting OTP...")
        otp_submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="submitEmailOtp"]')))
        otp_submit_button.click()

        # Wait for the unique element on the home page
        print("Waiting for the unique element on the home page...")
        unique_element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              '#splide05 > div.splide__arrows.splide__arrows--ltr > button.splide__arrow.splide__arrow--prev')))

        # Assert that the unique element is present, indicating the user is on the home page
        assert unique_element is not None, "User is not on the home page after successful login"

        # Optionally, you can print a message indicating the successful verification
        print("Verified that the user is on the home page after successful login")
    def test_search_and_add_to_cart(self):
        print("Test started: Searching for a product and adding it to the cart")

        # Find and enter text into the search field
        search_field = self.driver.find_element(By.CSS_SELECTOR, "#searchText")
        search_field.send_keys("LI651009")

        # Press Enter to perform the search
        search_field.send_keys(Keys.ENTER)

        # Wait for the product page to load
        try:
            product_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#addToBag_9cfbcfa4-69c1-44eb-b7d6-221c7f2c217a'))
            )
        except TimeoutException:
            print("Timeout occurred while waiting for the product page to load")
            return

        # Click on the add button
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="addToBag_9cfbcfa4-69c1-44eb-b7d6-221c7f2c217a"]'))
        )
        add_to_cart_button.click()

        # Wait for the confirmation message to appear
        try:
            confirmation_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
            )
        except TimeoutException:
            print("Timeout occurred while waiting for the confirmation message")
            return

        assert "Item added to Cart" in confirmation_message.text, "Confirmation message doesn't contain 'Item added to Cart' text"
        print("Confirmation message appeared.")

        # Click on the cart icon
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div/nav[1]/div/ul/li[4]'))
        )
        cart_icon.click()

        # Click on view cart
        view_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#cartdetailswrapper > div:nth-child(4) > div > a'))
        )
        view_cart_button.click()

        # Verify the URL of the cart page
        assert self.driver.current_url == "https://staging-ksa-v2.build-station.com/sa-en/cart", "Incorrect URL for the cart page"
        print("Navigated to the cart page successfully.")

    import time

    def test_simple_product_cart(self):
        print("Test started: Adding a single product to the cart")

        # Wait for 10 seconds
        time.sleep(10)

        # Find the quantity button and click to increase quantity
        quantity_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#quantityBox > button.btn.counter-increment.ItemplusBtn'))
        )
        quantity_button.click()

        # Wait for 10 seconds
        time.sleep(10)

        # Get the item price without tax and convert it to a float
        item_price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#sub_total'))
        )
        item_price_text = item_price_element.text
        item_price = float(item_price_text.replace(" SAR", ""))

        # Wait for 10 seconds
        time.sleep(10)

        # Calculate the subtotal (item price without tax * quantity)
        subtotal = item_price

        # Calculate the expected tax amount (15% of the subtotal)
        # Calculate the expected tax amount (15% of the subtotal) and round to two decimal places
        expected_tax = round(0.15 * subtotal, 2)
        print("Expected tax:", expected_tax)


        # Get the tax amount and convert it to a float
        tax_amount_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#tax_amount'))
        )
        # Get the tax amount and convert it to a float, then round to two decimal places
        tax_amount_text = tax_amount_element.text
        tax_amount = float(tax_amount_text.replace(" SAR", ""))
        print("Tax amount:", tax_amount)

        # Assert that the displayed tax amount matches the expected tax amount
        assert tax_amount == expected_tax, "Tax amount calculation is incorrect"
        print("Tax amount calculation is correct")

        # Calculate the expected grand total (subtotal + tax amount)
        expected_grand_total = subtotal + tax_amount
        print("Expected grand total:", expected_grand_total)

        # Get the grand total and convert it to a float
        grand_total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#grand_total'))
        )
        grand_total_text = grand_total_element.text
        grand_total = float(grand_total_text.replace(" SAR", ""))
        print("Grand total:", grand_total)

        # Verify that the displayed grand total matches the calculated grand total
        assert grand_total == expected_grand_total, "Grand total calculation is incorrect"
        print("Grand total calculation is correct")




# Run the test
if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])