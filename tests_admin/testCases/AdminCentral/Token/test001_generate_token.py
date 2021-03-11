import json
import random
import pytest
import requests

from tests_admin.testCases.AdminCentral.Update_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.updateroleAPI
def generate_sm_token():
    smurl = ReadConfig.sm_for_encryption()
    cmurl = ReadConfig.cm_for_decryption()
    # print("\n Sm_URL is ::", smurl)
    # print("\n CM URL is ::", cmurl)
    headers = {'Content-Type': 'application/json'}
    body = {"userName": "CMUIServer", "password": "a5a78cfc0e4711ebadc10242ac120002"}
    encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
    encrypted_body = encryption.text
    a = json.loads(encrypted_body)
    # print("\n Encrypted_body is ::", a)
    resp = requests.post(smurl + '/getSMToken', headers=headers, data=json.dumps(a, indent=4))
    encrypted_text = resp.text
    d = json.loads(encrypted_text)
    message = d["status_message"]
    # print("\n encrypted_text-->status_message is  ::", message)
    msg = json.loads(message)
    resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(msg, indent=4))
    token1 = resp1.text
    # print(" \n Full Token is ::", token1)
    e = json.loads(token1)
    accesstoken = "Bearer " + e["accessToken"]
    print("\n AccessToken   :::\n", accesstoken)
    # headers = {'Content-Type': 'application/json', 'Authorization': accesstoken}
    # return headers