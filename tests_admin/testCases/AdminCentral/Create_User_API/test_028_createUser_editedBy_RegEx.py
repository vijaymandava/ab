import pytest

from tests_admin.Field_Validations.editedby_field_validations import editedby_field_validations
from tests_admin.Field_Validations.username_field_validations import username_field_validations
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createUser_editedBy_RegEx_028():
    logger = LogGen.loggen()
    com = common_createUser_api()
    file_body = readFiles()
    logger.info("****************  Test_028: Test CreateUser when user sends  -  EditedBy with RegEx ****************")
    print("In Description :Test_028: Test CreateUser when user sends  -  EditedBy with RegEx")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")

    # Body
    user = username_field_validations()
    userName = user.username_regex()
    edit = editedby_field_validations()
    editedBy = edit.editedby_regex()
    body = file_body.create_user_body()
    body['userName'] = userName
    body['editedBy'] = editedBy

    com.create_user_positive(body, userName)

    com.verify_users_from_sm_with_api(userName)

    e = com.verify_user_options(userName)
    assert e['userName'] == userName
    assert e['firstName'] == 'v'
    assert e['middleInitial'] == 'i'
    assert e['lastName'] == 'j'
    assert e['emailAddress'] == 'abc@def.com'
    assert e['telephoneNumber'] == '23'
    assert e['extension'] == '5309'
    assert e['password'] == 'Password123'
    assert e['userRoleName'] == 'Operator'
    assert e['deactivated'] == False
    assert e['hidden'] == False
    assert e['isADUser'] == True
    print("All the options are matched with the request")
