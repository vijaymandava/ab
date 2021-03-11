import time

import allure
import pytest
from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@allure.severity(allure.severity_level.NORMAL)
class Test_004_DuplicateRole():
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_rolename_duplicateRole_existingRole_004(self,setup):
        self.logger.info("****************  Test_004_Test CreateRole when userClick ADD button and try to create existing/duplicate role .  ****************")
        print(
            "In Description : TestCase_004: Test CreateRole when userClick ADD button and try to create existing/duplicate role.")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        print("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        self.RolesList = roles(self.driver)
        self.RolesList.select_roles()
        time.sleep(3)
        self.RolesList.verify_AdminCentral_RolesList_header()
        self.RolesList.select_add_role_button()
        self.RolesList.send_existing_role_as_roleName()
        self.RolesList.select_system_from_dropdown()
        self.RolesList.select_save_button()


        time.sleep(5)
        try:
            self.RolesList.select_system_from_dropdown()
        except Exception:
            self.RolesList.capture_screenshot()
            self.RolesList.select_system_from_dropdown()
        self.driver.quit()





