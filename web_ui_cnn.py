from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
from Utils import WaitUtils

class WebUI():
    login_button_xpath = '//button[@data-test="userLoginButton"]'
    login_access_xpath = '//button[@class="user-account-login-form__button user-account-shared__button"]'
    email_name = "loginEmail"
    pass_id = "login-password-input"

    def __init__(self, driver, url = None):
        self._driver = driver
        if url: 
            self._driver.get(url)

    def login(self):
        WaitUtils.wait_xpath(self._driver, self.login_button_xpath).click()

    def input_email(self):
        emailTextfield = WaitUtils.wait_by(self._driver, By.NAME, self.email_name)
        emailTextfield.send_keys("bichphuonggl1997@gmail.com")

    def input_password(self):
        passTextfield = WaitUtils.wait_by(self._driver, By.ID, self.pass_id)
        passTextfield.send_keys("Bichphuong@888")

    def login_access(self):
        WaitUtils.wait_xpath(self._driver, self.login_access_xpath).click()