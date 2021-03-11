import pytest
import random
from tests_admin.Field_Validations.username_field_validations import username_field_validations
from tests_admin.utilities.customLogger import LogGen
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api
from tests_admin.utilities.readExternalFiles import readFiles


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_changeParameter_true_to_false_002():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("****************  Test_002: Test CreateUser when user sends  - Change the parameter values inside body.(True to false and false to true) ****************")
    print("In Description : Test_002: Test CreateUser when user sends  - Change the parameter values inside body.(True to false and false to true) ")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")

    # Body
    user = username_field_validations()
    userName = user.username_regex()

    list = ['true', 'false']
    a=random.choice(list)
    print("\n Sending isADUser as ::", a)
    print("\n Trying creating username   ::", userName)

    file_body = readFiles()
    body = file_body.create_user_body()
    body['userName'] = userName
    body['isADuser'] = a

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
    assert e['userRoleName'] == 'Administrator'
    assert e['deactivated'] == False
    assert e['hidden'] == False
    print("All the options are matched with the request")