import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
@pytest.fixture
def setup(request):
    service_obj = Service("C:/Users/Dell/PycharmProjects/Driver/chromedriver_win32 (1)/chromedriver.exe")
    request.cls.driver = webdriver.Chrome(service=service_obj)
    request.cls.driver.implicitly_wait(5)

    request.cls.driver.get("https://opensource-demo.orangehrmlive.com")
    request.cls.driver.implicitly_wait(8)
    yield
    request.cls.driver.quit()



# @pytest.fixture
# def setup(request):
#     request.cls.driver = webdriver.Chrome(executable_path="C:/Users/Dell/PycharmProjects/Driver/chromedriver_win32 (1)/chromedriver.exe")
#     request.cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     yield
#     request.cls.driver.quit()