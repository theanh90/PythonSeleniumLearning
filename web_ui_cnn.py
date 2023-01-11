
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys

class WebUI():
    login_button_xpath = '//button[@data-test="userLoginButton"]' 
    def __init__(self, driver, url = None):
        self._driver = driver
        if url: 
            self._driver.get(url)
    
    def wait_id(self, _id, timeout = 10):
        return WebDriverWait (self._driver, timeout).until(
            EC.presence_of_all_elements_located((By.ID, _id))
        )

    def wait_xpath(self, xpath, timeout = 10):
        return WebDriverWait (self._driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )

    def login(self):
        # login_button_xpath = '//button[@data-test="userLoginButton"]'   
        self.wait_xpath(self.login_button_xpath)[0].click()
        check_log = self.wait_xpath(self.login_button_xpath)
        sys.stderr.write(check_log)
        assert 1 == 0

    def input_email(self):
        self.wait_id(By.NAME, "loginEmail")
        self.send_keys("bichphuonggl1997@gmail.com")

    def input_password(self):
        self.wait_id(By.ID, "login-password-input")
        self.send_keys("Bichphuong@888")

    def login_access(self):
        login_access_xpath = '//button[@class="user-account-login-form__button user-account-shared__button"]'   
        self.wait_xapth(By.XPATH, login_access_xpath).click()