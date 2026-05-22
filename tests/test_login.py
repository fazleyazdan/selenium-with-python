from typing import overload, override

from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

load_dotenv(override=True)

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


def test_login(driver):

    driver.get("https://the-internet.herokuapp.com/login")

    login = LoginPage(driver)
    login.login(username, password)

    assert "secure" in driver.current_url