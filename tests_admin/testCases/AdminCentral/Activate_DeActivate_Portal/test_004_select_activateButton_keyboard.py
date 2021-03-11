import pytest
import time

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Test_004_Select_Activate_Button_keyBoard:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.activate_deactivate_button
    def test_select_activate_button_keyboard_004(self,setup):
        self.logger.info("**************** IN Description: TestCase_004 : Test Activate option when user access with  Keyboard Tabbing. ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164257?projectId=50")
        print(
            "**************** IN Description: TestCase_004 : Test Activate option when user access with  Keyboard Tabbing. ****************")
        print("Jama link::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164257?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        time.sleep(5)
        self.user = users(self.driver)
        self.user.select_users_Link()
        self.driver.close()
