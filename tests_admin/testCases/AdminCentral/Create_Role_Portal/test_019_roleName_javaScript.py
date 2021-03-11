import pytest
import time
from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

class Test_019_CreateRole_RoleName_JavaScript:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_roleName_javaScript_019(self, setup):
        self.logger.info("****************  test_019 ::  Test CreateRole when user sends 'userRoleName' with values ::  javascript ****************")
        print(
            "In Description : TestCase_019 ::  Test CreateRole when user sends 'userRoleName' with values ::  javascript ")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        print("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        self.RolesList = roles(self.driver)
        self.RolesList.select_roles()
        time.sleep(3)
        self.RolesList.select_add_role_button()
        self.RolesList.select_system_from_dropdown()
        data = "alert(document.getElementById('testInput').name);"
        print("String is :::", data)
        self.RolesList.send_userrole_runtime(data)
        self.RolesList.select_Random_roles_checkboxes()
        self.RolesList.select_save_button()
        self.RolesList.search_toastify(data)
        time.sleep(1)
        try:
            self.RolesList.select_Random_roles_checkboxes()
        except Exception:
            self.RolesList.capture_screenshot()
            self.RolesList.select_Random_roles_checkboxes()
        self.driver.quit()
