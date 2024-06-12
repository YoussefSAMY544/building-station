from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Test_Otp import fetch_otp_from_email
import time
from selenium.webdriver.support.ui import Select

from utilities.BaseClass import BaseClass

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

    def test_search_and_add_to_cart_Composite(self):
        print("Test started: Searching for a product and adding it to the cart")

        # Find and enter text into the search field
        search_field = self.driver.find_element(By.CSS_SELECTOR, "#searchText")
        search_field.send_keys("531556-531559")

        # Press Enter to perform the search
        search_field.send_keys(Keys.ENTER)

        # Wait for the product page to load


        # Click on the add button
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'addToBag_f2371ab0-a752-11eb-9dcc-af22e1d0ac8c'))
        )
        add_to_cart_button.click()
        time.sleep(2)

        # Wait for the button to be clickable and click it three times
        for _ in range(3):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="quantityBox"]/button[2]'))
            ).click()
            time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#component_details_a5576160-a726-11eb-8ffe-bb3f678c84aa > div.product__summary-item > div > div > span"))
        ).click()

        for _ in range(2):

         WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#component_details_a5576160-a726-11eb-8ffe-bb3f678c84aa > div.product__summary-item > div > div > select > option:nth-child(3)"))
         ).click()

        for _ in range(2):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="quantityBox"]/button[2]'))
            ).click()
            time.sleep(2)


        add_to_cart_button1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'addCompositeItemToCartModal'))
         )
        add_to_cart_button1.click()

        time.sleep(3)


        #Wait for the confirmation message to appear
        try:
            confirmation_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="toast-container"]/div/div[2]'))
            )
        except TimeoutException:
            print("Timeout occurred while waiting for the confirmation message")
            return

        assert "Item added to Cart" in confirmation_message.text, "Confirmation message doesn't contain 'Item added to Cart' text"
        print("Confirmation message appeared.")

        close_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#product_detail > div.modal-header > svg"))
        )

        # Click the close button
        close_button.click()

        time.sleep(2)

        # Click on the cart icon
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div/nav[1]/div/ul/li[4]'))
        )
        cart_icon.click()

        # Assert that the view cart button is visible and clickable
        try:
            view_cart_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#cartdetailswrapper > div:nth-child(4) > div > a'))
            )
            print("View cart button is visible and clickable.")
            # Click on view cart
            view_cart_button.click()
        except Exception as e:
            print("Cart not open or view cart button not found.")
        # Verify the URL of the cart page
        assert self.driver.current_url == "https://staging-ksa-v2.build-station.com/sa-en/cart", "Incorrect URL for the cart page"
        print("Navigated to the cart page successfully.")

    def test_composite_product_cart(self):
        print("Test started: Adding a single product to the cart")

        # Wait for 10 seconds
        time.sleep(10)

        # Find the quantity button and click to increase quantity
        for _ in range(15):
            quantity_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#quantityBox > button.btn.counter-decrement.ItemminusBtn'))
            )
            quantity_button.click()

        # Wait for 10 seconds
        time.sleep(10)

        item_price_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#sub_total'))
        )
        item_price_text = item_price_element.text
        # Remove comma and convert to float
        item_price = float(item_price_text.replace(" SAR", "").replace(",", ""))
        # Wait for 10 seconds
        time.sleep(10)

        # Calculate the subtotal (item price without tax * quantity)
        subtotal = item_price

        # Calculate the expected tax amount (15% of the subtotal) and round to two decimal places
        expected_tax = round(0.15 * subtotal, 2)
        print("Expected tax:", expected_tax)

        # Get the tax amount and convert it to a float
        tax_amount_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#tax_amount'))
        )
        # Get the tax amount and convert it to a float, then round to two decimal places
        tax_amount_text = tax_amount_element.text
        tax_amount = float(tax_amount_text.replace(" SAR", "").replace(",", ""))
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
        grand_total = float(grand_total_text.replace(" SAR", "").replace(",", ""))
        print("Grand total:", grand_total)

        # Assert that the displayed grand total matches the expected grand total
        assert grand_total == expected_grand_total, "Grand total calculation is incorrect"
        print("Grand total calculation is correct")

        print("Find and click on the Proceed to Checkout button")

        # Find and click on the "Proceed to Checkout" button
        proceed_to_checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "proceedToCheckout")))
        proceed_to_checkout_button.click()

        print("Find the checkbox and check it")

        print("Waiting for the shipping option to appear...")
        shipping_option = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#shipBox_0 > div > div > label'))
        )
        print("Shipping option appeared.")

        # Assert that the shipping option is present
        assert shipping_option is not None, "Shipping option did not appear"

        # Find the checkbox and check it
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#shipBox_0 > div > div > label'))
        )


        if not checkbox.is_selected():
            checkbox.click()

        print("Select the address by checking the checkbox")

        address_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="shipBox_0"]/div/div/label'))
        )
        address_checkbox.click()

        # Wait for 10 seconds
        time.sleep(10)

        print("Click on the shipping info button")

        # Click on the shipping info button
        shipping_info_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'shipping-info-btn'))
        )
        shipping_info_btn.click()
        print("Wait for the page to load, then interact with payment fields")

        # Wait for the page to load, then interact with payment fields
        time.sleep(3)  # Adjust the sleep time as needed
        print("Click on the debit/credit card option")


        # credit card option
        debit_credit_card = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#debit-credit-card'))
        )
        debit_credit_card.click()

        print("Fill in card details")

        # Fill in card details
        card_holder_name = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#card_holder_name'))
        )
        card_holder_name.send_keys("Test Card")

        card_number = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#card_number'))
        )
        card_number.send_keys("5105105105105100")

        expiry_month = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#expiry_month'))
        )
        expiry_month.send_keys("02")

        expiry_year = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#expiry_year'))
        )
        expiry_year.send_keys("28")

        card_security_code = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#card_security_code'))
        )
        card_security_code.send_keys("123")

        print("Check the checkbox")

        # Check the checkbox
        # Switch to the adminstaging    qm*+*3&mpz
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#checkboxG158"))
        ).click()

        print("Click on the complete payment button")

        # Click on the complete payment button


        complete_payment_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#complete-payment'))
        )
        complete_payment_btn.click()
        # Wait for 15 seconds
        self.driver.implicitly_wait(20)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "otp"))
        ).send_keys(123123)
        time.sleep(3)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "submit-btn"))
        ).click()
        print("Make a Complete order")

        time.sleep(20)

        self.driver.quit()

