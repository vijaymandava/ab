from tests_admin.utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By


class admin_central_login():
    textbox_userName_id = "userName"
    textbox_Password_id = "password"
    button_login_xpath = "//button[text()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def admin_login(self):
        username = ReadConfig.username()
        self.driver.find_element_by_id(self.textbox_userName_id).clear()
        self.driver.find_element_by_id(self.textbox_userName_id).send_keys(username)
        password = ReadConfig.password()
        self.driver.find_element_by_id(self.textbox_Password_id).clear()
        self.driver.find_element_by_id(self.textbox_Password_id).send_keys(password)
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def send_userName(self):
        username = ReadConfig.username()
        self.driver.find_element_by_id(self.textbox_userName_id).clear()
        self.driver.find_element_by_id(self.textbox_userName_id).send_keys(username)

    def send_password(self):
        password = ReadConfig.password()
        self.driver.find_element_by_id(self.textbox_Password_id).clear()
        self.driver.find_element_by_id(self.textbox_Password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()


