import pytest
from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.getroleAPI
def test_getRoles_API_004():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("****************  Test_004: GetRoles  -  Valid Request ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164278?projectId=50")
    print("****************  Test_004: GetRoles  -  Valid Request ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164278?projectId=50")
    roles = com.getRolesList()
    print("\n Roles are:", roles)

