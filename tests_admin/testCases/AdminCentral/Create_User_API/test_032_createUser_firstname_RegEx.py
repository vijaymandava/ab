import pytest
from xeger import Xeger

from tests_admin.Field_Validations.username_field_validations import username_field_validations
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createUser_firstName_RegEx_032():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("****************  Test_032: Test CreateUser when user sends  -  firstName with RegEx ****************")
    print("In Description :Test_032: Test CreateUser when user sends  -  firstName with RegEx")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")

    x = Xeger(limit=15)
    firstname=com.firstName_RegEx()
    FirstName=x.xeger(firstname)

    user = username_field_validations()
    userName = user.username_regex()
    file_body = readFiles()
    body = file_body.create_user_body()
    body['userName'] = userName
    body['firstName'] = FirstName

    com.create_user_positive(body, userName)

    com.verify_users_from_sm_with_api(userName)

    e = com.verify_user_options(userName)
    assert e['userName'] == userName
    assert e['firstName'] == FirstName
    assert e['middleInitial'] == 'i'
    assert e['lastName'] == 'j'
    assert e['emailAddress'] == 'abc@def.com'
    assert e['telephoneNumber'] == '23'
    assert e['extension'] == '5309'
    assert e['password'] == 'Password123'
    assert e['userRoleName'] == 'Operator'
    assert e['deactivated'] == False
    assert e['hidden'] == False
    assert e['isADUser'] == False
    print("All the options are matched with the request")
