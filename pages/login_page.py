from selenium.webdriver.common.by import By
from utils.helper_function import type_text, click

class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self):
        type_text(self.driver, self.USERNAME, "tomsmith")

    def enter_password(self):
        type_text(self.driver, self.PASSWORD, "SuperSecretPassword!")

    def click_login(self):
        click(self.driver, self.LOGIN_BTN)