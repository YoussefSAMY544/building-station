
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.Test_Otp import fetch_otp_from_email
import time

#nav__bar__category > div > div > div:nth-child(3) > div > div > div > ul > li:nth-child(3) > a > svg
#nav__bar__category > div > div > div:nth-child(3) > div > div > div > ul > li:nth-child(3) > ul > li:nth-child(1) > a
@pytest.mark.usefixtures("setup")
class TestVariableProduct:
    def test_variable_proudct(self):
        Lighting = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#nav__bar__category > div > div > div:nth-child(3) > a"))
        )
        ActionChains(self.driver).move_to_element(Lighting).perform()

        Outdoor = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#nav__bar__category > div > div > div:nth-child(3) > div > div > div > ul > li:nth-child(3) > a > svg"))
        )
        print("Hovering over the second element")
        ActionChains(self.driver).move_to_element(Outdoor).perform()

        LEDFloodLight = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#nav__bar__category > div > div > div:nth-child(3) > div > div > div > ul > li:nth-child(3) > ul > li:nth-child(1) > a"))
        )
        print("Clicking on the third element")
        LEDFloodLight.click()






