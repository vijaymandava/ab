import json

import pytest
from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createroleAPI
def test_roleName_without_userRoleNameField_020():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("**************** IN Description: TestCase_020: Test CreateRole when user sends JSON without 'userRoleName'. ****************")
    print("In Description :Testcase_020: Test CreateRole when user sends JSON without 'userRoleName'.")
    logger.info("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")
    print("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")

    roleName = ""
    print("\n Trying to create role :::", roleName)

    files = readFiles()
    body = files.create_role_body()
    body['userRoleName'] = roleName

    com.create_role_negative(body, roleName)

    com.verify_roles_from_sm_with_api(roleName)


