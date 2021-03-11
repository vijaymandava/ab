import pytest
import requests
import json
from tests_admin.testCases.AdminCentral.Update_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateroleAPI
def test_updateRole_without_roleName_012():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("****************  Test_012: Test updateRole when user sends  -  Request without RoleName in JSON ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    print("****************  Test_012: Test updateRole when user sends  -  Request without RoleName in JSON ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164302?projectId=50")
    url = ReadConfig.sm()
    # Additional headers.
    headers = com.headers()
    # Body
    a = {'editedBy': 'admin', 'createMethod': 'true', 'editMethod': 'true',
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
    # convert dict to json string by json.dumps() for body data.
    resp = requests.post(url + '/updateRole', headers=headers, data=json.dumps(a, indent=4))
    print("\nResponse is :::\n", resp.text)
    assert resp.status_code != 200
    logger.info("**************** Role not Updated ****************")
    print(" Role not updated")

