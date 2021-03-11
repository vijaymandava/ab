import json
import random
import pytest
from xeger import Xeger

from tests_admin.testCases.AdminCentral.Update_User_API.common_updateUser_api import common_updateUser_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateuserAPI
def test_updateUser_lastname_RegEx_013():
    logger = LogGen.loggen()
    com = common_updateUser_api()
    logger.info("****************  Test_013: Test updateUser when user sends  -  lastname RegEx ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")
    print("****************  Test_013: Test updateUser when user sends  -  lastname RegEx ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")

    # Body
    list = com.getUsersList()
    userName = random.choice(list)
    print("Updating user ::", userName)

    x = Xeger(limit=15)
    last=com.lastName_RegEx()
    lastName=x.xeger(last)
    print("Updating LastName with RegEx", lastName)

    file = open("./tests_admin/testCases/update_user_api.json", 'r')
    body = json.loads(file.read())
    body['userName'] = userName
    body['lastName'] = lastName

    com.update_user_positive(body, userName)

    com.verify_updated_user_from_sm_with_api(userName)

    e = com.verify_update_user_options(userName)
    assert e['firstName'] == 'vijay'
    assert e['middleInitial'] == 'm'
    assert e['lastName'] == lastName
    assert e['emailAddress'] == 'vijay@rmb.com'
    assert e['telephoneNumber'] == '603-555-1212'
    assert e['extension'] == '5309'
    assert e['password'] == 'Password123'
    assert e['userRoleName'] == 'FieldService'
    assert e['deactivated'] == False
    assert e['hidden'] == False
    assert e['isADUser'] == False


    # com.verify_updated_user_from_sm_UI(userName)
