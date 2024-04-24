import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")

class TestChangelanguage(BaseClass):
    def Test_Change_language(self):
        Switch_language_Icon = self.driver.find_element(By.XPATH, '//*[@id="page"]/div[2]/nav[1]/div/ul/li[1]/div')
        Switch_language_Icon.click()

        English_language =self.driver.find_element(By.XPATH,  '//*[@id="page"]/div[2]/nav[1]/div/ul/li[1]/div/ul/li[1]')
        English_language.click()

        Arabic_language = self.driver.find_element(By.CSS_SELECTOR,
                                                    '#page > div.navbar__wrapper > nav.navbar.navbar__main > div > ul > li.nav-item.navbar-language > div > ul > li.option.selected.focus')
        Arabic_language.click()



