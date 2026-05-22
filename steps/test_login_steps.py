from pytest_bdd import given, when, then, scenarios
from pages.login_page import LoginPage

scenarios("../features/login.feature")

@given("user is on login page")
def open_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

@when("user enters valid username and password")
def enter_credentials(driver):
    login = LoginPage(driver)
    login.enter_username()
    login.enter_password()


@when("clicks login button")
def click_login(driver):
    login = LoginPage(driver)
    login.click_login()

@then("user should be redirected to secure page")
def verify_login(driver):
    assert "secure" in driver.current_url