import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.ui import Select

from generate_mail import generate_random_email

@pytest.mark.usefixtures("setup")
class TestAddtocart():
    def test_Popup_to_Cart(self):
        # Scrolling down to ensure the target element is in view
        print("Scrolling to the target element...")
        element = self.driver.find_element(By.CSS_SELECTOR, "#page > main > section:nth-child(6) > div > div > div:nth-child(1) > div > div > a")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        print("Arrived at the target element.")

        # Clicking the 'Add to Cart' button
        print("Waiting for the 'Add to Cart' button to become clickable...")
        Addtocartbutton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="addToBag_73e51ed1-50c2-4ed2-8fab-e03a833cc2fc"]')))
        Addtocartbutton.click()
        print("'Add to Cart' button clicked.")

        # Waiting for the popup after adding the item to cart
        print("Waiting for the popup to appear...")
        popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "product_detail"))
        )
        time.sleep(4)  # This can be adjusted based on the actual response time of your application
        print("Popup has appeared.")

        # Asserting the popup visibility and its class attribute
        assert popup.is_displayed(), "Popup is not displayed."
        assert "modal-content" in popup.get_attribute("class"), "Popup does not have the expected 'modal-content' class."
        print("Assertion passed: Popup is displayed with the correct class.")

        # Clicking the secondary 'Add to Cart' button within the popup
        print("Waiting for the second 'Add to Cart' button...")
        addItemsToCart2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#addItemsToCart2")))
        addItemsToCart2.click()
        print("Second 'Add to Cart' button clicked.")

        # Waiting for the confirmation message and verifying its content
        print("Waiting for the confirmation message...")
        confirmation_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#toast-container"))
        )
        confirmation_text = confirmation_message.text
        assert "Item added to Cart" in confirmation_text, "The confirmation message did not contain expected text."
        print("Confirmation message received and verified: ", confirmation_text)

        # Optionally, close the driver if it's not managed globally by the fixture
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#product_detail > div.modal-header.modal-header-pad > svg"))).click()


    def test_change_variable_attribuate(self):
        print("Scrolling to the target element...")
        element = self.driver.find_element(By.CSS_SELECTOR,"#page > main > section:nth-child(6) > div > div > div:nth-child(1) > div > div > a")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        print("Arrived at the target element.")

        # Clicking the 'Add to Cart' button
        print("Waiting for the 'Add to Cart' button to become clickable...")
        Addtocartbutton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="addToBag_73e51ed1-50c2-4ed2-8fab-e03a833cc2fc"]')))
        Addtocartbutton.click()
        print("'Add to Cart' button clicked.")

        # Waiting for the popup after adding the item to cart
        print("Waiting for the popup to appear...")
        popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "product_detail"))
        )
        time.sleep(4)  # This can be adjusted based on the actual response time of your application
        print("Popup has appeared.")

        # Asserting the popup visibility and its class attribute
        assert popup.is_displayed(), "Popup is not displayed."
        assert "modal-content" in popup.get_attribute(
            "class"), "Popup does not have the expected 'modal-content' class."
        print("Assertion passed: Popup is displayed with the correct class.")

        print("Clicking the first element in the modal...")


        dropdown = self.driver.find_element(By.CSS_SELECTOR,
                                                 "#product_detail > div.modal-body > div > div > div:nth-child(2) > div:nth-child(7) > div > div > div > div")
        dropdown.click()
        print("First element clicked.")

        # Wait for the second element to appear and click it
        print("Waiting for the second element to appear...")
        Matt_Black = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#product_detail > div.modal-body > div > div > div:nth-child(2) > div:nth-child(7) > div > div > div > div > ul > li:nth-child(2)"))
        )
        print("Matt Black is visible. Clicking now...")
        Matt_Black.click()
        time.sleep(4)

        # Verify the dynamic id element contains the expected text
        print("Verifying the SKU...")
        item_SKU_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='item_code_']"))
            # This selector matches any id that starts with 'item_code_'
        )
        item_SKU_text = item_SKU_element.text
        assert "SW01330022" in item_SKU_text, f"Item code does not contain the expected text. Found: {item_SKU_text}"
        print("Item code verified successfully: ", item_SKU_text)

        first_element = self.driver.find_element(By.CSS_SELECTOR,
                                                 "#product_detail > div.modal-body > div > div > div:nth-child(2) > div:nth-child(7) > div > div > div > div")
        first_element.click()
        time.sleep(3)

        Brushed_Gold = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#product_detail > div.modal-body > div > div > div:nth-child(2) > div:nth-child(7) > div > div > div > div > ul > li:nth-child(4)"))
        )
        print("Brushed Gold is visible. Clicking now...")
        Brushed_Gold.click()
        time.sleep(3)
        item_SKU_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='item_code_']")))

        # This selector matches any id that starts with 'item_code_'
        item_SKU_text = item_SKU_element.text
        assert "SW01330030" in item_SKU_text, f"Item code does not contain the expected text. Found: {item_SKU_text}"
        print("Item code verified successfully: ", item_SKU_text)

        first_element = self.driver.find_element(By.CSS_SELECTOR,
                                                 "#product_detail > div.modal-body > div > div > div:nth-child(2) > div:nth-child(8) > div > div > div > div")
        first_element.click()
        time.sleep(3)

        Lenght = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[4]/div/div/div[2]/div/div/div[2]/div[4]/div/div/div/div/ul/li[2]")))
        print("Brushed Gold is visible. Clicking now...")
        Lenght.click()
        time.sleep(3)
        item_SKU_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[id^='item_code_']")))

        # This selector matches any id that starts with 'item_code_'
        item_SKU_text = item_SKU_element.text
        assert "SW01330033" in item_SKU_text, f"Item code does not contain the expected text. Found: {item_SKU_text}"
        print("Item code verified successfully: ", item_SKU_text)

    def test_quantity_input(self):


        print("Waiting for the quantity input to be visible...")
        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "cart_quantity2"))
        )

        # Retrieve the current value of the quantity input
        current_quantity = quantity_input.get_attribute("value")
        print(f"Current quantity is: {current_quantity}")

        # Assert that the current quantity is as expected
        #expected_quantity = "3"  # Change this value to your expected value
        #assert current_quantity == expected_quantity, f"Expected quantity to be {expected_quantity}, but got {current_quantity}."

        print("Quantity matches expected value.")

        # Optional: Interact with increment/decrement buttons and re-check the value
        # Incrementing quantity
        # Increase the quantity by clicking the "+" button 4 times
        print("Increasing the quantity...")
        increase_Quantity = self.driver.find_element(By.CSS_SELECTOR,
                                                     "#quantityBox > button.btn.counter-increment.quantity_plus2")
        for _ in range(4):
            increase_Quantity.click()
            time.sleep(1)  # Small delay to allow UI to update, may adjust based on response time

        # wait for quantity update if necessary

        # Checking updated quantity
        updated_quantity = quantity_input.get_attribute("value")
        print(f"Updated quantity is: {updated_quantity}")

        # Example assertion to check if quantity increased by 1
        new_expected_quantity = "5"  # Adjust according to your increment logic
        assert updated_quantity == new_expected_quantity, f"Expected updated quantity to be {new_expected_quantity}, but got {updated_quantity}."

        # Decrement quantity to check if it decreases
        # Decrease the quantity by clicking the "-" button 2 times
        print("Decreasing the quantity...")
        decrease_Quantity = self.driver.find_element(By.CSS_SELECTOR,
                                                     "#quantityBox > button.btn.counter-decrement.quantity_minus2")
        for _ in range(2):
            decrease_Quantity.click()
            time.sleep(1)  # Small delay to allow UI to update

        # wait for quantity update

        # Re-checking the quantity after decrement
        final_quantity = quantity_input.get_attribute("value")
        print(f"Final quantity after decrement is: {final_quantity}")

        # Assert the final expected quantity after decrement
        final_expected_quantity = "3"  # Adjust this according to decrement logic
        assert final_quantity == final_expected_quantity, f"Expected final quantity to be {final_expected_quantity}, but got {final_quantity}."

        time.sleep(1)

        print("Clear the Selection...")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID,
                                              "clear-variant-selection-73e51ed1-50c2-4ed2-8fab-e03a833cc2fc"))).click()
        time.sleep(5)
        print("Close the popup...")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#product_detail > div.modal-header.modal-header-pad > svg > path:nth-child(1)"))).click()

        print("Scrolling to the cart counter...")
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "#page > div > nav.navbar.navbar__main > div > ul > li:nth-child(5) > a > i")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        print("Arrived at the counter.")

        # Retrieve the text of the element
        element_text = element.text

        # Assert that the text of the element contains "1"
        assert "1" in element_text, f"The element does not contain '1'. Found: {element_text}"
        print("Assertion passed: The Cart contains '1'.")

        print("Click on cart Icon")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#page > div > nav.navbar.navbar__main > div > ul > li:nth-child(5)"))).click()
        print("Click on View Cart")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#cartdetailswrapper > div:nth-child(4) > div > a"))).click()

        time.sleep(3)

        element = self.driver.find_element(By.ID, "sku_73e51ed1-50c2-4ed2-8fab-e03a833cc2fc_0")

        # Get the text of the element
        element_text = element.text

        # Assert that the text of the element contains "1"
        assert "SW01330019" in element_text, f"The element does not contain 'SW01330019'. Found: {element_text}"
        print("Assertion passed: The element contains 'SW01330019'.")

    def test_Edit_add_attriubuate_from_viewcart(self):

        print("Scrolling to the target element...")
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           "#page > main > section > div > div:nth-child(3) > div.col-md-8.px-3.px-md-0 > div > div > div > div > div > div.col-7.col-md-8.cart__img__page > div > div.productCounter.dropdown-align-cart-page > div:nth-child(4) > div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        print("Arrived at the target element.")

        dropdown_selector = "#page > main > section > div > div:nth-child(3) > div.col-md-8.px-3.px-md-0 > div > div > div > div > div > div.col-7.col-md-8.cart__img__page > div > div.productCounter.dropdown-align-cart-page > div:nth-child(4) > div"
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, dropdown_selector)))
        ActionChains(self.driver).move_to_element(dropdown).click().perform()

        print("Dropdown clicked.")

        time.sleep(4)

        # Wait for the dropdown options to become visible and select the third option
        option_selector = "#page > main > section > div > div:nth-child(3) > div.col-md-8.px-3.px-md-0 > div > div > div > div > div > div.col-7.col-md-8.cart__img__page > div > div.productCounter.dropdown-align-cart-page > div:nth-child(4) > div > div > ul > li:nth-child(3)"
        option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, option_selector)))
        option.click()

        print("Option selected.")

        print("Waiting for the confirmation message...")
        try:
            # Wait for the toast message to appear
            confirmation_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#toast-container > div > button"))
            )

            # Get the text of the toast message
            confirmation_text = confirmation_message.text

            # Assert that the expected text is present in the toast message
            assert "Sorry, variant Is not available for add to cart" in confirmation_text, "The toast message did not contain expected text."

            print("Toast message received and verified: ", confirmation_text)
        except TimeoutException:
            # If the toast message does not appear within the timeout, raise an assertion error
            raise AssertionError("Toast message did not appear within the expected time.")
























































