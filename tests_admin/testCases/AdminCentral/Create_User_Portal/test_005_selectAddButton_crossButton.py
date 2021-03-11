import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Test_005_Select_cross_x_button:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createuser
    def test_cross_x_button_005(self,setup):
        self.logger.info("****************  Test_005: Test CreateUser when userClick ADD button and select cross(*) button  ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164248?projectId=50")
        print("****************  Test_005: Test CreateUser when userClick ADD button and select cross(*) button  ****************")
        print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164248?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.User = users(self.driver)
        self.User.select_add_button()
        self.User.select_close_x()
        try:
            self.User.select_add_button()
        except Exception:
            self.User.capture_screenshot()
            self.User.verify_error()
            self.User.select_add_button()

        self.driver.quit()