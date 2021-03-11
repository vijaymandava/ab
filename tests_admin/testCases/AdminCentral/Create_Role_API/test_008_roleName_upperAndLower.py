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
def test_roleName_upperAndLowerCase_008():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("****************  IN Description: TestCase_008: Test CreateRole when user sends  - 'userRoleName' with values :: upper and lowercase alphabets(Aa-zZ) ****************")
    print("In Description :Testcase_008: Test CreateRole when user sends  - 'userRoleName' with values :: upper and lowercase alphabets(Aa-zZ)")
    logger.info("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")
    print("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")

    role = userRoleName_field_validations()
    roleName = role.userRolename_upper_lower()
    files = readFiles()
    body = files.create_role_body()
    body['userRoleName'] = roleName

    com.create_role_positive(body, roleName)

    com.verify_roles_from_sm_with_api(roleName)

    e = com.verify_roleName_options(roleName)
    assert e['userRoleName'] == roleName
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
    print("All the options are verified and match with the request")
