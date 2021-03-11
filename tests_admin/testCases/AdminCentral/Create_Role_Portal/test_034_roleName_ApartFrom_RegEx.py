import time

import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

class Test_034_roleName_ApartFrom_RegEx:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_roleName_ApartFrom_RegEx_034(self,setup):
        self.logger.info("****************  Test_034 :: Test CreateRole by sending the userRoleName apart from  ^[a-zA-Z0-9\-_()'.#\\+ ]*$  (ex:- ?,@ etc.,)  ****************")
        print(
            "In Description : TestCase_034 :: Test CreateRole by sending the userRoleName apart from  ^[a-zA-Z0-9\-_()'.#\\+ ]*$  (ex:- ?,@ etc.,)  ")
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
        list={".", "!", "@", "=", "$", "%", "^", "&", "*", "~", ":", ";", "/", "/", "?", "]", "[", "|"}
        for i in list:
            print(i)
            self.RolesList.send_userrole_runtime(i)
            self.RolesList.select_save_button()
            time.sleep(5)
            try:
                self.RolesList.get_error()
            except Exception:
                self.RolesList.capture_screenshot()
                self.RolesList.select_save_button()
        self.driver.quit()



