import pytest
from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager

# To test in single Browser
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome('Drivers/chromedriver.exe')
#     return driver

#To Test in multiple browsers
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome('./tests_admin/Drivers/chromedriver.exe')
        print("Launching Browser Chrome......")
        driver.maximize_window()
        driver.implicitly_wait(100)
    elif browser=='Edge':
        driver = webdriver.Edge()
        print("Launching Firefox Browser......")
        driver.maximize_window()
    else:
        driver = webdriver.Chrome('./tests_admin/Drivers/chromedriver.exe')
        driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# .........PyTest HTML Reports ...............
#Add the Required fileds in the Reports
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'RMB'
#     config._metadata['Tester'] = 'Vijay'
#
# #Modify/delete fields in the report
# def pytest_metadata(metadata):
#     metadata.pop("Packages", None)
#     metadata.pop("Plugins", None)
#     metadata.pop("Python", None)




