import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Change_Language import TestChangelanguage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestLoginUIArabic(TestChangelanguage):
    def test_login_popup_appears(self):
        print("Starting test: test_login_popup_appears")

        # Click on the language switch icon
        print("Clicking on the language switch icon...")
        Switch_language_Icon = self.driver.find_element(By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[1]/div')
        Switch_language_Icon.click()
        time.sleep(4)  # Waiting for the language menu to appear

        # Select English language
        print("Selecting Arabic language...")
        Arabic_language = self.driver.find_element(By.CSS_SELECTOR,
                                                    '#page > div.navbar__wrapper > nav.navbar.navbar__main > div > ul > li.nav-item.navbar-language > div > ul > li.option.selected.focus')
        Arabic_language.click()

        # Click on the login icon
        print("Clicking on the login icon...")
        login_icon = self.driver.find_element(By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[3]/a/img')
        login_icon.click()

        # Wait for the login popup to appear
        print("Waiting for the login popup to appear...")
        login_popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="Signin_modal"]/div/div'))
        )

        # Verifying the presence of elements in the login popup
        print("Verifying the presence of elements in the login popup...")
        assert self.driver.find_element(By.XPATH,
                                        '//*[@id="Signin_modal"]/div/div/div[3]/div[2]/button[1]').is_displayed(), "Email button not displayed"
        assert self.driver.find_element(By.XPATH,
                                        '//*[@id="Signin_modal"]/div/div/div[3]/div[2]/button[2]').is_displayed(), "Other login button not displayed"
        assert 'لا تملك حساب؟' in login_popup.text, "Sign up text not present"
        assert self.driver.find_element(By.XPATH,
                                        '//*[@id="Signin_modal"]/div/div/div[3]/div[3]/button').is_displayed(), "Sign up button not displayed"
        assert 'الـدخـــول' in login_popup.text, "Login text not present"
        assert 'اختر الوسيلة المناسبة' in login_popup.text, "Instruction text not present"

        text_link = self.driver.find_element(By.XPATH, '//*[@id="Signin_modal"]/div/div/div[3]/div[3]/button')
        assert text_link.text == 'سجل', "Register button text mismatch"

        print("Test completed successfully.")
