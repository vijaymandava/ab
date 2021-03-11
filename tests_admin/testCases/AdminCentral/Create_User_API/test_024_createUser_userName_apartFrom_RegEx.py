import pytest

from tests_admin.utilities.customLogger import LogGen
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api
from tests_admin.utilities.readExternalFiles import readFiles


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createUser_userName_apartFrom_RegEx_024():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("****************  Test_024: Test CreateUser when user sends 'userName' values other than ^[a-zA-Z0-9\-_()'.#\\+ ]*$   ")
    print("In Description :Test_024: Test CreateUser when user sends 'userName' values other than ^[a-zA-Z0-9\-_()'.#\\+ ]*$")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")

    # Body
    list = {".", "!", "@", "=", "$", "%", "^", "&", "*", "~", ":", ";", "/", "/", "?", "]", "[", "|"}
    for userName in list:
        print("\n Trying to create user name ::", userName)
        file_body = readFiles()
        body = file_body.create_user_body()
        body['userName'] = userName
        com.create_user_negative(body, userName)
        com.verify_users_from_sm_with_api(userName)
