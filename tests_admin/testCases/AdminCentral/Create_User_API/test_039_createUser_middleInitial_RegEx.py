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
def test_createUser_middleInitial_RegEx_039():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("****************  Test_039: Test CreateUser when user sends  -  MiddleInitial RegEx ****************")
    print("In Description :Test_039: Test CreateUser when user sends  -  MiddleInitial RegEx")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    # URL
    url = ReadConfig.sm()

    # Additional headers.
    headers = com.headers()

    # Body
    x = Xeger(limit=10)
    name = com.userName_RegEx()
    middle=com.middleInitial_RegEx()
    userName = x.xeger(name)
    y = Xeger(limit=1)
    middleInitial=y.xeger(middle)

    file = open("./tests_admin/testCases/create_user_api.json", 'r')
    body = json.loads(file.read())
    body['middleInitial'] = middleInitial
    body['userName'] = userName

    com.create_user_positive(body, userName)

    com.verify_users_from_sm_with_api(userName)

    e = com.verify_user_options(userName)
    assert e['userName'] == userName
    assert e['firstName'] == 'v'
    assert e['middleInitial'] == middleInitial
    assert e['lastName'] == 'j'
    assert e['emailAddress'] == 'abc@def.com'
    assert e['telephoneNumber'] == '23'
    assert e['extension'] == '5309'
    assert e['password'] == 'Password123'
    assert e['userRoleName'] == 'Operator'
    assert e['deactivated'] == False
    assert e['hidden'] == False
    assert e['isADUser'] == False
    print("All the options are matched with the request")
