from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_driver():


    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    ser_obj = Service(r"D:\apps\chromedriver-win64\chromedriver.exe")

    driver = webdriver.Chrome(
        service=ser_obj,
        options=options
    )

    driver.implicitly_wait(10)

    return driver

def click(driver, locator):
    driver.find_element(*locator).click()


def type_text(driver, locator, text):
    driver.find_element(*locator).send_keys(text)


def get_text(driver, locator):
    return driver.find_element(*locator).text


def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )


def take_screenshot(driver, name="screenshot"):
    driver.save_screenshot(f"{name}.png")