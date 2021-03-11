import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_050_UpdateUser_Password_ConfirmPassword_Different:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.updateuser
    def test_updateUser_password_confirmpassword_different_050(self,setup):
        self.logger.info("****************  Test_050:: Test UpdateUser by sending password & CreatePassword does not match ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        print(
            "****************  Test_050:: Test UpdateUser by sending password & CreatePassword does not match ****************")
        print(
            "Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.user = users(self.driver)
        self.user.select_users_Link()

        self.user.select_edit_button()
        self.user.password_RegEx()
        self.user.confirmPassword_RegEx()
        self.user.select_save_button()

        try:
            self.user.select_edit_button()
        except Exception:
            self.user.capture_screenshot()
            self.user.select_edit_button()
        self.driver.quit()