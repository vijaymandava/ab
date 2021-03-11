import json
import random
import pytest

from tests_admin.testCases.AdminCentral.Update_User_API.common_updateUser_api import common_updateUser_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateuserAPI
def test_updateUser_phoneNumber_empty_030():
    logger = LogGen.loggen()
    com = common_updateUser_api()
    logger.info("****************  Test_030: Test updateUser when user sends  -  telephone value as empty ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")
    print("****************  Test_030: Test updateUser when user sends  -  telephone value as empty ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")

    # Body
    list = com.getUsersList()
    userName = random.choice(list)
    print("Updating user ::", userName)

    file = open("./tests_admin/testCases/update_user_api.json", 'r')
    body = json.loads(file.read())
    body['userName'] = userName
    body['telephoneNumber'] = ''

    com.update_user_positive(body, userName)

    com.verify_updated_user_from_sm_with_api(userName)

    # com.verify_updated_user_from_sm_UI(userName)

