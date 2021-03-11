import pytest
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Test_003_DeleteRole_SelectDelete_and_x:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.deleterole
    def test_selectDelete_and_x_003(self, setup):
        self.logger.info("****************  Test_003 :Test DeleteRole when user Click 'Delete' button and cross(x) button. ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164245?projectId=50")
        print("****************  Test_003 :Test DeleteRole when user Click 'Delete' button and cross(x) button. ****************")
        print(
            "Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164245?projectId=50")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.RolesList = roles(self.driver)
        self.RolesList.select_delete_role_button()
        self.RolesList.select_closeSymbol_mark()

