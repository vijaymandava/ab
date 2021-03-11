import json

import pytest
from xeger import Xeger
from tests_admin.testCases.AdminCentral.Update_User_API.common_updateUser_api import common_updateUser_api
from tests_admin.utilities.customLogger import LogGen


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateuserAPI
def test_updateUser_userRole_administrator_044():
    logger = LogGen.loggen()
    com = common_updateUser_api()
    logger.info("****************  Test_044: Test Default Administrator and its default User Role Settings ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")
    print("****************  Test_044: Test Default Administrator and its default User Role Settings ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")
    # Body
    userName = 'Administrator'
    print("updating username ::: Administrator")

    file = open("./tests_admin/testCases/update_user_api.json", 'r')
    body = json.loads(file.read())
    body['userName'] = userName
    body['userRoleName'] = userName

    com.update_user_negative(body, userName)

    com.verify_updated_user_from_sm_with_api(userName)

    # com.verify_updated_user_from_sm_UI(userName)
