from telnetlib import EC
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
@pytest.fixture(scope="module")
def chrome_driver():
    # Replace 'path_to_chromedriver' with the actual path to chromedriver.exe
    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(4)
    driver.get("https://staging-ksa-v2.build-station.com/sa-ar")

    def handle_authentication_dialog(Username, Password):
        # Wait for the dialog to appear (adjust the sleep time as needed)
        time.sleep(2)

        # Type the username
        pyautogui.typewrite(Username)

        # Press TAB to switch to the password field
        pyautogui.press('tab')

        # Type the password
        pyautogui.typewrite(Password)

        # Press Enter to submit the credentials


    # Example usage
    username = "adminstaging"
    password = "qm*+*3&mpz"
    handle_authentication_dialog(username, password)
    time.sleep(4)
    pyautogui.press('Sign in')
    pyautogui.press('Sign in')
    yield driver
    #driver.quit()

def test_open_website(chrome_driver):
    chrome_driver.get("https://staging-ksa-v2.build-station.com/sa-en")

if __name__ == "__main__":
    pytest.main([__file__])


    def test_open_website(chrome_driver):
        # Navigate to the desired page
        chrome_driver.get("https://staging-ksa-v2.build-station.com/ae-en")

        # Wait for the element to be clickable
        WebDriverWait(chrome_driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[2]/div[1]')))

        # Find the element
        element = chrome_driver.find_element(By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[2]/div[1]')
        WebDriverWait(chrome_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[2]/div[1]/ul/li[2]')))
        child_element = chrome_driver.find_element(By.XPATH,
                                                   '//*[@id="page"]/div[2]/nav[1]/div/ul/li[2]/div[1]/ul/li[2]')
        child_element.click()

        # Click on the element
        element.click()


