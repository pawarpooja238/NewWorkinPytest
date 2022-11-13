from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
        self.driver=driver
        self.textbox_username_Xpath= "//input[@name='username']"
        self.textbox_password_Xpath= "//input[@name='password']"
        self.button_login_xpath= "//button[@type='submit']"
        self.invalid_msg_xpath="//div[@class='oxd-alert-content oxd-alert-content--error']"
    def input_username(self,username):
       # self.driver.implecite_wait(3)
        self.driver.find_element(By.XPATH, self.textbox_username_Xpath).send_keys(username)
    def input_password(self,passwors):
        self.driver.find_element(By.XPATH, self.textbox_password_Xpath).send_keys(passwors)
    def click_login(self):
        self.driver.find_element(By.XPATH,  self.button_login_xpath).click()

    def invalid_method(self):
        return self.driver.find_element(By.XPATH,self.invalid_msg_xpath).text