import pytest
import requests
import json
from xeger import Xeger
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createUser_userRole_fieldService_068():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("**************** In Description : TestCase_068: Test Default fieldService and its default User Role Settings ****************")
    print("In Description :TestCase_068: Test Default fieldService and its default User Role Settings")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")

    userName = "Fieldservice"

    file_body = readFiles()
    body = file_body.create_user_body()
    body['userRoleName'] = userName
    body['userName'] = userName

    com.create_user_negative(body, userName)

    com.verify_users_from_sm_with_api(userName)
