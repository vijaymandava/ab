import json
import random
import pytest

from tests_admin.testCases.AdminCentral.Update_User_API.common_updateUser_api import common_updateUser_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.updateuserAPI
def test_updateUser_editedBy_ApartFrom_RegEx_006():
    logger = LogGen.loggen()
    com = common_updateUser_api()
    logger.info("****************  Test_006: Test updateUser when user sends  -  EditedBy value apart from  RegEx ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")
    print("****************  Test_006: Test updateUser when user sends  -  EditedBy value apart from  RegEx ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164311?projectId=50")

    # Body
    list = com.getUsersList()
    userName = random.choice(list)
    print("Updating user ::", userName)
    print("EditedBy value is sending apart from RegEx")

    list = {".", "!", "@", "=", "$", "%", "^", "&", "*", "~", ":", ";", "/", "?", "]", "[", "|"}
    for i in list:
        print("Trying to update editedby with ::",i)

        file = open("./tests_admin/testCases/update_user_api.json", 'r')
        body = json.loads(file.read())
        body['userName'] = userName
        body['editedBy'] = i

        com.update_user_negative(body, userName)

        com.verify_updated_user_from_sm_with_api(userName)

    # com.verify_updated_user_from_sm_UI(userName)