import pytest

from tests_admin.Field_Validations.username_field_validations import username_field_validations
from tests_admin.utilities.customLogger import LogGen
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api
from tests_admin.utilities.readExternalFiles import readFiles


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createuser_userName_with_spaces_007():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("****************  Test_007: Test CreateUser when user sends  -  userName with spaces ****************")
    print("In Description : Test_007: Test CreateUser when user sends  -  userName with spaces")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")

    # Body
    user = username_field_validations()
    userName = user.username_spaces_inbetween()
    file_body = readFiles()
    body = file_body.create_user_body()
    body['userName'] = userName

    com.create_user_negative(body, userName)

    com.verify_users_from_sm_with_api(userName)