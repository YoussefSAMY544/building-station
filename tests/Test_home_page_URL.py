import pytest
from selenium import webdriver





@pytest.mark.usefixtures("setup")
class TestHomePageURL:

    def test_home_page_url(self):
        print("Test started: Home page URL verification")
        expected_url = "https://staging-ksa-v2.build-station.com/sa-en"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Expected URL: {expected_url}, but got: {actual_url}"
        print("Home page URL verification passed successfully")
        print("Test completed: Home page URL verification")
