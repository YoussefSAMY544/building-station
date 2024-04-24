import time
from lib2to3.pgen2 import driver
from selenium import webdriver

import pyautogui
import pytest


@pytest.mark.usefixtures("setup")

class BaseClass:



        @staticmethod
        def handle_authentication(request):
            # Initialize the WebDriver and open the URL that triggers the authentication dialog
            driver = webdriver.Chrome()  # or use the appropriate driver
            driver.get("https://staging-ksa-v2.build-station.com/sa-en")

            # Here you can add the logic to handle the authentication dialog
            # For example, using pyautogui to input credentials on a system dialog
            time.sleep(5)  # Wait for the dialog to appear

            pyautogui.typewrite('adminstaging')
            pyautogui.press('tab')  # Move to the password field

            time.sleep(5)

            pyautogui.typewrite('qm*+*3&mpz')
            pyautogui.press('enter')  # Press the Enter key to submit the dialog

            def teardown():
                driver.quit()

            request.addfinalizer(teardown)
            return driver
