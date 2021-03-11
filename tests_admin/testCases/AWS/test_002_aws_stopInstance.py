import pytest
import time
import allure

from tests_admin.testCases.AWS.common_aws_methods import Common_Aws_Methods
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@allure.severity(allure.severity_level.BLOCKER)
class Test_002_AWS_StopInstance:
    # baseURL = ReadConfig.get_aws_vijay_sm()
    baseURL = ReadConfig.get_aws_vijay_win10_sm()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_aws_stopInstance_002(self,setup):
        self.logger.info("****************  Test_002 : verify AWS Stop Instance ****************")
        print("Test_002 : verify AWS Stop Instance ")
        self.driver=setup
        self.driver.get(self.baseURL)
        driver = self.driver
        self.login = Common_Aws_Methods(self.driver)
        self.login.aws_login()
        time.sleep(2)
        self.login.stopInstance()
        time.sleep(2)
        self.driver.quit()
