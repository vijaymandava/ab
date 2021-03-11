import time

import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.testCases.AdminCentral.Create_Role_Portal.common_role_portal import Common_role_portal
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

class Test_createRole_with_keyBoard_shiftTab_008:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_createRole_with_keyBoard_shiftTab_008(self, setup):
        self.logger.info("****************  Test_008 : Test CreateRole when user use Key Board shiftTab ****************")
        print("In Description : TestCase_007: Test CreateRole when user use Key Board shiftTab")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        print("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        time.sleep(10)
        self.RolesList = roles(self.driver)
        self.RolesList.select_roles_with_keyboard_shiftTab()
        time.sleep(2)
        self.RolesList.verify_AdminCentral_RolesList_header()
        self.RolesList.select_add_role_button_with_keyboard_shiftTab()
        self.RolesList.select_system_from_dropdown()
        creating_role = self.RolesList.send_Random_RoleName()
        self.RolesList.select_total_checkboxes_with_KeyBoard_shiftTab()
        self.RolesList.select_save_button()
        self.RolesList.search_toastify(creating_role)
        self.RolesList.verify_cm_ui_positive(creating_role)
        com = Common_role_portal()
        com.verify_roles_from_sm_with_api(creating_role)
        try:
            self.RolesList.select_add_role_button()
        except Exception:
            self.RolesList.capture_screenshot()
            self.RolesList.select_add_role_button()
        self.driver.quit()