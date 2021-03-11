import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_067_CreateUser_Password_OneUpper_OneDigit:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createuser
    def test_createUser_password_oneupper_onedigit_067(self,setup):
        self.logger.info("****************  Test_067:: Test createUser by sending password   one digit and one uppercase character. RegEx:  ^(?=.*[0-9])(?=.*[A-Z]).{8,32}$ ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164248?projectId=50")
        print("****************  Test_067:: Test createUser by sending password   one digit and one uppercase character. RegEx:  ^(?=.*[0-9])(?=.*[A-Z]).{8,32}$ ****************")
        print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164248?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.user = users(self.driver)
        self.user.select_users_Link()

        self.user.select_edit_button()

        self.driver.find_element_by_id("password").send_keys("Abcd1234")
        self.driver.find_element_by_id("confirmPassword").send_keys("Abcd1234")


        self.user.select_save_button()
        try:
            self.user.select_edit_button()
        except Exception:
            self.user.capture_screenshot()
            self.user.select_edit_button()
        self.driver.quit()

        self.user.select_save_button()