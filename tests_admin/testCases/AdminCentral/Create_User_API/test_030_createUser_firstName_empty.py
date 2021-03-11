import pytest

from tests_admin.Field_Validations.username_field_validations import username_field_validations
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createUser_firstName_empty_030():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("****************  Test_030: Test CreateUser when user sends FirstName value as Empty")
    print("In Description :Test_030: Test CreateUser when user sends FirstName value as Empty")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")

    # Body
    user = username_field_validations()
    userName = user.username_regex()
    file_body = readFiles()
    body = file_body.create_user_body()
    body['userName'] = userName
    body['firstName'] = ""

    com.create_user_negative(body, userName)

    com.verify_users_from_sm_with_api(userName)
