import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from PagesObject.Dashbord import dashbord
from PagesObject.Loginpage import Login


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_003(self):
        lg = Login(self.driver)
        db = dashbord(self.driver)
        lg.input_username("Admin")
        lg.input_password("admin123")
        lg.click_login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(db.admin_tab_hover()).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(db.job_tab_hover()).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(db.employment_status_tab_hover()).click().perform()