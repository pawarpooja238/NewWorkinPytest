import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PagesObject.Loginpage import Login
from PagesObject.Dashbord import dashbord
@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_001(self):
        lg = Login(self.driver)
        db = dashbord(self.driver)
        lg.input_username("Admin")
        lg.input_password("admin123")
        lg.click_login()

        if 'Paul Collings' in db.wellcome_text():
            assert True
            print("test pass test 1")
        else:
            assert False
            print("test fail test 1")

    def test_002(self):
        lg = Login(self.driver)
        db = dashbord(self.driver)
        lg.input_username("Admin1")
        lg.input_password("admin123")
        lg.click_login()
        time.sleep(2)
        if 'Invalid credentials' in lg.invalid_method():
            assert True
            print("test pass test 2")
        else:
            assert False
            print("test fail test 2")