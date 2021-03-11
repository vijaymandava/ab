import json

import requests
from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class common():

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

    def getRolesList(self):
        com = common()
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
        return list

    def getUsersList(self):
        com = common()
        headers = com.headers()
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        r = requests.get(url + "/getUsers", headers=headers)
        data = r.json()
        # print("Data from SM::\n", r.json())
        resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(data, indent=4))
        users = resp1.json()
        # print("Users are ::", users)
        # extracting data in json format
        list = []
        for item in users:
            userNames = item.get('userName')
            list.append(userNames)
        print("\n Users are ::::",list)
        return list

    def verify_users_from_sm_with_api(self,userName):
        com = common()
        headers = com.headers()
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        r = requests.get(url + "/getUsers", headers=headers)
        data = r.json()
        # print("Data from SM::\n", r.json())
        resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(data, indent=4))
        roles = resp1.json()
        # print("Roles are ::", roles)
        # extracting data in json format
        list = []
        for item in roles:
            userNames = item.get('userName')
            list.append(userNames)
        print("Users are ::::", list)
        if list.__contains__(userName):
            assert list.__contains__(userName) == True
            print("\n Created user present in the SM(checking with API)  ::::", userName)
            # logger.info("****************  Role present in the SM ****************")
        else:
            assert list.__contains__(userName) != True
            print("\n User is not present in the SM(checking with API)  ::::", userName)
            # logger.info("****************  Role not present in the SM ****************")

    def encrypt(self, body):
        smurl = ReadConfig.sm_for_encryption()
        cmurl = ReadConfig.cm_for_decryption()
        com = common()
        headers = com.headers()
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
        encrypted_body = encryption.text
        b = json.loads(encrypted_body)
        # print("Request Body after encryption ::", b)
        return b

    def decrypt(self, msg):
        cmurl = ReadConfig.cm_for_decryption()
        com = common()
        headers = com.headers()
        decrypt = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(msg, indent=4))
        decrypted_text = decrypt.text
        e = json.loads(decrypted_text)
        print("\n Decrypted text is ::\n", e)
        return e
        # for key, value in e.items():
        #     print("assert e['", key,"'] == ",value)
        # return e

    def get_default_roleList(self):
        com = common()
        headers = com.headers()
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        r = requests.get(url + "/getRoles", headers=headers)
        data = r.json()
        resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(data, indent=4))
        roles = resp1.json()
        list = []
        for item in roles:
            userroles = item.get('userRoleName')
            list.append(userroles)
        return list




