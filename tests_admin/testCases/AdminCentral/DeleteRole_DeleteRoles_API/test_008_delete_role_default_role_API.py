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
def test_delete_role_API_008():
    logger=LogGen.loggen()
    url = ReadConfig.sm()
    com = common()
    headers = com.headers()
    logger.info("****************  Test_008: Test delete Role when user sends  -  Default Role Request ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164305?projectId=50")
    print("****************  Test_008: Test delete Role when user sends  -  Default Role Request ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164305?projectId=50")
    list = ['Administrator','Fieldservice','Operator']
    # Generating Token
    for i in list:
        print("\n Deleting Role ::", i)
        body = {
        "userRoleName": i,
        "deletedBy": "vijay"
        }
        b = com.encrypt(body)
        resp = requests.post(url + '/deleteRole', headers=headers, data=json.dumps(b, indent=4))
        resp_text = resp.text
        d = json.loads(resp_text)
        message = d["status_message"]
        msg = json.loads(message)
        status = d.get('status')
        assert status == 'Failure'
        print("\n msg::", resp_text)