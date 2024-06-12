import pytest
from selenium import webdriver
import pytest
from selenium import webdriver
import pyautogui
import time

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Choose browser: chrome, firefox, or safari"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    print("Setting up WebDriver...")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://staging-ksa-v2.build-station.com/sa-en")
    request.cls.driver = driver
    time.sleep(2)  # Wait for the dialog to appear
    pyautogui.typewrite('adminstaging')
    pyautogui.press('tab')  # Move to the password field
    pyautogui.typewrite('qm*+*3&mpz')
    pyautogui.press('enter')  # Press the Enter key to submit the dialog


    yield driver

    print("Quitting WebDriver...")
    driver.quit()

    import pytest

    @pytest.fixture(scope="function")
    def login_with_email_and_otp():
        # Perform login with email and OTP
        # Example code to perform login...
        print("Performing login with email and OTP")
        # Example code to yield any necessary objects or values...
        yield



