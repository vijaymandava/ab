import json

import pytest

from tests_admin.Field_Validations.userRoleName_field_validations import userRoleName_field_validations
from tests_admin.Field_Validations.username_field_validations import username_field_validations
from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createroleAPI
def test_roleName_javascript_011():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("**************** IN Description : TestCase_011: Test CreateRole when user sends  - 'userRoleName' with values :: javascript ****************")
    print("In Description :Testcase_011: Test CreateRole when user sends  - userRoleName with values :: javascript")
    logger.info("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")
    print("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")

    role = userRoleName_field_validations()
    roleName = role.userRolename_javascript()
    files = readFiles()
    body = files.create_role_body()
    body['userRoleName'] = roleName

    com.create_role_negative(body, roleName)

    com.verify_roles_from_sm_with_api(roleName)

