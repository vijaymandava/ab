import random
import pytest
from tests_admin.testCases.AdminCentral.Update_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateroleAPI
def test_updateRole_without_editedBy_015():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("****************  Test_015: Test updateRole when user sends  -  Request without editedBy ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    print("****************  Test_015: Test updateRole when user sends  -  Request without editedBy ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    # Body
    list = com.getRolesList()
    roleName = random.choice(list)
    print("\n Updating Role ::", roleName)

    body = { 'userRoleName': roleName, 'createMethod': 'true', 'editMethod': 'true',
         'deleteMethod': 'true',
         'createActionAlertLevel': 'true', 'editActionAlertLevel': 'true', 'deleteActionAlertLevel': 'true',
         'createHandlingRule': 'true', 'editHandlingRule': 'true', 'deleteHandlingRule': 'true',
         'createSample': 'false', 'editSample': 'false', 'deleteSample': 'false', 'createProduct': 'false',
         'editProduct': 'false', 'deleteProduct': 'false', 'createUser': 'false', 'editUser': 'false',
         'deleteUser': 'false', 'createUserRole': 'false', 'editUserRole': 'false', 'deleteUserRole': 'false',
         'cancelCassettes': 'true', 'retrieveCassettes': 'true', 'approveCassettes': 'true', 'cleanupCassettes': 'true',
         'orderTests': 'true', 'loadTests': 'true', 'printProductLabels': 'true', 'administerGD': 'false',
         'editSettings': 'false', 'maintenance': 'false', 'acknowledgeSystemAlarms': 'true',
         'acknowledgeSystemErrors': 'true', 'acknowledgeSystemServiceIssues': 'true', 'editAlarmNotifications': 'false',
         'emptyTrash': 'true', 'service': 'false', 'editITSettings': 'false', 'editLimsSettings': 'false',
         'printLimsLabels': 'false', 'modifyLimsRequest': 'false', 'editLimsTestResultsFields': 'false',
         'sendSystemLogs': 'true'}

    com.update_role_negative(body, roleName)

    com.verify_updated_role_from_sm_with_api(roleName)

    # com.verify_updated_roles_from_sm_UI(roleName)


