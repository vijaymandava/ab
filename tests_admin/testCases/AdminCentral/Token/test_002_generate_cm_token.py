import json
import pytest
import requests
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.updateroleAPI
def generate_cm_token():
    cmurl = ReadConfig.cm_for_encryption()
    print("\n CM URL is ::", cmurl)

    #Encrypting Login_info
    headers = {'Content-Type': 'application/json'}
    body = {"userName": "admin", "password": "ChangeMe!234"}
    encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
    encrypted_body = encryption.text
    a = json.loads(encrypted_body)
    print("\n CM Side - Encrypted_body is ::", a)

    #Login
    print("Login with encrypted login body")
    resp = requests.post(cmurl + '/auth/login', headers=headers, data=json.dumps(a, indent=4))
    encrypted_text = resp.text
    d = json.loads(encrypted_text)
    print("\n Login Response - encrypted_text ::", d)

    # Decrypting login Response to see token
    resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(d, indent=4))
    token1 = resp1.text
    # print(" \n Full Token is ::", token1)
    e = json.loads(token1)
    accesstoken = "Bearer " + e["accessToken"]
    print("\n Decrypted AccessToken   :::\n", accesstoken)
    # headers = {'Content-Type': 'application/json', 'Authorization': accesstoken}
    # return headers