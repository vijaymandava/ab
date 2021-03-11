import pytest

from tests_admin.pageObjects.common import common
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.getuserAPI
def test_getUser_API_004():
    logger = LogGen.loggen()
    com = common()
    logger.info("****************  Test_004: GetUsers  -  Valid Request ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164290?projectId=50")
    print("****************  Test_004: GetUsers  -  Valid Request ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164290?projectId=50")
    com.getUsersList()