import json
import random
import pytest

from tests_admin.testCases.AdminCentral.Update_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateroleAPI
def test_updateRole_with_minimum_JSONBody_009():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("****************  Test_009: Test updateRole when user sends  -  Valid Request with minimum Json Body****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    print("****************  Test_009: Test updateRole when user sends  -  Valid Request with minimum Json Body****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    # Body
    list = com.getRolesList()
    roleName = random.choice(list)
    print("\n Updating Role ::", roleName)

    file = open("./tests_admin/testCases/update_role_api.json", 'r')
    body = json.loads(file.read())
    body['deleteMethod'] = ''
    body['userRoleName'] = roleName

    # body = {'editedBy': 'admin', 'userRoleName': roleName, 'createMethod': 'true', 'editMethod': 'true',
    #      'deleteMethod': 'true',
    #      'createActionAlertLevel': 'true', 'editActionAlertLevel': 'true', 'deleteActionAlertLevel': 'true',
    #      'createHandlingRule': 'true', 'editHandlingRule': 'true', 'deleteHandlingRule': 'true',
    #      'createSample': 'false', 'editSample': 'false', 'deleteSample': 'false', 'createProduct': 'false',
    #      'editProduct': 'false', 'deleteProduct': 'false', 'createUser': 'false', 'editUser': 'false',
    #      'deleteUser': 'false', 'createUserRole': 'false', 'editUserRole': 'false', 'deleteUserRole': 'false',
    #      'cancelCassettes': 'true', 'retrieveCassettes': 'true', 'approveCassettes': 'true', 'cleanupCassettes': 'true',
    #      'orderTests': 'true', 'loadTests': 'true', 'printProductLabels': 'true', 'administerGD': 'false',
    #      'editSettings': 'false', 'maintenance': 'false', 'acknowledgeSystemAlarms': 'true',
    #      'acknowledgeSystemErrors': 'true', 'acknowledgeSystemServiceIssues': 'true', 'editAlarmNotifications': 'false',
    #      'emptyTrash': 'true', 'service': 'false', 'editITSettings': 'false', 'editLimsSettings': 'false',
    #      'printLimsLabels': 'false', 'modifyLimsRequest': 'false', 'editLimsTestResultsFields': 'false'
    #     }

    com.update_role_negative(body, roleName)

    com.verify_updated_role_from_sm_with_api(roleName)

    # com.verify_updated_roles_from_sm_UI(roleName)

