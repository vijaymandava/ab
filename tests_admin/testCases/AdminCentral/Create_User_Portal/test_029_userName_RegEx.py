import random
import string

import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Test_029_roleName_RegEx:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createuser
    def test_userName_RegEx_029(self,setup):
        self.logger.info("****************  Test_029: test User name RegEx  ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164248?projectId=50")
        print("****************  Test_029: test User name RegEx  ****************")
        print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164248?projectId=50")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.user = users(self.driver)
        self.user.select_users_Link()
        self.user.select_add_button()

        self.user.userName_RegEx()
        self.user.send_firstname_textbox()
        self.user.send_middleinitial_textbox()
        self.user.send_lastname_textbox()
        self.user.send_emailaddress_textbox()
        self.user.send_telephonenumber_textbox()
        self.user.send_extension_textbox()
        self.user.send_same_password_and_confirmPassword()
        self.user.select_system_dropdown()
        self.user.select_Role_from_dropdown()
        self.user.select_save_button()
        self.user.verify_error()

        try:
            self.user.select_add_button()
        except Exception:
            self.user.capture_screenshot()
            self.user.select_add_button()
        self.driver.quit()