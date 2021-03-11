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
def test_delete_role_API_005():
    logger=LogGen.loggen()
    url = ReadConfig.sm()
    com = common()
    headers = com.headers()
    logger.info("****************  Test_005: Test delete Role when user sends  -  without deleteBy Request ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164305?projectId=50")
    print("****************  Test_005: Test delete Role when user sends  -  without deleteBy Request ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164305?projectId=50")
    role = com.getRolesList()
    delete_role = random.choice(role)
    print("\n Deleting role  ::  ", delete_role)
    # Generating Token
    body = {
                "userRoleName": delete_role
            }
    b = com.encrypt(body)
    resp = requests.post(url + '/deleteRole', headers=headers, data=json.dumps(b, indent=4))
    resp_text = resp.text
    d = json.loads(resp_text)
    status = d.get('status')
    print("Status is ::", status)
    assert status == 'Failure'