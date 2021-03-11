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
def test_createUser_lastname_RegEx_036():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("****************  Test_036: Test CreateUser when user sends  -  lastname RegEx ****************")
    print("In Description :Test_036: Test CreateUser when user sends  -  lastname RegEx")
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
    last=com.lastName_RegEx()
    userName = x.xeger(name)
    lastName=x.xeger(last)

    file = open("./tests_admin/testCases/create_user_api.json", 'r')
    body = json.loads(file.read())
    body['lastName'] = lastName
    body['userName'] = userName

    com.create_user_positive(body, userName)

    com.verify_users_from_sm_with_api(userName)

    e = com.verify_user_options(userName)
    assert e['userName'] == userName
    assert e['firstName'] == 'v'
    assert e['middleInitial'] == 'i'
    assert e['lastName'] == lastName
    assert e['emailAddress'] == 'abc@def.com'
    assert e['telephoneNumber'] == '23'
    assert e['extension'] == '5309'
    assert e['password'] == 'Password123'
    assert e['userRoleName'] == 'Operator'
    assert e['deactivated'] == False
    assert e['hidden'] == False
    assert e['isADUser'] == False
    print("All the options are matched with the request")
