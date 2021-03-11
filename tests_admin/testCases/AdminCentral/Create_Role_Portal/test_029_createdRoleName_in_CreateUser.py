import pytest
import time

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.testCases.AdminCentral.Create_Role_Portal.common_role_portal import Common_role_portal
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

class Test_029_CreatedRole_in_CreateUsers:

    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_roleName_CreatedRole_in_CreateUsers_029(self,setup):
        self.logger.info("****************  Test_029 - Test that Created Role is displayed in the Role option while Creating User ****************")
        print(
            "In Description : TestCase_029 - Test that Created Role is displayed in the Role option while Creating User")
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
        self.RolesList.selectAll_checkbox()
        self.RolesList.select_save_button()
        time.sleep(2)
        self.RolesList.search_toastify(creating_role)
        self.RolesList.verify_cm_ui_positive(creating_role)
        com = Common_role_portal()
        com.verify_roles_from_sm_with_api(creating_role)
        list=self.RolesList.verify_Roles_in_SM()
        print(list)
        if list.__contains__(creating_role):
            print("Role present in the SM UI")
        else:
            print("Role not present in the SM UI")
        self.UserList = users(self.driver)
        self.UserList.select_users_Link()
        time.sleep(5)
        self.UserList.select_add_button()
        self.UserList.select_system_dropdown()
        UserRolelist=self.UserList.select_Role_dropdown()
        if UserRolelist.__contains__(creating_role):
            print("Role present")
        else:
            print("Role not present ")
        self.driver.close()

