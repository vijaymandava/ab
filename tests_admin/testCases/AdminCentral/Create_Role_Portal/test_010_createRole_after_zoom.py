import time

import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.testCases.AdminCentral.Create_Role_Portal.common_role_portal import Common_role_portal
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

class Test_010_CreateRole_After_Zoom:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_createRole_after_zoom_010(self, setup):
        self.logger.info("****************  Test_010 : Test CreateRole after zoom ****************")
        print("In Description : TestCase_010: Test CreateRole after zoom")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        print("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        time.sleep(10)
        self.RolesList = roles(self.driver)
        self.RolesList.select_roles_after_zoom()
        time.sleep(2)
        self.RolesList.verify_AdminCentral_RolesList_header()
        self.RolesList.select_add_role_button_after_zoom()
        self.RolesList.select_system_from_dropdown()
        creating_role = self.RolesList.send_Random_RoleName()
        self.RolesList.selectAll_checkbox_after_zoom()
        self.RolesList.select_save_button_after_zoom()
        self.RolesList.search_toastify(creating_role)
        self.RolesList.verify_cm_ui_positive(creating_role)
        try:
            self.RolesList.select_add_role_button()
        except Exception:
            self.RolesList.capture_screenshot()
            self.RolesList.select_add_role_button()
        self.driver.quit()






