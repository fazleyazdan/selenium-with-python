from pytest_bdd import given, when, then, scenarios
from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

scenarios("../features/login.feature")

load_dotenv(override=True)
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

@given("user is on login page")
def open_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

@when("user enters valid username and password")
def enter_credentials(driver):
    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)

 
@when("clicks login button")
def click_login(driver):
    login = LoginPage(driver)
    login.click_login()

@then("user should be redirected to secure page")
def verify_login(driver):
    assert "secure" in driver.current_url