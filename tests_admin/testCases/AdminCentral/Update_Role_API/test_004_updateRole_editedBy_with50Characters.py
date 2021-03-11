import json
import random
import pytest

from tests_admin.testCases.AdminCentral.Update_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateroleAPI
def test_updateRole_editBy_with50Characters_004():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("****************  Test_004: Test updateRole when user sends  -  editBy with 50 characters ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    print("****************  Test_004: Test updateRole when user sends  -  editBy with 50 characters ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    list = com.getRolesList()
    roleName = random.choice(list)
    print("\n Updating Role ::", roleName)

    file = open("./tests_admin/testCases/update_role_api.json", 'r')
    body = json.loads(file.read())
    body['editedBy'] = 'abcde12345abcde12345abcde12345abcde12345abcde12345'
    body['userRoleName'] = "vijay"

    com.update_role_positive(body, roleName)

    com.verify_updated_role_from_sm_with_api(roleName)

    e = com.verify_update_roleName_options(roleName)

    assert e['createMethod'] == True
    assert e['editMethod'] == True
    assert e['deleteMethod'] == True
    assert e['createActionAlertLevel'] == True
    assert e['editActionAlertLevel'] == True
    assert e['deleteActionAlertLevel'] == True
    assert e['createHandlingRule'] == True
    assert e['editHandlingRule'] == True
    assert e['deleteHandlingRule'] == True
    assert e['createSample'] == False
    assert e['editSample'] == False
    assert e['deleteSample'] == False
    assert e['createProduct'] == False
    assert e['editProduct'] == False
    assert e['deleteProduct'] == False
    assert e['createUser'] == False
    assert e['editUser'] == False
    assert e['deleteUser'] == False
    assert e['createUserRole'] == False
    assert e['editUserRole'] == False
    assert e['deleteUserRole'] == False
    assert e['cancelCassettes'] == True
    assert e['retrieveCassettes'] == True
    assert e['approveCassettes'] == True
    assert e['cleanupCassettes'] == True
    assert e['orderTests'] == True
    assert e['loadTests'] == True
    assert e['printProductLabels'] == True
    assert e['administerGD'] == False
    assert e['editSettings'] == False
    assert e['maintenance'] == False
    assert e['acknowledgeSystemAlarms'] == True
    assert e['acknowledgeSystemErrors'] == True
    assert e['acknowledgeSystemServiceIssues'] == True
    assert e['editAlarmNotifications'] == False
    assert e['emptyTrash'] == True
    assert e['service'] == False
    assert e['editITSettings'] == False
    assert e['editLimsSettings'] == False
    assert e['printLimsLabels'] == False
    assert e['modifyLimsRequest'] == False
    assert e['editLimsTestResultsFields'] == False
    assert e['sendSystemLogs'] == True

    # com.verify_updated_roles_from_sm_UI(roleName)


