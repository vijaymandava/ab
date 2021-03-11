import pytest

from tests_admin.Field_Validations.username_field_validations import username_field_validations
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createUser_editedBy_ApartFrom_RegEx_029():
    logger = LogGen.loggen()
    com = common_createUser_api()
    file_body = readFiles()
    logger.info("****************  Test_029: Test CreateUser when user sends  -  EditedBy value apart from  RegEx ****************")
    print("In Description : Test_029: Test CreateUser when user sends  -  EditedBy value apart from  RegEx")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")

    # Body
    user = username_field_validations()
    userName = user.username_regex()

    list = {".", "!", "@", "=", "$", "%", "^", "&", "*", "~", ":", ";", "/", "/", "?", "]", "[", "|"}
    for i in list:
        print("\n Creating user by sending Edited by value apart from RegEx - Sending -  :", i)

        body = file_body.create_user_body()
        body['editedBy'] = i
        body['userName'] = userName

        com.create_user_negative(body, userName)

        com.verify_users_from_sm_with_api(userName)
