import pytest
import time
import allure
from allure_commons.types import AttachmentType

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.testCases.AdminCentral.Create_Role_Portal.common_role_portal import Common_role_portal
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@allure.severity(allure.severity_level.BLOCKER)
class Test_043:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_total_checkboxes_043(self, setup):
        self.logger.info(
            "****************  Test_043 : Test updateRole when user Click ADD button and verify total check boxes ****************")
        print("In Description : Test_043 : Test updateRole when user Click ADD button and verify total checkboxes ")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        print("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        self.RolesList = roles(self.driver)
        self.RolesList.select_roles()
        time.sleep(2)
        self.RolesList.verify_AdminCentral_RolesList_header()
        self.RolesList.select_add_role_button()
        self.RolesList.total_checkboxes()
        len = self.RolesList.total_checkboxes_size()
        assert len == 43
        self.driver.close()