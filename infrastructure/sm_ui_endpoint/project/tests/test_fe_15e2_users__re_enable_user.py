# from common_settings_for_fe_be_tests import CommonSettingForFeBeTests
from infrastructure.sm_ui_endpoint.project.tests.common_settings_for_fe_be_tests import CommonSettingForFeBeTests

import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')
    common = CommonSettingForFeBeTests()

    assert False, "re-enable user is not coded, specifically on re-enable there is a popup requiring new password"
  
    print('------- test done --------')
