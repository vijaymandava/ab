import json
import random
import pytest
from tests_admin.testCases.AdminCentral.Update_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateroleAPI
def test_updateRole_006():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("****************  Test_006: Test updateRole when user sends  -  editedBy empty Request ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    print("****************  Test_006: Test updateRole when user sends  -  editedBy empty Request ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    # Body
    list = com.getRolesList()
    roleName = random.choice(list)
    print("\n Updating Role - editedBy as null::", roleName)

    file = open("./tests_admin/testCases/update_role_api.json", 'r')
    body = json.loads(file.read())
    body['editedBy'] = ''
    body['userRoleName'] = roleName

    com.update_role_negative(body, roleName)

    com.verify_updated_role_from_sm_with_api(roleName)

    # com.verify_updated_roles_from_sm_UI(roleName)
