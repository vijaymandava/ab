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
def test_createUser_middleInitial_apartFrom_RegEx_040():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("****************  Test_040: Test CreateUser when user sends  -  middleInitial apart from RegEx ****************")
    print("In Description : Test_040: Test CreateUser when user sends  -  middleInitial apart from RegEx ")
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

        file_body = readFiles()
        body = file_body.create_user_body()
        print("Sending middleInitial as :"+i)
        body['middleInitial'] = i
        body['userName'] = userName

        com.create_user_negative(body, userName)

        com.verify_users_from_sm_with_api(userName)
