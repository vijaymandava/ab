from datetime import datetime
import json
# from common_settings_for_fe_be_tests import CommonSettingForFeBeTests
from infrastructure.sm_ui_endpoint.project.tests.common_settings_for_fe_be_tests import CommonSettingForFeBeTests

import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')
    common = CommonSettingForFeBeTests()

    #############################
    role_name = "test_" + datetime.now().strftime('%y%m%d%H%M%S%f')
    print('------- test the error case - create role with missing privs element {}'.format(role_name))

    body_raw = {
        'name': role_name,
        }
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'roles/create_role',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)

    assert r.status == 500, "expected a bad status and did not see that! {} {}".format(r.status, r.data)

    print('------- test done --------')
