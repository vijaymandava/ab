import json

import requests
from xeger import Xeger

from tests_admin.pageObjects.common import common
from tests_admin.utilities.readProperties import ReadConfig

class common_createUser_api():

    def userName_RegEx(self):
        userName = "^[a-zA-Z0-9]+$"
        return userName

    def editedBy_RegEx(self):
        editedBy = "^[a-zA-Z0-9]+$"
        return editedBy

    def firstName_RegEx(self):
        firstName = "^([a-zA-Z '-]+)$"
        return firstName

    def middleInitial_RegEx(self):
        middleInitial = "^([a-zA-Z]+)$"
        return middleInitial

    def lastName_RegEx(self):
        lastName = "^([a-zA-Z '-]+)$"
        return lastName

    def emailId_RegEx(self):
        first="^([a-zA-Z0-9_\-\.]+)$"
        last="^(\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|([a-zA-Z0-9.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$"
        # emailId = "^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$"
        x = Xeger(limit=64)
        before = x.xeger(first)
        y=Xeger(limit=256)
        after=y.xeger(last)
        emailId=before+"@"+after
        return emailId

    def telephone_RegEx(self):
        telephone = "^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$"
        return telephone

    def password_RegEx(self):
        password = "^(?=.*[0-9])(?=.*[A-Z]).{8,32}$"
        return password

    def confirmPassword_RegEx(self):
        confirmPassword = "^(?=.*[0-9])(?=.*[A-Z]).{8,32}$"
        return confirmPassword

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

    def getUsersList(self):
        com = common_createUser_api()
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

    def create_user_positive(self, body, userName):
        smurl = ReadConfig.sm_for_encryption()
        cmurl = ReadConfig.cm_for_decryption()
        url = ReadConfig.sm()
        headers = self.headers()
        # Encrypting the request
        # print("Encrypting request ")
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
        encrypted_body = encryption.text
        b = json.loads(encrypted_body)
        # print("Request Body after encryption ::", b)

        # Creating role with encrypted body.
        #print("Now sending Encrypted Json as a Post request ")
        resp = requests.post(url + '/createUser', headers=headers, data=json.dumps(b, indent=4))
        resp_text = resp.text
        # print("\n   Response is :::\n", resp_text)
        d = json.loads(resp_text)
        message = d["status_message"]
        # print("\n Received 'status_message' from the encrypted request ::", message)
        msg = json.loads(message)
        # print("Value in msg is ::", msg)
        # print("Trying to decrypt the Response body")
        decrypt = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(msg, indent=4))
        decrypted_text = decrypt.text
        e = json.loads(decrypted_text)
        # print("Decrypted text is ::", e)
        assert resp.status_code == 200
        print("\n Created User is ::", userName)

    def create_user_negative(self, body, userName):
        smurl = ReadConfig.sm_for_encryption()
        cmurl = ReadConfig.cm_for_decryption()
        url = ReadConfig.sm()
        print("\n Sm_URL is ::", smurl)
        print("\n CM URL is ::", cmurl)

        # Generating Token
        headers = self.headers()
        # Encrypting the request
        # print("Encrypting request ")
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
        encrypted_body = encryption.text
        b = json.loads(encrypted_body)
        # print("Request Body after encryption ::", b)

        # Creating role with encrypted body.
        # print("Now sending Encrypted Json as a Post request ")
        resp = requests.post(url + '/createUser', headers=headers, data=json.dumps(b, indent=4))
        resp_text = resp.text
        # print("\n   Response is :::\n", resp_text)
        d = json.loads(resp_text)
        message = d["status_message"]
        status = d['status']
        # print("\n Received 'status_message' from the encrypted request ::", message)
        msg = json.loads(message)
        # print("Value in msg is ::", msg)
        # print("Trying to decrypt the Response body")
        decrypt = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(msg, indent=4))
        decrypted_text = decrypt.text
        e = json.loads(decrypted_text)
        # print("Decrypted text is ::", e)
        assert status == 'Failure'
        print("\n User Not Created   ::::", userName)

    def verify_users_from_sm_with_api(self,userName):
        com = common_createUser_api()
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
        # print("Users are ::::", list)
        if list.__contains__(userName):
            assert list.__contains__(userName) == True
            print("\n Created user present in the SM(checking with API)  ::::", userName)
            # logger.info("****************  Role present in the SM ****************")
        else:
            assert list.__contains__(userName) != True
            print("\n User is not present in the SM(checking with API)  ::::", userName)
            # logger.info("****************  Role not present in the SM ****************")

    def verify_user_options(self, userName):
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        com = common()
        headers = com.headers()
        print("\n Verifying options in role ::  ", userName)
        # Generating Token
        body = {
            "userName": userName
        }
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
        encrypted_body = encryption.text
        b = json.loads(encrypted_body)
        resp = requests.post(url + '/getUser', headers=headers, data=json.dumps(b, indent=4))
        resp_text = resp.text
        d = json.loads(resp_text)
        message = d["status_message"]
        msg = json.loads(message)
        decrypt = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(msg, indent=4))
        decrypted_text = decrypt.text
        e = json.loads(decrypted_text)
        # print("\n Decrypted text is ::\n", e)
        # return e
        for key, value in e.items():
            print("assert e['", key,"'] == ",value)
        return e




