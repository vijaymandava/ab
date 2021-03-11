import json
import pytest
from tests_admin.Field_Validations.userRoleName_field_validations import userRoleName_field_validations
from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readExternalFiles import readFiles


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createroleAPI
def test_roleName_editBy_apartfrom_RegEx_027():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("**************** In Description : TestCase_027: Test createRole by sending the 'EditedBy' values apart from  ^[a-zA-Z0-9]+$ ****************")
    print("In Description :Testcase_027: Test createRole by sending the 'EditedBy' values apart from  ^[a-zA-Z0-9]+$")
    logger.info("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")
    print("Jama link: https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164299?projectId=50")

    role = userRoleName_field_validations()
    roleName = role.userRolename_regex()

    print("\n Trying to create role :::", roleName)
    list = {".", "!", "@", "=", "$", "%", "^", "&", "*", "~", ":", ";", "/", "/", "?", "]", "[", "|"}
    for i in list:
        print("\n Trying to create role", roleName, " with editedBy:::", i)
        files = readFiles()
        body = files.create_role_body()
        body['editedBy'] = i
        body['userRoleName'] = roleName

        com.create_role_negative(body, roleName)

        com.verify_roles_from_sm_with_api(roleName)

    logger.info("****************  Role not created ****************")



