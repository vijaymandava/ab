import pytest
import time
import allure

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@allure.severity(allure.severity_level.BLOCKER)
class Test_001_CreateRole:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_createRole_001(self,setup):
        self.logger.info("****************  Test_001 : Test CreateRole when user Click ADD button and add name then save role. ****************")
        print("In Description : TestCase_001: Test CreateRole when user Click ADD button and add name then save role.")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        print("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        time.sleep(10)
        self.RolesList = roles(self.driver)
        self.RolesList.select_roles()
        time.sleep(2)
        self.RolesList.verify_AdminCentral_RolesList_header()
        self.RolesList.select_add_role_button()
        self.RolesList.select_system_from_dropdown()
        creating_role=self.RolesList.send_Random_RoleName()
        self.RolesList.selectAll_checkbox()
        self.RolesList.select_save_button()
        self.RolesList.search_toastify(creating_role)
        self.RolesList.verify_cm_ui_positive(creating_role)
        try:
            self.RolesList.select_add_role_button()
        except Exception:
            self.RolesList.capture_screenshot()
            self.RolesList.select_add_role_button()
        self.driver.quit()

        self.RolesList.verify_roles_from_sm_with_api(creating_role)
        e = self.RolesList.verify_roleName_options(creating_role)
        assert e['userRoleName'] == creating_role
        assert e['createMethod'] == True
        assert e['editMethod'] == True
        assert e['deleteMethod'] == True
        assert e['createActionAlertLevel'] == True
        assert e['editActionAlertLevel'] == True
        assert e['deleteActionAlertLevel'] == True
        assert e['createHandlingRule'] == True
        assert e['editHandlingRule'] == True
        assert e['deleteHandlingRule'] == True
        assert e['createSample'] == True
        assert e['editSample'] == True
        assert e['deleteSample'] == True
        assert e['createProduct'] == True
        assert e['editProduct'] == True
        assert e['deleteProduct'] == True
        assert e['createUser'] == True
        assert e['editUser'] == True
        assert e['deleteUser'] == True
        assert e['createUserRole'] == True
        assert e['editUserRole'] == True
        assert e['deleteUserRole'] == True
        assert e['cancelCassettes'] == True
        assert e['retrieveCassettes'] == True
        assert e['approveCassettes'] == True
        assert e['cleanupCassettes'] == True
        assert e['orderTests'] == True
        assert e['loadTests'] == True
        assert e['printProductLabels'] == True
        assert e['administerGD'] == True
        assert e['editSettings'] == True
        assert e['maintenance'] == True
        assert e['acknowledgeSystemAlarms'] == True
        assert e['acknowledgeSystemErrors'] == True
        assert e['acknowledgeSystemServiceIssues'] == True
        assert e['editAlarmNotifications'] == True
        assert e['emptyTrash'] == True
        assert e['service'] == True
        assert e['editITSettings'] == True
        assert e['editLimsSettings'] == True
        assert e['printLimsLabels'] == True
        assert e['modifyLimsRequest'] == True
        assert e['editLimsTestResultsFields'] == True
        assert e['sendSystemLogs'] == True
        print("All the options are verified and match with the request")






