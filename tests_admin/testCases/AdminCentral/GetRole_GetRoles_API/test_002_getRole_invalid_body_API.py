import json
import pytest
import requests

from tests_admin.pageObjects.common import common
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.test_api
@pytest.mark.regression
@pytest.mark.getroleAPI
def test_getRole_API_002():
    logger = LogGen.loggen()
    cmurl = ReadConfig.cm_for_decryption()
    smurl = ReadConfig.sm()
    com = common()
    headers = com.headers()
    logger.info("****************  Test_002: Test getRole when user sends  -  Invalid Body ****************")
    logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164278?projectId=50")
    print("****************  Test_002: Test getRole when user sends  -  Invalid Body ****************")
    print("Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164278?projectId=50")

    body = {
            "userRoleName": ""
        }
    b = com.encrypt(body)
    resp = requests.post(smurl + '/getRole', headers=headers, data=json.dumps(b, indent=4))
    resp_text = resp.text
    d = json.loads(resp_text)
    message = d["status_message"]
    msg = json.loads(message)
    decrypt = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(msg, indent=4))
    decrypted_text = decrypt.text
    e = json.loads(decrypted_text)
    status = e.get('status')
    assert status == 'failed'
    print("\n Decrypted text is ::\n", e)