import json
import random
import pytest

from tests_admin.testCases.AdminCentral.Update_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateroleAPI
def test_updateRole_002():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("****************  Test_002: Test updateRole when user sends  -  request body by changing parameters true/false ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    print("****************  Test_002: Test updateRole when user sends  -  request body by changing parameters true/false ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    # Body
    list = com.getRolesList()
    roleName = random.choice(list)
    print("\n Updating Role ::", roleName)
    list1=['true','false']
    boolean_value=random.choice(list1)

    file = open("./tests_admin/testCases/update_role_api.json", 'r')
    body = json.loads(file.read())
    body['createMethod'] = boolean_value
    body['deleteMethod'] = boolean_value
    body['createActionAlertLevel'] = boolean_value
    body['editActionAlertLevel'] = boolean_value
    body['createHandlingRule'] = boolean_value
    body['userRoleName'] = roleName

    com.update_role_positive(body, roleName)

    com.verify_updated_role_from_sm_with_api(roleName)

    # com.verify_updated_roles_from_sm_UI(roleName)

