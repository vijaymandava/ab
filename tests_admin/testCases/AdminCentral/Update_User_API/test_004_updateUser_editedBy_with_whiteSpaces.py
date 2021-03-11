import json
import random
import pytest

from tests_admin.testCases.AdminCentral.Update_User_API.common_updateUser_api import common_updateUser_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateuserAPI
def test_updateUser_userName_editedBy_with_whiteSpaces_004():
    logger = LogGen.loggen()
    com = common_updateUser_api()
    logger.info("****************  Test_004: Test updateUser when user sends EditedBy values with whiteSpaces  ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")
    print("****************  Test_004: Test updateUser when user sends EditedBy values with whiteSpaces  ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")

    # Body
    list = com.getUsersList()
    userName = random.choice(list)
    print("Updating user ::", userName)
    print("EditedBy value is updating with whiteSpaces")

    file = open("./tests_admin/testCases/update_user_api.json", 'r')
    body = json.loads(file.read())
    body['userName'] = userName
    body['editedBy'] = '   '

    body = {
        "editedBy": "    ", "userName": userName, "firstName": "vijay", "middleInitial": "m", "lastName": "mandava",
        "emailAddress": "vijay@rmb.com", "telephoneNumber": "603-555-1212", "extension": "5309", "password": "Password123",
        "confirmPassword": "Password123", "userRoleName": "FieldService", "deactivated": 'false',
        "hidden": 'false', "isADUser": 'true'
    }

    com.update_user_negative(body, userName)

    com.verify_updated_user_from_sm_with_api(userName)

    # com.verify_updated_user_from_sm_UI(userName)