import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestLoginUIEnglish:

    def test_login_popup_appears(self):
        print("Test started: Checking login popup appearance")
        # Click on the login icon
        login_icon = self.driver.find_element(By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[3]/a/img')
        login_icon.click()

        # Wait for the login popup to appear
        login_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="Signin_modal"]/div/div'))
        )

        # Verify the presence of elements in the login popup
        assert self.driver.find_element(By.XPATH,'//*[@id="Signin_modal"]/div/div/div[3]/div[2]/button[1]').is_displayed()
        assert self.driver.find_element(By.XPATH,
                                        '//*[@id="Signin_modal"]/div/div/div[3]/div[2]/button[2]').is_displayed()
        assert 'Do not have an account?' in login_popup.text
        assert self.driver.find_element(By.XPATH, '//*[@id="Signin_modal"]/div/div/div[3]/div[3]/button').is_displayed()
        assert 'Log In' in login_popup.text
        assert 'Choose Login Method' in login_popup.text
        text_link = self.driver.find_element(By.XPATH, '//*[@id="Signin_modal"]/div/div/div[3]/div[3]/button')
        assert text_link.text == 'Signup'
        print("Login popup appearance verification passed successfully")
        print("Test completed: Checking login popup appearance")
