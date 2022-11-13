from selenium.webdriver.common.by import By
class dashbord:
    def __init__(self,driver):
        self.driver=driver
        self.text_welcomemsg="//p[text()='Paul Collings']"
        self.admin_tab_xpath="//span[text()='Admin']"
        self.job_tab_xpath="//li[@class='--active oxd-topbar-body-nav-tab --parent']"
        self.employment_status_tab_xpath='//a[text()="Employment Status"]'

    def wellcome_text(self):
        return self.driver.find_element(By.XPATH, self.text_welcomemsg).text
    def admin_tab_hover(self):
        return self.driver.find_element(By.XPATH, self.admin_tab_xpath)
    def job_tab_hover(self):
        return self.driver.find_element(By.XPATH, self.job_tab_xpath)
    def employment_status_tab_hover(self):
        return self.driver.find_element(By.XPATH,self.employment_status_tab_xpath)
