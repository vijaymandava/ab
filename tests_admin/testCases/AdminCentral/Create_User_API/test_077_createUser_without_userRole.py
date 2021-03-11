import pytest
import requests
import json
from xeger import Xeger

from tests_admin.Field_Validations.username_field_validations import username_field_validations
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createUser_without_userName_009():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("**************** In Description : TestCase_009: Test createUser -  request without userRole in the JSON ****************")
    print("In Description :TestCase_009: Test createUser -  request without userRole in the JSON")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164287?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164287?projectId=50")

    user = username_field_validations()
    userName = user.username_regex()
    print('UserRole is not sending in the body')
    body = {
    "editedBy": "vijay", "userName": "Operator", "firstName": "v", "middleInitial":"i", "lastName":"j",
    "emailAddress": "abc@abc.com", "telephoneNumber": "123456", "extension": "5309", "password": 'Password123',
    "confirmPassword": 'Password123', "deactivated": 'false',
    "hidden": 'false', "isADUser": 'true'
    }

    com.create_user_negative(body, userName)

    com.verify_users_from_sm_with_api(userName)
