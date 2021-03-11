import pytest
import time

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Test_002_UpdateRole_Select_Edit_Select_Close:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.updaterole
    def test_updateRole_select_edit_select_close_002(self,setup):
        self.logger.info("****************  Test_002 : Test UpdateRole when user  - Click 'Edit' button and cancel role. ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164242?projectId=50")
        print("****************  Test_002 : Test UpdateRole when user  - Click 'Edit' button and cancel role. ****************")
        print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164242?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.RolesList = roles(self.driver)
        self.RolesList.select_roles()
        time.sleep(5)

        self.RolesList.verify_AdminCentral_RolesList_header()
        self.RolesList.select_edit_role_button()
        self.RolesList.select_close_button()
        time.sleep(2)

        try:
           self.RolesList.select_edit_role_button()
        except Exception:
            self.RolesList.verify_error()
            self.RolesList.capture_screenshot()
            self.RolesList.select_edit_role_button()

        self.driver.quit()






