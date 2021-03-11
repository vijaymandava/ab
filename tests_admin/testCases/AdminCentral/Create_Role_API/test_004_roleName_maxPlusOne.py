import json
import random
import string
import pytest

from tests_admin.Field_Validations.userRoleName_field_validations import userRoleName_field_validations
from tests_admin.Field_Validations.username_field_validations import username_field_validations
from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createroleAPI
def test_roleName_maxPlusOne_004():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("**************** IN Description: TestCase_004 : Test CreateRole when user sends  - userRoleName with Maximum+1 value("
                "51) ****************")
    print("**************** IN Description: TestCase_004 : Test CreateRole when user sends  - userRoleName with Maximum+1 value("
                "51) ****************")
    logger.info("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")
    print("jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")

    role = userRoleName_field_validations()
    roleName = role.userRolename_max_plus_one()
    file_body = readFiles()
    body = file_body.create_role_body()
    body['userRoleName'] = roleName

    com.create_role_negative(body, roleName)

    com.verify_roles_from_sm_with_api(roleName)


