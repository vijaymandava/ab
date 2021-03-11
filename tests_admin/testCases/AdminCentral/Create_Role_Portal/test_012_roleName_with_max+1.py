import pytest
import time
from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig
import random
import string

class Test_012_CreateRole_RoleName_MaxPlusOne:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_MaxPlusOne_012(self, setup):
        self.logger.info(
            "****************  Test_012 :Test CreateRole when user sends userRoleName with Maximum+1 value(51) ****************")
        print(
            "In Description : TestCase_012: Test CreateRole when user sends userRoleName with Maximum+1 value(51).")
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
        def randStr(chars=string.ascii_uppercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))
        data = randStr(N=35)
        print("String is :::", data)
        self.RolesList.send_userrole_runtime(data)
        self.RolesList.select_Random_roles_checkboxes()
        self.RolesList.select_save_button()
        time.sleep(1)
        try:
            self.RolesList.select_Random_roles_checkboxes()
        except Exception:
            self.RolesList.capture_screenshot()
            self.RolesList.select_Random_roles_checkboxes()
        self.driver.quit()