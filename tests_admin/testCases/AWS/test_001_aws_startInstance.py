import pytest
import time
import allure

from tests_admin.testCases.AWS.common_aws_methods import Common_Aws_Methods
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@allure.severity(allure.severity_level.BLOCKER)
class Test_001_AWS_StartInstance:
    baseURL = ReadConfig.get_aws_vijay_sm()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_aws_startInstance_001(self,setup):
        self.logger.info("****************  Test_001 : verify AWS Start Instance ****************")
        print("Test_001 : verify AWS Start Instance ")
        self.driver=setup
        self.driver.get(self.baseURL)
        driver = self.driver
        self.login = Common_Aws_Methods(self.driver)
        self.login.aws_login()
        time.sleep(2)
        self.login.startInstance()
        time.sleep(2)
        self.driver.quit()
