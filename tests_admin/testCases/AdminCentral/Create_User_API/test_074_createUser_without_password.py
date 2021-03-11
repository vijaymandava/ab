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
def test_createUser_without_password_006():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("**************** In Description : Test_006: Test CreateUser when user sends  - without Password ****************")
    print("In Description :Test_006 :Test CreateUser when user sends  - without Password")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164287?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164287?projectId=50")

    # Body
    user = username_field_validations()
    userName = user.username_regex()

    print(" Password field is not sending in the Body")
    body = {
    "editedBy": "vijay", "userName": userName, "firstName": "v", "middleInitial":"i", "lastName":"j",
    "emailAddress": "abc@abc.com", "telephoneNumber": "123456", "extension": "5309",
    "confirmPassword": 'Password123', "userRoleName": "Operator", "deactivated": 'false',
    "hidden": 'false', "isADUser": 'true'
    }

    com.create_user_negative(body, userName)

    com.verify_users_from_sm_with_api(userName)
