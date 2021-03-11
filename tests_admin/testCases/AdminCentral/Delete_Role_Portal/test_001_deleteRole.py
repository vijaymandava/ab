import time

import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Test_001_DeleteRole:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.deleterole
    def test_deleteRole_001(self,setup):
        self.logger.info("****************  Test_001_Test DeleteRole when user Click 'Delete' button. ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164245?projectId=50")
        print("****************  Test_001_Test DeleteRole when user Click 'Delete' button. ****************")
        print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164245?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        time.sleep(10)
        self.RolesList = roles(self.driver)
        self.RolesList.select_roles()
        self.RolesList.select_delete_role_button()
        self.RolesList.select_ok_button_deleteRole_popup()
        self.driver.close()
