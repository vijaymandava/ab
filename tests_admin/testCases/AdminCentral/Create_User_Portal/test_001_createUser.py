import time
import pytest
from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_001_CreateUser:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createuser
    def test_createUser_001(self,setup):
        self.logger.info("****************  Test_001:: Test CreateUser when user Click ADD button and add name then save user. ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164248?projectId=50")
        print("****************  Test_001:: Test CreateUser when user Click ADD button and add name then save user. ****************")
        print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164248?projectId=50")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.user = users(self.driver)
        self.user.select_users_Link()
        self.user.select_add_button()
        self.user.send_username_textbox()
        self.user.send_firstname_textbox()
        self.user.send_middleinitial_textbox()
        self.user.send_lastname_textbox()
        self.user.send_emailaddress_textbox()
        self.user.send_telephonenumber_textbox()
        self.user.send_extension_textbox()
        self.user.send_same_password_and_confirmPassword()
        self.user.select_system_dropdown()
        time.sleep(3)
        # self.user.select_Role_from_dropdown()
        self.user.select_save_button()
        self.user.verify_error()
        try:
            self.user.select_add_button()
        except Exception:
            self.user.capture_screenshot()
            self.user.verify_error()
            self.user.select_add_button()

        self.driver.quit()





