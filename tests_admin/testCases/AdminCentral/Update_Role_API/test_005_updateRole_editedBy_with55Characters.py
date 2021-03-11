import json
import random
import pytest

from tests_admin.testCases.AdminCentral.Update_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateroleAPI
def test_updateRole_editBy_with_55Characters_005():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("****************  Test_005: Test updateRole when user sends  -  editBy with 55 characters ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    print("****************  Test_005: Test updateRole when user sends  -  editBy with 55 characters ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    url = ReadConfig.sm()
    # Additional headers.
    headers = com.headers()
    # Body
    list = com.getRolesList()
    roleName = random.choice(list)
    print("\n Updating Role ::", roleName)

    file = open("./tests_admin/testCases/update_role_api.json", 'r')
    body = json.loads(file.read())
    body['editedBy'] = 'abcde12345abcde12345abcde12345abcde12345abcde12345abcde'
    body['userRoleName'] = roleName

    com.update_role_negative(body, roleName)

    com.verify_updated_role_from_sm_with_api(roleName)

    # com.verify_updated_roles_from_sm_UI(roleName)

