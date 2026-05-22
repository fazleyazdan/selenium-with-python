import pytest
from utils.helper_function import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()