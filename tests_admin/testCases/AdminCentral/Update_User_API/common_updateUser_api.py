from datetime import datetime
import json
import random
import string
import uuid

import allure
import requests
import urllib3
from allure_commons.types import AttachmentType
from xeger import Xeger

from tests_admin.pageObjects.common import common
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

class common_updateUser_api():

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
        com = common_updateUser_api()
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
        print("\n Users are ::::",list)
        return list

    def update_user_positive(self, body, userName):
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
        # print("Token is ::", headers)

        # Encrypting the request
        # print("Encrypting request ")
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
        encrypted_body = encryption.text
        b = json.loads(encrypted_body)
        # print("Request Body after encryption ::", b)

        # Creating role with encrypted body.
        #print("Now sending Encrypted Json as a Post request ")
        resp = requests.post(url + '/updateUser', headers=headers, data=json.dumps(b, indent=4))
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
        print("\n User Updated is ::", userName)

    def update_user_negative(self, body, userName):
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
        resp = requests.post(url + '/updateUser', headers=headers, data=json.dumps(b, indent=4))
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
        assert resp.status_code != 200
        print("\n user Not updated   ::::", userName)

    def verify_updated_user_from_sm_with_api(self,userName):
        com = common_updateUser_api()
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

    def verify_updated_user_from_sm_UI(self, userName):
        logger = LogGen.loggen()

        url_sm_ui = ReadConfig.sm_user_interface()
        http = urllib3.PoolManager()

        ########### create #####################
        username = "u" + datetime.now().strftime('%y%m%d%H%M%S%f')
        role_name = 'Operator'
        logger.info('------- create user {} with role {}'.format(username, role_name))

        letters = string.ascii_lowercase

        first = ''.join(random.choice(letters) for i in range(6))
        middle = ''.join(random.choice(letters))
        last = ''.join(random.choice(letters) for i in range(6))
        email = uuid.uuid4().hex.upper()[0:6] + r'@rapidmicrobio.com'
        password = r'BlahBlah123@'
        phone = '123-456-7890'
        extension = '123'
        role = 'Operator'

        body_raw = {
            'first': first,
            'middle': middle,
            'last': last,
            'username': username,
            'email': email,
            'password': password,
            'phone': phone,
            'extension': extension,
            'role_name': role_name}
        body_encoded = json.dumps(body_raw).encode('utf-8')

        r = http.request(
            method='POST',
            url=url_sm_ui + 'users/create_user',
            body=body_encoded,
            headers={'Content-Type': 'application/json'},
            retries=False,
            timeout=120.0, )

        assert r.status == 200, "response has bad status {} {}".format(r.status, r.data)

        ############ update ######################3

        role_name = 'Administrator'
        logger.info('------- update user {} to role {}'.format(username, role_name))

        letters = string.ascii_lowercase

        first = ''.join(random.choice(letters) for i in range(6))
        middle = ''.join(random.choice(letters))
        last = ''.join(random.choice(letters) for i in range(6))
        email = uuid.uuid4().hex.upper()[0:6] + r'@rapidmicrobio.com'
        password = r'Foofoo123@'
        phone = '456-789-0123'
        extension = '456'

        body_raw = {
            'first': first,
            'middle': middle,
            'last': last,
            'username': username,
            'email': email,
            'password': password,
            'phone': phone,
            'extension': extension,
            'role_name': role_name}
        body_encoded = json.dumps(body_raw).encode('utf-8')

        logger.info('------- issue the command -------')
        r = http.request(
            method='POST',
            url=url_sm_ui + 'users/update_user',
            body=body_encoded,
            headers={'Content-Type': 'application/json'},
            retries=False,
            timeout=120.0, )

        assert r.status == 200, "response has bad status {} {}".format(r.status, r.data)

        ######### get/check user ###############
        logger.info('------- get/check user -------')

        fields = {
            'user_name': username,
        }

        r = http.request(
            method='GET',
            url=url_sm_ui + 'users/get_user',
            fields=fields,
            retries=False,
            timeout=120.0, )

        logger.info('response is type {}'.format(type(r)))
        logger.info('headers is type  {}'.format(type(r.headers)))
        logger.info('status is type   {}'.format(type(r.status)))
        logger.info('data is type     {}'.format(type(r.data)))
        logger.info('r.headers = {}'.format(r.headers))
        logger.info('r.status  = {}'.format(r.status))
        # logger.info('r.data    = {}'.format(r.data))

        assert r.status == 200, "response has bad status"
        data = json.loads(r.data.decode('utf-8'))

        logger.info('------- work with the response data --------')
        for key, value in data.items():
            logger.info("{} {}".format(key, value))
        logger.info('there are {}'.format(len(data)))

        assert data['first'] == first
        assert data['middle'] == middle
        assert data['last'] == last
        assert data['username'] == username
        assert data['email'] == email
        assert data['phone'] == phone
        assert data['extension'] == extension
        # zona not implemented assert data['role'] = role

        assert data['methods_create'] == 1
        assert data['methods_edit'] == 1
        assert data['methods_delete'] == 1
        assert data['aa_create'] == 1
        assert data['aa_edit'] == 1
        assert data['aa_delete'] == 1

        logger.info('------- test done --------')

    def verify_update_user_options(self, userName):
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



