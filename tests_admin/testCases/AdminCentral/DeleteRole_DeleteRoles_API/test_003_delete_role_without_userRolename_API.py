import json
import random

import pytest
import requests
from tests_admin.pageObjects.common import common
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.deleteroleAPI
def test_delete_role_API_003():
    logger=LogGen.loggen()
    url = ReadConfig.sm()
    com = common()
    headers = com.headers()
    logger.info("****************  Test_003: Test delete Role when user sends  -  without userRolename Request ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164305?projectId=50")
    print("****************  Test_003: Test delete Role when user sends  -  without userRolename Request ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164305?projectId=50")
    # Generating Token
    body = {
    "deletedBy": "vijay"
    }
    b = com.encrypt(body)
    resp = requests.post(url + '/deleteRole', headers=headers, data=json.dumps(b, indent=4))
    resp_text = resp.text
    d = json.loads(resp_text)
    status = d.get('status')
    print("Status is ::", status)
    assert status == 'Failure'