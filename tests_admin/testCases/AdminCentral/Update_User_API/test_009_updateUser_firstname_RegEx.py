import json
import random
import pytest

from xeger import Xeger
from tests_admin.testCases.AdminCentral.Update_User_API.common_updateUser_api import common_updateUser_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_updateUser_firstName_RegEx_009():
    logger = LogGen.loggen()
    com = common_updateUser_api()
    logger.info("****************  Test_009: Test updateUser when user sends  -  firstName with RegEx ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")
    print("****************  Test_009: Test updateUser when user sends  -  firstName with RegEx ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")

    # Body
    list = com.getUsersList()
    userName = random.choice(list)
    print("Updating user ::", userName)

    x = Xeger(limit=15)
    firstname=com.firstName_RegEx()
    FirstName=x.xeger(firstname)
    print("FirstName is updating as ::", FirstName)

    file = open("./tests_admin/testCases/update_user_api.json", 'r')
    body = json.loads(file.read())
    body['userName'] = userName
    body['firstName'] = FirstName

    # convert dict to json string by json.dumps() for body data.
    com.update_user_positive(body, userName)

    com.verify_updated_user_from_sm_with_api(userName)

    e = com.verify_update_user_options(userName)
    assert e['firstName'] == FirstName
    assert e['middleInitial'] == 'm'
    assert e['lastName'] == 'mandava'
    assert e['emailAddress'] == 'vijay@rmb.com'
    assert e['telephoneNumber'] == '603-555-1212'
    assert e['extension'] == '5309'
    assert e['password'] == 'Password123'
    assert e['userRoleName'] == 'FieldService'
    assert e['deactivated'] == False
    assert e['hidden'] == False
    assert e['isADUser'] == False

    # com.verify_updated_user_from_sm_UI(userName)