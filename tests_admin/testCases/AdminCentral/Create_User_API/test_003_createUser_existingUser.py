import random
import pytest
from tests_admin.utilities.customLogger import LogGen
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api
from tests_admin.utilities.readExternalFiles import readFiles


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createuserAPI
def test_createuser_existingUser_003():
    logger = LogGen.loggen()
    com = common_createUser_api()
    logger.info("****************  Test_003: Test CreateUser when user sends  -  existing username ****************")
    print("In Description : Test_003: Test CreateUser when user sends  -  existing username")
    logger.info(
        "Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")
    print("Jama Link :: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164308?projectId=50")

    # Body
    list = com.getUsersList()
    userName=random.choice(list)
    print("\n Trying to create user :::", userName)

    file_body = readFiles()
    body = file_body.create_user_body()
    body['userName'] = userName

    com.create_user_negative(body, userName)

    com.verify_users_from_sm_with_api(userName)
