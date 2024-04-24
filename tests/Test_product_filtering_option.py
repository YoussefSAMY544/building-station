import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class TestProductFiltering:
    def test_proudct_filter(self):

        Lighting = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#nav__bar__category > div > div > div:nth-child(1) > a"))
        )
        print("Hovering over the first element")
        ActionChains(self.driver).move_to_element(Lighting).perform()

        Outdoor = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="nav__bar__category"]/div/div/div[1]/div/div/div/ul/li[1]/a/span'))
        )
        print("Hovering over the second element")
        ActionChains(self.driver).move_to_element(Outdoor).perform()

        LEDFloodLight = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="nav__bar__category"]/div/div/div[1]/div/div/div/ul/li[1]/ul/li[6]/a'))
        )
        print("Clicking on the third element")
        LEDFloodLight.click()

        print("Opening price dropdown")
        pricedropdown = WebDriverWait(self.driver, 10).until(
         EC.presence_of_element_located((By.CSS_SELECTOR, "#navbarOffcanvasLg > div:nth-child(2) > section > div > div > div:nth-child(2) > button"))).click()

        # Define the price range
        min_price = 0
        max_price = 200

        print("Entering the minimum price")
        min_price_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "minPriceFilter"))
        )
        min_price_input.clear()
        min_price_input.send_keys(str(min_price))

        print("Entering the maximum price")
        max_price_input = self.driver.find_element(By.ID, "maxPriceFilter")
        max_price_input.clear()
        max_price_input.send_keys(str(max_price))

        print("Clicking on the apply filter button")
        apply_filter_button = self.driver.find_element(By.ID, "priceFilterApply")
        apply_filter_button.click()

        time.sleep(20)  # Waiting for the products to load

        # Get the prices of all displayed products
        product_prices = self.driver.find_elements(By.CLASS_NAME, "product__amount")

        # Verify that all product prices fall within the specified range
        for price_element in product_prices:
            price_text = price_element.text.strip('$')  # Assuming the price is displayed with a $ sign
            try:
                price = float(price_text)
                assert min_price <= price <= max_price, "Filter not applied correctly: Some products are outside the specified price range"
            except ValueError:
                print(f"Error: Could not convert '{price_text}' to float")

        # If the loop completes without raising an assertion, then all products are within the specified range
        print("Filter applied correctly: All products are within the specified price range")

    def test_proudct_filter_watt(self):
        Lighting = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#nav__bar__category > div > div > div:nth-child(1) > a"))
        )
        print("Hovering over the first element")
        ActionChains(self.driver).move_to_element(Lighting).perform()

        Outdoor = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="nav__bar__category"]/div/div/div[1]/div/div/div/ul/li[1]/a/span'))
        )
        print("Hovering over the second element")
        ActionChains(self.driver).move_to_element(Outdoor).perform()

        LEDFloodLight = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="nav__bar__category"]/div/div/div[1]/div/div/div/ul/li[1]/ul/li[6]/a'))
        )
        print("Clicking on the third element")
        LEDFloodLight.click()

        print("Opening price dropdown")
        pricedropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "#navbarOffcanvasLg > div:nth-child(2) > section > div > div > div:nth-child(3) > button"))).click()




        WATTRadiobutton = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#radio_05389"))
        ).click()

        time.sleep(20)


        # Find all elements with the class "product__title recentItem__title"
        product_titles = self.driver.find_elements(By.CSS_SELECTOR, "#page > main > section.section__products > div > div:nth-child(3) > div.col-md-9 > div.row.gy-4.products_grid > div > article > div.product__meta.mobileCart > a")
        print(f"Number of product titles found: {len(product_titles)}")

        for title_element in product_titles:
            product_title = title_element.text
            print(f"Product title found: '{product_title}'")

            if "300 watt" in product_title:
                print(f"Product title '{product_title}' contains '300 watt'")
            else:
                print(f"Product title '{product_title}' does not contain '300 watt'")

    def test_proudct_filter_ALLOPTIONS(self):
            Lighting = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#nav__bar__category > div > div > div:nth-child(1) > a"))
            )
            print("Hovering over the first element")
            ActionChains(self.driver).move_to_element(Lighting).perform()

            Outdoor = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="nav__bar__category"]/div/div/div[1]/div/div/div/ul/li[1]/a/span'))
            )
            print("Hovering over the second element")
            ActionChains(self.driver).move_to_element(Outdoor).perform()

            LEDFloodLight = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#nav__bar__category > div > div > div:nth-child(1) > div > div > div > ul > li:nth-child(1) > ul > li:nth-child(6) > a"))
            )
            print("Clicking on the third element")
            LEDFloodLight.click()

            print("Opening price dropdown")
            pricedropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "#navbarOffcanvasLg > div:nth-child(2) > section > div > div > div:nth-child(4) > button"))).click()

            LumenRadiobutton= WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#radio_05388"))).click()

            time.sleep(20)
            IPdropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "#navbarOffcanvasLg > div:nth-child(2) > section > div > div > div:nth-child(5) > button"))).click()

            IPRadiobutton = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#radio_063"))
            ).click()

            IP=65

            time.sleep(20)

            ColorTemperaturedropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "#navbarOffcanvasLg > div:nth-child(2) > section > div > div > div:nth-child(6) > button"))).click()

            ColorTemperatureRadiobutton = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#radio_0597"))
                   ).click()

            ColorTemperature=3000, 4000, 5700


            time.sleep(20)

            CRIdropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                "#navbarOffcanvasLg > div:nth-child(2) > section > div > div > div:nth-child(7) > button"))).click()

            CRIadiobutton = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#radio_058"))
            ).click()

            CRI=80


            # Assert that no products message is displayed
            no_products_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".row.gy-4.products_grid"))
            )
            assert "Sorry, no products found in this category" in no_products_message_element.text, \
                "Expected message 'Sorry, no products found in this category' not found"







