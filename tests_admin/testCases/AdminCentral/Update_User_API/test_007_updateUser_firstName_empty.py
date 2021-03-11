import json
import random
import pytest
from tests_admin.testCases.AdminCentral.Update_User_API.common_updateUser_api import common_updateUser_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateuserAPI
def test_updateUser_firstName_empty_007():
    logger = LogGen.loggen()
    com = common_updateUser_api()
    logger.info("****************  Test_007: Test updateUser when user sends FirstName value as Empty")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")
    print("****************  Test_007: Test updateUser when user sends FirstName value as Empty")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")

    # Body
    list = com.getUsersList()
    userName = random.choice(list)
    print("Updating user ::", userName)
    print("FirstName is sending as empty to updateUser")

    file = open("./tests_admin/testCases/update_user_api.json", 'r')
    body = json.loads(file.read())
    body['userName'] = userName
    body['firstName'] = ""

    body = {
        "editedBy": "Admin", "userName": userName, "firstName": "", "middleInitial": "m", "lastName": "mandava",
        "emailAddress": "vijay@rmb.com", "telephoneNumber": "603-555-1212", "extension": "5309", "password": "Password123",
        "confirmPassword": "Password123", "userRoleName": "FieldService", "deactivated": 'false',
        "hidden": 'false', "isADUser": 'true'
    }
    com.update_user_negative(body, userName)

    com.verify_updated_user_from_sm_with_api(userName)

    # com.verify_updated_user_from_sm_UI(userName)