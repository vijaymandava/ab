import pytest
import time
from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.testCases.AdminCentral.Create_Role_Portal.common_role_portal import Common_role_portal
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig
import random
import string

from tests_admin.utilities.customLogger import LogGen


class Test_013_CreateRole_RoleName_SpacesInBetween:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_roleName_SpacesInBetween_013(self, setup):

        self.logger.info("****************  test_013 ::  Test CreateRole when user sends RoleName with keeping spaces in between value ****************")
        print(
            "In Description : TestCase_013 ::  Test CreateRole when user sends RoleName with keeping spaces in between value.")
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
        def randStr(chars=string.ascii_uppercase+' '+' ', N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        data = randStr(N=34)
        print("String is :::", data)
        self.RolesList.send_userrole_runtime(data)
        self.RolesList.select_Random_roles_checkboxes()
        self.RolesList.select_save_button()
        self.RolesList.search_toastify(data)
        self.RolesList.verify_cm_ui_positive(data)
        com = Common_role_portal()
        com.verify_roles_from_sm_with_api(data)

        time.sleep(1)
        try:
            self.RolesList.select_add_role_button()
        except Exception:
            self.RolesList.capture_screenshot()
            self.RolesList.select_add_role_button()
        self.driver.quit()
