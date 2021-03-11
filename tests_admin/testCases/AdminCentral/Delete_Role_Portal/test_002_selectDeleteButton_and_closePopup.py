import pytest
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Test_002_DeleteRole_SelectDelete_CloseDeletePopup:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.deleterole
    def test_selectDelete_closeDeletePopup_002(self, setup):
        self.logger.info("****************  Test_002 :Test DeleteRole when user Click 'Delete' button and cancel button. ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164245?projectId=50")
        print("****************  Test_002 :Test DeleteRole when user Click 'Delete' button and cancel button. ****************")
        print(
            "Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164245?projectId=50")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.RolesList = roles(self.driver)
        self.RolesList.select_delete_role_button()
        self.RolesList.select_close_button()

