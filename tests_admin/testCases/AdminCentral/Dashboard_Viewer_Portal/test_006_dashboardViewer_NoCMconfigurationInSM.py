import time
import allure
import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_dashboard_viewer import dashboard_viewer
from tests_admin.testCases.conftest import setup
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

@allure.severity(allure.severity_level.BLOCKER)
class Test_006_dashboardViewer_NoCMconfigurationInSM:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.dashboardviewer
    def test_006_dashboardViewer_NoCMconfigurationInSM(self,setup):
        self.logger.info(
            "****************  Test_006:: Test if no CM address is configured in SM. ****************")
        self.logger.info("")
        print(
            "****************  Test_006:: Test if no CM address is configured in SM.   ****************")
        print(
            "Jama link is ::")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        time.sleep(10)

        self.dashboard = dashboard_viewer(self.driver)
        self.dashboard.select_viewer()
        time.sleep(2)
        self.dashboard.verify_dashboard_header()
        self.dashboard.click_dayOption_dropdown()
        self.dashboard.verify_dayOption_dropdown()
        time.sleep(2)
        self.dashboard.select_dayOption_dropdown('30 days')
        time.sleep(2)
        self.dashboard.verify_numberOfInstrument()
        self.dashboard.table_verifyColumn('Instrument Name', '1')
        self.dashboard.table_verifyColumn('Instrument ID', '2')
        self.dashboard.table_verifyColumn('Loaded', '3')
        self.dashboard.table_verifyColumn('Completed', '4')
        self.dashboard.table_verifyColumn('Approved', '5')
        self.dashboard.table_verifyColumn('Failed', '6')
        self.dashboard.table_verifyColumn('Active', '7')
        self.dashboard.table_verifyColumn('Ordered', '8')
        self.dashboard.table_verifyColumn('Last Test Date', '9')


        self.driver.quit()
