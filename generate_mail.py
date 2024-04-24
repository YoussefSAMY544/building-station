import random
import string

def generate_random_email():
    # Generate a random username with digits and lowercase letters
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    # Combine the username with the domain name
    email = f"{username}_sami{random.randint(2000, 2025)}@yahoo.com"

    return email




#from selenium.common.exceptions import StaleElementReferenceException

#attempts = 0
#while attempts < 3:
    #try:
        #element = driver.find_element_by_id('element_id')
        #element.click()
        #break
    #except StaleElementReferenceException:
        #attempts += 1

