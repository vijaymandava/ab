import json

from xeger import Xeger

from tests_admin.testCases.AdminCentral.Create_In_SM_GDSystem_Verify_In_CM.common_sm_ui import Common_sm_ui
from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen


def test_createRole_001():
    logger = LogGen.loggen()
    sm = Common_sm_ui()
    com = Common_role_api()

    # Body
    x = Xeger(limit=20)
    role=com.userRoleName_RegEx()
    roleName = x.xeger(role)
    print("\n Trying to create Role ::::", roleName)

    # sm.create_role_in_sm_ui(roleName)

    # com.verify_role_in_cm_ui(roleName)
