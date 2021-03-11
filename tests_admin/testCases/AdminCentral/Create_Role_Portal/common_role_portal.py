import requests
import json
import urllib3

from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Common_role_portal():
    logger = LogGen.loggen()
    def headers(self):
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
        # print("\n AccessToken   :::\n", accesstoken)
        headers = {'Content-Type': 'application/json', 'Authorization': accesstoken}
        return headers

    def verify_roles_from_sm_with_api(self,roleName):
        com = Common_role_api()
        headers = com.headers()
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        r = requests.get(url + "/getRoles", headers=headers)
        data = r.json()
        # print("Data from SM::\n", r.json())
        resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(data, indent=4))
        roles = resp1.json()
        # print("Roles are ::", roles)
        # extracting data in json format
        list = []
        for item in roles:
            userroles = item.get('userRoleName')
            list.append(userroles)
        # print("Roles are :::\n", list)
        if list.__contains__(roleName):
            assert list.__contains__(roleName) == True
            print("\n Created Role present in the SM(checking with API)  ::::", roleName)
            # logger.info("****************  Role present in the SM ****************")
        else:
            assert list.__contains__(roleName) != True

            print("\n Role not present in the SM(checking with API)  ::::", roleName)
            # logger.info("****************  Role not present in the SM ****************")

        # //*[contains(text(),'+CfBB')]

