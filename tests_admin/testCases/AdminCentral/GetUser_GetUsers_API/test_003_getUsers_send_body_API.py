import json
import pytest
import requests

from tests_admin.pageObjects.common import common
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.getuserAPI
def test_getUser_API_003():
    logger=LogGen.loggen()
    url = ReadConfig.sm()
    com = common()
    headers = com.headers()
    logger.info("****************  Test_003: Test getUsers when user sends  - Valid Body ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164290?projectId=50")
    print("****************  Test_003: Test getUsers when user sends  - Valid Body ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164290?projectId=50")
    # Generating Token
    body = {
            "userName": "Administrator"
        }
    b = com.encrypt(body)
    resp = requests.post(url + '/getUsers', headers=headers, data=json.dumps(b, indent=4))
    resp_text = resp.text
    d = json.loads(resp_text)
    message = d["status_message"]
    msg = json.loads(message)
    com.decrypt(msg)