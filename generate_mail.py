import random
import string
from lib2to3.pgen2 import driver


def generate_random_email():
    # Generate a random username with digits and lowercase letters
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    # Combine the username with the domain name
    email = f"{username}_sami{random.randint(2000, 2025)}@yahoo.com"

    return email







