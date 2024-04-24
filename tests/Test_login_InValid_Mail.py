import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.mark.usefixtures("setup")

def test_login_with_invalid_email(driver):

    print("Test started: Logging in with an invalid email address")

    # Navigate to the website
    print("Navigating to the website...")
    driver.get("https://staging-ksa-v2.build-station.com/sa-en")

    # Click on the login icon
    print("Clicking on the login icon...")
    login_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[3]/a')))
    login_icon.click()

    # Wait for the login modal to appear
    print("Waiting for the login modal to appear...")
    login_modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="Signin_modal"]/div/div')))

    # Click on the mail button
    print("Clicking on the mail button...")
    mail_button = WebDriverWait(login_modal, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Signin_modal"]/div/div/div[3]/div[2]/button[2]')))
    mail_button.click()

    # Wait for the email modal to appear
    print("Waiting for the email modal to appear...")
    email_modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="Signin-email_modal"]/div/div')))

    # Find the email field and enter the email address
    print("Entering the email address...")
    email_field = WebDriverWait(email_modal, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="email_auth_second"]')))
    email_field.send_keys("fdkm@mkfdmj=")

    # Find and click on the login button
    print("Clicking on the login button...")
    login_button = WebDriverWait(email_modal, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Signin-email_modal"]/div/div/div[3]/button')))
    login_button.click()

    # Wait for the error message to appear
    print("Waiting for the error message to appear...")
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "* Please provide valid email address")]')))

    # Check if the error message contains the expected text
    print("Checking the error message...")
    assert "* Please provide valid email address" in error_message.text

    print("Test completed: Logged in with an invalid email address")
