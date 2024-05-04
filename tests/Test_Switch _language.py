import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestLanguageSelection:

    def test_language_selection(self):
        print("Test started: Language selection")

        # Find the language dropdown
        print("Finding the language dropdown...")
        language_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[1]/div'))
        )
        # Click on the language dropdown
        print("Clicking on the language dropdown...")
        language_dropdown.click()

        # Wait for the first language option to appear
        print("Waiting for the first language option...")
        language_option_1 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[1]/div/ul/li[1]'))
        )
        # Click on the first language option
        print("Clicking on the first language option...")
        language_option_1.click()

        # Re-locate the language dropdown after the page has updated
        print("Re-locating the language dropdown...")
        language_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[1]/div'))
        )

        # Click on the language dropdown again
        print("Clicking on the language dropdown again...")
        language_dropdown.click()

        # Wait for the second language option to appear
        print("Waiting for the second language option...")
        language_option_2 = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[1]/div/ul/li[2]'))
        )

        # Click on the second language option
        print("Clicking on the second language option...")
        language_option_2.click()

        # Assert that the URL changes to English
        assert self.driver.current_url == "https://staging-ksa-v2.build-station.com/sa-ar"
        print("Language dropdown working well")
        print("Test completed: Language selection")
