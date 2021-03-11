import json
import pytest
from xeger import Xeger
from tests_admin.utilities.customLogger import LogGen
from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.createroleAPI
def test_createRole_001():
    logger = LogGen.loggen()
    com = Common_role_api()
    logger.info("Creating role from SM GDSystem UI and verify the role in CM UI")

    com.create_role_in_sm_ui()

