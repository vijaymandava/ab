import json
import pytest
import requests
from tests_admin.pageObjects.common import common
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig



@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.deleteroleAPI
def test_delete_role_API_007():
    logger=LogGen.loggen()
    url = ReadConfig.sm()
    com = common()
    headers = com.headers()
    logger.info("****************  Test_007: Test delete Role when user sends  -  not existing userRoleName Request ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164305?projectId=50")
    print("****************  Test_007: Test delete Role when user sends  -  not existing userRoleName Request ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164305?projectId=50")
    # Generating Token
    body = {
    "userRoleName": "delete_role",
    "deletedBy": "vijay"
    }
    b = com.encrypt(body)
    resp = requests.post(url + '/deleteRole', headers=headers, data=json.dumps(b, indent=4))
    resp_text = resp.text
    d = json.loads(resp_text)
    status = d.get('status')
    print("Status is ::", status)
    assert status == 'Failure'