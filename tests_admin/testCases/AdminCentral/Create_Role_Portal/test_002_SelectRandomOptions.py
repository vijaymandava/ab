import time

import allure
import pytest
import random
import string

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.testCases.AdminCentral.Create_Role_Portal.common_role_portal import Common_role_portal
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@allure.severity(allure.severity_level.NORMAL)
class Test_002_Select_random_options:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_select_random_options_002(self,setup):
        com = Common_role_portal()
        self.logger.info("****************  Test_002_Test CreateRole when userClick ADD button and select random options.  ****************")
        print(
                    "In Description : TestCase_002: Test CreateRole when userClick ADD button and select random options.")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        print("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        self.RolesList = roles(self.driver)
        self.RolesList.select_roles()
        time.sleep(2)
        self.RolesList.verify_AdminCentral_RolesList_header()
        self.RolesList.select_add_role_button()
        self.RolesList.select_system_from_dropdown()
        # self.RolesList.send_Random_RoleName()
        def randStr(chars=string.ascii_uppercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        data = randStr(N=20)
        print("String is :::", data)
        self.RolesList.send_userrole_runtime(data)
        self.RolesList.select_Random_roles_checkboxes()
        self.RolesList.select_save_button()
        self.RolesList.search_toastify(data)
        self.RolesList.verify_cm_ui_positive(data)
        try:
            self.RolesList.select_add_role_button()
        except Exception:
            self.RolesList.capture_screenshot()
            self.RolesList.select_add_role_button()
            self.driver.quit()
        self.RolesList.verify_roles_from_sm_with_api(data)

        self.driver.quit()


