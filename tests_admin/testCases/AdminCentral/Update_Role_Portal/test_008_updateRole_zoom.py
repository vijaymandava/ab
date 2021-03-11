import pytest
import time

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Test_008_UpdateRole_Zoom:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.updaterole
    def test_updateRole_zoom_008(self,setup):
        self.logger.info("****************  Test_008 : Test UpdateRole when user  access after  Zoomin/ZoomOut ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164242?projectId=50")
    print("****************  Test_046: Test Default fieldService and its default User Role Settings ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164242?projectId=50")
