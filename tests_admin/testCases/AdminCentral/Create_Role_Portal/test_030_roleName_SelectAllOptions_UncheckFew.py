import time

import pytest
from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

class Test_030_CreateRole_RoleName_SelectAllOptions_Uncheck_Few:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_roleName_selectAllOptions_uncheck_few_030(self,setup):
        self.logger.info("****************  Test_030 - Test CreateRole when user selects “select all” option and unchecks some and save. ****************")
        print(
            "In Description : TestCase_030 : Test CreateRole when user selects “select all” option and unchecks some and save.")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        print("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        self.RolesList = roles(self.driver)
        self.RolesList.select_roles()
        time.sleep(3)
        self.RolesList.verify_AdminCentral_RolesList_header()
        self.RolesList.select_add_role_button()
        self.RolesList.select_system_from_dropdown()
        creating_role=self.RolesList.send_Random_RoleName()
        self.RolesList.select_Random_roles_checkboxes()
        # self.RolesList.select_save_button()
        # time.sleep(2)
        # self.RolesList.search_toastify_success()
        # list=self.RolesList.verify_Roles_in_SM()
        # print(list)
        # if list.__contains__(creating_role):
        #     print("Role present in the SM UI")
        # else:
        #     print("Role not present in the SM UI")
        # try:
        #     self.RolesList.select_add_role_button()
        # except Exception:
        #     self.RolesList.capture_screenshot()
        #     self.RolesList.select_add_role_button()
        # self.driver.quit()







