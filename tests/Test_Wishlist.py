
from selenium.webdriver import ActionChains
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Test_Otp import fetch_otp_from_email
import time
@pytest.mark.usefixtures("setup")
class TestWishlist:
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
                EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[3]/a')))
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
                EC.visibility_of_element_located(
                    (By.XPATH, '//*[@id="signinemail-form-new"]/div[2]/div/div/div/iframe')))
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

        def test_add_to_wishlist(self):
            print("Test started: Adding item to wishlist")

            # Wait for the element to be present in the DOM
            print("Waiting for the wishlist icon to be present...")
            wishlist_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        '#splide06-slide05 > article > div.buttonGroup > button.whishList.mark-favourite'))
            )

            # Use Action Chains to move to the element and click it
            print("Moving to wishlist icon and clicking...")
            actions = ActionChains(self.driver)
            actions.move_to_element(wishlist_icon).click().perform()

            # Wait for the confirmation message to be visible
            print("Waiting for the confirmation message...")
            confirmation_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'div.toast.toast-success[style*="display: block;"] > div.toast-message'))
            )

            # Assertion for confirmation message
            assert confirmation_message.text == "Product added to your wishlist.", "Failed to add item to wishlist"

            print("Item added to wishlist successfully")

            # Get product information
            product_name, product_sku = self.get_product_info()

            # Print product information
            print("Product Name:", product_name)
            print("Product SKU:", product_sku)

            # Navigate to the wish list page
            Profile_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="page"]/div[2]/nav[1]/div/ul/li[3]/a'))
            )

            actions = ActionChains(self.driver)
            actions.move_to_element(Profile_icon).click().perform()

            time.sleep(5)

            Wish_List_Ico = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,
                                            '#page > main > section > div > div > div.col-md-3.profile__menu > ul > li:nth-child(5)')))
            Wish_List_Ico.click()



            # Assert that the product is in the wishlist
            # Assert that the product is in the wishlist
            wishlist_product_info = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '/html/body/div[2]/main/section/div/div/div[2]/section/div/div/div/div[5]/div/div[2]/div/div[1]/div/div')
                )).text

            # Split the wishlist product info into product name and SKU
            wishlist_product_name, wishlist_product_sku = wishlist_product_info.split(" - ")

            # Assert product name and SKU
            assert product_name == wishlist_product_name.strip(), f"Product name in wishlist ({wishlist_product_name}) does not match added product name ({product_name})"
            assert product_sku == wishlist_product_sku.strip(), f"Product SKU in wishlist ({wishlist_product_sku}) does not match added product SKU ({product_sku})"

        def get_product_info(self):
            # Navigate to the product page
            product_page_url = "https://staging-ksa-v2.build-station.com/sa-en/product/light_switch_2_gang_1_way_glossy_grey?category=glossy_grey"
            self.driver.get(product_page_url)

            # Wait for the product name and SKU elements to be present
            product_name_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '#page > main > section.product__information > div > div:nth-child(2) > div.col-md-6.mt-5.mt-md-0 > div.product__summary > h1'))
            )
            product_sku_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'item_code'))
            )

            # Extract the text of the product name and SKU elements
            product_name = product_name_element.text
            product_sku = product_sku_element.text

            return product_name, product_sku




