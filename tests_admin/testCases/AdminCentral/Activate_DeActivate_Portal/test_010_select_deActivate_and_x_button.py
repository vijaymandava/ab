import pytest
import time

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Test_010_Select_DeActivate_Button_close:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.activate_deactivate_button
    def test_select_deactivate_button_close_010(self,setup):
        self.logger.info("****************  IN description :TestCase_010 : Test DeActivate option when user  Click Deactivate button and select * button ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164257?projectId=50")
        print(
            "****************  IN description :TestCase_010 : Test DeActivate option when user  Click Deactivate button and select * button ****************")
        print("Jama link::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164257?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        time.sleep(5)
        self.user = users(self.driver)
        self.user.select_users_Link()
        self.user.select_deactivate_button()
        self.user.select_close_x()
        self.driver.close()