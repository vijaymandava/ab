import json
import random
import pytest

from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createroleAPI
def test_roleName_without_EditByField_022():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("****************  IN Description: TestCase_022: Test CreateRole by sending EditedBy='whitespaces'. ****************")
    print("In Description :Testcase_022: Test CreateRole by sending EditedBy='whitespaces'")
    logger.info("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")
    print("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")

    roleName = random.randint(0, 9)
    print("\n Trying to create role :::", roleName)

    files = readFiles()
    body = files.create_role_body()
    body['editedBy'] = ''
    body['userRoleName'] = roleName

    com.create_role_negative(body, roleName)

    com.verify_roles_from_sm_with_api(roleName)


