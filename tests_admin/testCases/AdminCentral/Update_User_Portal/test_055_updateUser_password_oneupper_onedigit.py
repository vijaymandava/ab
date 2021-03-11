import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_055_UpdateUser_Password_OneUpper_OneDigit:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.updateuser
    def test_updateUser_password_oneupper_onedigit_055(self,setup):
        self.logger.info("****************  Test_055:: Test UpdateUser by sending password   one digit and one uppercase character. RegEx:  ^(?=.*[0-9])(?=.*[A-Z]).{8,32}$ ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        print(
            "****************  Test_055:: Test UpdateUser by sending password   one digit and one uppercase character. RegEx:  ^(?=.*[0-9])(?=.*[A-Z]).{8,32}$ ****************")
        print(
            "Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
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
        self.user.verify_error()
        try:
            self.user.select_edit_button()
        except Exception:
            self.user.capture_screenshot()
            self.user.select_edit_button()
        self.driver.quit()