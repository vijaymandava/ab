import pytest
import time

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Test_011_UpdateRole_SelectAll_DeselectFew:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.updaterole
    def test_UpdateRole_selectALL_deselectFew_011(self,setup):
        self.logger.info("****************  Test_011 : Test UpdateRole when user selects “select all” option and unchecks some and save. ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164242?projectId=50")
        print("****************  Test_011 : Test UpdateRole when user selects “select all” option and unchecks some and save. ****************")
        print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164242?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.RolesList = roles(self.driver)
        self.RolesList.select_roles()
        time.sleep(10)

        self.RolesList.verify_AdminCentral_RolesList_header()
        self.RolesList.select_edit_role_button()
        self.RolesList.selectAll_checkbox()
        self.RolesList.select_Random_roles_checkboxes()
        self.RolesList.select_save_button()
        time.sleep(2)
        self.RolesList.search_toastify_edit_success()
        self.driver.close()






