from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WaitUtils:
    @staticmethod
    def wait_by(driver, by, value, timeout = 10):
        return WebDriverWait (driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    @staticmethod
    def wait_xpath(driver, xpath, timeout = 10):
        return WebDriverWait (driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )