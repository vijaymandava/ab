import allure
import requests
import json

import urllib3
from allure_commons.types import AttachmentType

from tests_admin.pageObjects.common import common
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class Common_role_api():
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

    def update_role_positive(self, body, roleName):
        smurl = ReadConfig.sm_for_encryption()
        cmurl = ReadConfig.cm_for_decryption()
        url = ReadConfig.sm()
        # print("\n Sm_URL is ::", smurl)
        # print("\n CM URL is ::", cmurl)

        # Generating Token
        headers = {'Content-Type': 'application/json'}
        CMUIserver_body = {"userName": "CMUIServer", "password": "a5a78cfc0e4711ebadc10242ac120002"}
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(CMUIserver_body, indent=4))
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

        # Encrypting the request
        # print("Encrypting request ")
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
        encrypted_body = encryption.text
        # print("Encryption-Body is ::::", encrypted_body)
        b = json.loads(encrypted_body)
        # print("Request Body after encryption ::", b)

        # Creating role with encrypted body.
        #print("Now sending Encrypted Json as a Post request ")
        resp = requests.post(url + '/updateRole', headers=headers, data=json.dumps(b, indent=4))
        resp_text = resp.text
        print("\n   Response is :::\n", resp_text)
        # d = json.loads(resp_text)
        # message = d["status_message"]
        # print("\n Received 'status_message' from the encrypted request ::", message)
        # msg = json.loads(message)
        # print("Value in msg is ::", msg)
        # print("Trying to decrypt the Response body")
        # decrypt = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(msg, indent=4))
        # decrypted_text = decrypt.text
        # e = json.loads(decrypted_text)
        # print("Decrypted text is ::", e)
        assert resp.status_code == 200
        print("\n Updated Role is ::", roleName)

    def update_role_negative(self, body, roleName):
        smurl = ReadConfig.sm_for_encryption()
        cmurl = ReadConfig.cm_for_decryption()
        url = ReadConfig.sm()
        # print("\n Sm_URL is ::", smurl)
        # print("\n CM URL is ::", cmurl)

        # Generating Token
        headers = {'Content-Type': 'application/json'}
        CMUIserver_body = {"userName": "CMUIServer", "password": "a5a78cfc0e4711ebadc10242ac120002"}
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers,
                                   data=json.dumps(CMUIserver_body, indent=4))
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

        # Encrypting the request
        # print("Encrypting request ")
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
        encrypted_body = encryption.text
        b = json.loads(encrypted_body)
        # print("Request Body after encryption ::", b)

        # Creating role with encrypted body.

        # print("Now sending Encrypted Json as a Post request ")
        resp = requests.post(url + '/updateRole', headers=headers, data=json.dumps(b, indent=4))
        resp_text = resp.text
        # print("\n   Response is :::\n", resp_text)
        d = json.loads(resp_text)
        message = d["status_message"]
        # print("Received 'status_message' from the encrypted request ::", message)
        msg = json.loads(message)
        # print("Value in msg is ::", msg)
        # print("Trying to decrypt the Response body")
        # decrypt = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(msg, indent=4))
        # decrypted_text = decrypt.text
        # e = json.loads(decrypted_text)
        # print("Decrypted text is ::", e)
        assert resp.status_code != 200
        print("\n Role Not Created   ::::", roleName)

    def verify_updated_role_from_sm_with_api(self,roleName):
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
            print("\n Updated Role present in the SM(checking with API)  ::::", roleName)
            # logger.info("****************  Role present in the SM ****************")
        else:
            assert list.__contains__(roleName) != True
            print("\n Role not present in the SM(checking with API)  ::::", roleName)
            allure.attach(self.driver.get_screenshot_as_png(), name="",
                          attachment_type=AttachmentType.PNG)
            # logger.info("****************  Role not present in the SM ****************")

    def verify_updated_roles_from_sm_UI(self, a):
        logger = LogGen.loggen()

        url_sm_ui = ReadConfig.sm_user_interface()
        http = urllib3.PoolManager()

        ######### get role ###############
        logger.info('------- get role -------')

        name = "Administrator"
        fields = {
            'name': name,
        }

        r = http.request(
            method='GET',
            url=url_sm_ui + 'roles/get_role',
            fields=fields,
            retries=False,
            timeout=120.0, )

        logger.info('response is type {}'.format(type(r)))
        logger.info('headers is type  {}'.format(type(r.headers)))
        logger.info('status is type   {}'.format(type(r.status)))
        logger.info('data is type     {}'.format(type(r.data)))
        logger.info('r.headers = {}'.format(r.headers))
        logger.info('r.status  = {}'.format(r.status))
        logger.info('r.data    = {}'.format(r.data))

        assert r.status == 200, "response has bad status"
        data = json.loads(r.data.decode('utf-8'))

        logger.info('------- work with the response data --------')
        for key, value in data.items():
            logger.info("{} {}".format(key, value))
        logger.info('there are {}'.format(len(data)))

        assert data['methods_create'] == 1
        assert data['methods_edit'] == 1
        assert data['methods_delete'] == 1
        assert data['aa_create'] == 1
        assert data['aa_edit'] == 1
        assert data['aa_delete'] == 1

        logger.info('------- test done --------')

    def verify_update_roleName_options(self, roleName):
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        com = common()
        headers = com.headers()
        print("\n Verifying options in role ::  ", roleName)
        # Generating Token
        body = {
            "userRoleName": roleName
        }
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
        encrypted_body = encryption.text
        b = json.loads(encrypted_body)
        resp = requests.post(url + '/getRole', headers=headers, data=json.dumps(b, indent=4))
        resp_text = resp.text
        d = json.loads(resp_text)
        message = d["status_message"]
        msg = json.loads(message)
        decrypt = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(msg, indent=4))
        decrypted_text = decrypt.text
        e = json.loads(decrypted_text)
        # print("\n Decrypted text is ::\n", e)
        # return e
        # for key, value in e.items():
        #     print("assert e['", key,"'] == ",value)
        return e

    def getRolesList(self):
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
        return list




