import pytest
import requests
import json
from xeger import Xeger

from tests_admin.Field_Validations.username_field_validations import username_field_validations
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createUser_phoneNumber_empty_053():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("**************** IN description : TestCase_053: Test CreateUser when user sends  -  telephone value as empty ****************")
    print("IN description : TestCase_053: Test CreateUser when user sends  -  telephone value as empty")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")

    user = username_field_validations()
    userName = user.username_regex()

    file_body = readFiles()
    body = file_body.create_user_body()
    body['telephoneNumber'] = ''
    body['userName'] = userName

    com.create_user_positive(body, userName)

    com.verify_users_from_sm_with_api(userName)

