import json
import random
import pytest

from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createroleAPI
def test_roleName_booleanFields_otherthan_true_false_023():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("**************** In Description: TestCase_023: Test CreateRole by sending all boolean fields other than true or false. ****************")
    print("In Description :Testcase_023: Test CreateRole by sending all boolean fields other than true or false.")
    logger.info("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")
    print("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")

    roleName = random.randint(0, 9)
    print("\n Trying to create role :::", roleName)

    files = readFiles()
    body = files.create_role_body()
    body['createMethod'] = 1
    body['editMethod'] = 1
    body['deleteMethod'] = 0
    body['createActionAlertLevel'] = 1
    body['userRoleName'] = roleName

    com.create_role_negative(body, roleName)

    com.verify_roles_from_sm_with_api(roleName)


