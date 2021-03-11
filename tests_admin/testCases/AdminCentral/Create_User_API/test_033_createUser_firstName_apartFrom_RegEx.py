import pytest
import requests
import json
from xeger import Xeger
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createUser_firstName_apartFrom_RegEx_033():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("****************  Test_033: Test CreateUser when user sends  -  firstName apart From RegEx ****************")
    print("In Description :Test_033: Test CreateUser when user sends  -  firstName apart From RegEx")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    # URL
    url = ReadConfig.sm()

    # Additional headers.
    headers = com.headers()

    # Body
    x = Xeger(limit=15)
    name = com.userName_RegEx()
    userName = x.xeger(name)
    list = {".", "!", "@", "=", "$", "%", "^", "&", "*", "~", ":", ";", "/", "/", "?", "]", "[", "|"}
    for i in list:
        file = open("./tests_admin/testCases/create_user_api.json", 'r')
        print("Sending firstname ::"+i)
        body = json.loads(file.read())
        body['firstName'] = i
        body['userName'] = userName

        com.create_user_negative(body, userName)

        com.verify_users_from_sm_with_api(userName)

