import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_069_CreateUser_Default_UserNames:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createuser
    def test_createUser_default_userNames_069(self,setup):
        self.logger.info("****************  Test_069:: Test CreateUser by sending default UserNames ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164248?projectId=50")
        print("****************  Test_069:: Test CreateUser by sending default UserNames ****************")
        print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164248?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.user = users(self.driver)
        self.user.select_users_Link()

        self.user.select_default_user()
        self.user.send_same_password_and_confirmPassword()

        self.user.select_save_button()

        try:
            self.user.select_add_button()
        except Exception:
            self.user.capture_screenshot()
            self.user.verify_error()
            self.user.select_add_button()

        self.driver.quit()