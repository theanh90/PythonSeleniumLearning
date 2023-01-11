from selenium import webdriver
from web_ui_cnn import WebUI

class Test_cnn_login():
    def setup(self):
        self.driver = webdriver.Chrome()
    
    def test_login_cnn(self):
        web_ui = WebUI(self.driver, 'https://edition.cnn.com/')
        web_ui.login()
        web_ui.input_email()
        web_ui.input_password()
        web_ui.login_access()
        assert 2 == 1 + 1



