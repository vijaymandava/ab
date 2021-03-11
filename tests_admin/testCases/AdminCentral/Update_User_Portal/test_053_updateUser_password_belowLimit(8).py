import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_053_UpdateUser_Password_Below8Characters:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.updateuser
    def test_updateUser_password_below8Characters_053(self,setup):
        self.logger.info("****************  Test_053:: Test UpdateUser by sending password below 8 characters ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        print(
            "****************  Test_053:: Test UpdateUser by sending password below 8 characters ****************")
        print(
            "Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.user = users(self.driver)
        self.user.select_users_Link()

        self.user.select_edit_button()
        self.driver.find_element_by_id("password").send_keys("abc")
        self.user.confirmPassword_RegEx()
        self.user.select_save_button()
        self.user.verify_error()
        try:
            self.user.firstName_RegEx()
        except Exception:
            self.user.capture_screenshot()
            self.user.select_edit_button()
        self.driver.quit()