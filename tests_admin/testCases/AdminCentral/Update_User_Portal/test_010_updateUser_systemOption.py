import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_010_UpdateUser_systemOptions:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.updateuser
    def test_UpdateUser_systemOptions_010(self,setup):
        self.logger.info("**************** Test_010:: Test UpdateUser when user  Try to Update 'System' option ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        print(
            "**************** Test_010:: Test UpdateUser when user  Try to Update 'System' option ****************")
        print(
            "Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.user = users(self.driver)
        self.user.select_users_Link()

        self.user.select_edit_button()

        self.user.select_system_dropdown()

        self.user.select_save_button()
        try:
            self.user.select_edit_button()
        except Exception:
            self.user.capture_screenshot()
            self.user.select_edit_button()
        self.driver.quit()