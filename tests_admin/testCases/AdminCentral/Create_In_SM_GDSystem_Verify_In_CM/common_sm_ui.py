from random import random
from datetime import datetime
import random
import string
import urllib3
import uuid
import json
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

class Common_sm_ui():
    logger = LogGen.loggen()
    url_sm_ui = ReadConfig.sm_user_interface()

    def create_role_in_sm_ui(self, role_name):

        timeout = ReadConfig.timeout_sm()
        http = urllib3.PoolManager()

        ######### create role ###############
        # role_name = "test_" + datetime.now().strftime('%y%m%d%H%M%S%f')

        print("Creating Role from SM GDSystem UI is ::", role_name)

        self.logger.info('------- create role with privs alternating one/zero {}'.format(role_name))

        body_raw = {
            'name': role_name,
            'privs_set': {
                'methods_create': '1',
                'methods_edit': '0',
                'methods_delete': '1',
                'aa_create': '0',
                'aa_edit': '1',
                'aa_delete': '0'}}
        body_encoded = json.dumps(body_raw).encode('utf-8')

        r = http.request(
            method='POST',
            url=self.url_sm_ui + 'roles/create_role',
            body=body_encoded,
            headers={'Content-Type': 'application/json'},
            retries=False,
            timeout=timeout)

        ######### get/check ###############
        self.logger.info('------- get/check role -------')

        name = "Administrator"
        fields = {
            'name': role_name,
        }

        r = http.request(
            method='GET',
            url=self.url_sm_ui + 'roles/get_role',
            fields=fields,
            retries=False,
            timeout=timeout)

        assert r.status == 200, "response has bad status"
        data = json.loads(r.data.decode('utf-8'))

        assert data['privs_get']['methods_create'] == 1
        assert data['privs_get']['methods_edit'] == 0
        assert data['privs_get']['methods_delete'] == 1
        assert data['privs_get']['aa_create'] == 0
        assert data['privs_get']['aa_edit'] == 1
        assert data['privs_get']['aa_delete'] == 0

        self.logger.info('------- test done --------')

    def verify_role_in_sm_ui(self, roleName):

        timeout = ReadConfig.timeout_sm()
        http = urllib3.PoolManager()

        ######### get list ###############
        self.logger.info('------- get list -------')

        r = http.request(
            method='GET',
            url=self.url_sm_ui + 'roles/get_list',
            fields={},
            retries=False,
            timeout=timeout)

        self.logger.info('response is type {}'.format(type(r)))
        self.logger.info('headers is type  {}'.format(type(r.headers)))
        self.logger.info('status is type   {}'.format(type(r.status)))
        self.logger.info('data is type     {}'.format(type(r.data)))
        self.logger.info('r.headers = {}'.format(r.headers))
        self.logger.info('r.status  = {}'.format(r.status))
        self.logger.info('r.data    = {}'.format(r.data))

        assert r.status == 200, "response has bad status"

        data = json.loads(r.data.decode('utf-8'))

        # print("Values from SM_UI  ::", data)

        self.logger.info('------- work with the response data --------')
        list = []
        for key, value in data.items():

            self.logger.info("{} {}".format(key, value))
            list.append(key)
        self.logger.info('there are {}'.format(len(data)))
        assert list.__contains__(roleName) == True
        print("\n Created Role present in the SM(checking from SM_UI)  ::::", roleName)
        self.logger.info('------- test done --------')

    def verify_updated_role_in_sm_UI(self, a):
        logger = LogGen.loggen()

        url_sm_ui = ReadConfig.sm_user_interface()
        http = urllib3.PoolManager()

        ######### get role ###############
        logger.info('------- get role -------')

        name = a
        fields = {
            'name': name
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

    def update_role_in_sm_ui(self, role_name):
        logger = LogGen.loggen()

        url_sm_ui = ReadConfig.sm_user_interface()
        timeout = ReadConfig.timeout_sm()
        http = urllib3.PoolManager()

        ############## update ############
        logger.info('------- update some privs in that role {}'.format(role_name))

        body_raw = {
            'name': role_name,
            'privs_set': {
                'methods_create': '1',
                'methods_edit': '0',
                # 'methods_delete': '1',
                'aa_create': '1',
                'aa_edit': '0',
                # 'aa_delete': '0'
            }}
        body_encoded = json.dumps(body_raw).encode('utf-8')

        r = http.request(
            method='POST',
            url=url_sm_ui + 'roles/update_role',
            body=body_encoded,
            headers={'Content-Type': 'application/json'},
            retries=False,
            timeout=timeout)

        assert r.status == 200, "response has bad status"

        ######### get/check ###############
        logger.info('------- get/check role -------')

        fields = {
            'name': role_name,
        }

        r = http.request(
            method='GET',
            url=url_sm_ui + 'roles/get_role',
            fields=fields,
            retries=False,
            timeout=timeout)

        assert r.status == 200, "response has bad status"
        data = json.loads(r.data.decode('utf-8'))

        assert data['privs_get']['methods_create'] == 1
        assert data['privs_get']['methods_edit'] == 0
        assert data['privs_get']['methods_delete'] == 1
        assert data['privs_get']['aa_create'] == 1
        assert data['privs_get']['aa_edit'] == 0
        assert data['privs_get']['aa_delete'] == 0

        logger.info('------- test done --------')

    def create_user_in_sm_ui(self, username):
        timeout = ReadConfig.timeout_sm()
        http = urllib3.PoolManager()

        ######### create ########################
        # username = "u" + datetime.now().strftime('%y%m%d%H%M%S%f')
        role_name = 'Operator'
        self.logger.info('------- create user {} with role {}'.format(username, role_name))

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
            url=self.url_sm_ui + 'users/create_user',
            body=body_encoded,
            headers={'Content-Type': 'application/json'},
            retries=False,
            timeout=timeout, )

        assert r.status == 200, "response has bad status {} {}".format(r.status, r.data)

        ######### get/check user ###############
        self.logger.info('------- get/check user -------')

        fields = {
            'user_name': username,
        }

        r = http.request(
            method='GET',
            url=self.url_sm_ui + 'users/get_user',
            fields=fields,
            retries=False,
            timeout=timeout, )

        self.logger.info('response is type {}'.format(type(r)))
        self.logger.info('headers is type  {}'.format(type(r.headers)))
        self.logger.info('status is type   {}'.format(type(r.status)))
        self.logger.info('data is type     {}'.format(type(r.data)))
        self.logger.info('r.headers = {}'.format(r.headers))
        self.logger.info('r.status  = {}'.format(r.status))
        # logger.info('r.data    = {}'.format(r.data))

        assert r.status == 200, "response has bad status"
        data = json.loads(r.data.decode('utf-8'))

        self.logger.info('------- work with the response data --------')
        for key, value in data.items():
            self.logger.info("{} {}".format(key, value))
        self.logger.info('there are {}'.format(len(data)))

        assert data['first'] == first
        assert data['middle'] == middle
        assert data['last'] == last
        assert data['username'] == username
        assert data['email'] == email
        assert data['phone'] == phone
        assert data['extension'] == extension
        # zona not implemented assert data['role'] = role

        assert data['privs_get']['methods_create'] == 0
        assert data['privs_get']['methods_edit'] == 0
        assert data['privs_get']['methods_delete'] == 0
        assert data['privs_get']['aa_create'] == 0
        assert data['privs_get']['aa_edit'] == 0
        assert data['privs_get']['aa_delete'] == 0

        self.logger.info('------- test done --------')

    def verify_user_in_sm_ui(self, name):
        logger = LogGen.loggen()

        url_sm_ui = ReadConfig.sm_user_interface()
        timeout = ReadConfig.timeout_sm()
        http = urllib3.PoolManager()

        ######### get user ###############
        logger.info('------- get user -------')

        # name = "Administrator"
        fields = {
            'user_name': name,
        }

        r = http.request(
            method='GET',
            url=url_sm_ui + 'users/get_user',
            fields=fields,
            retries=False,
            timeout=timeout, )

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

        assert data['privs_get']['methods_create'] == 1
        assert data['privs_get']['methods_edit'] == 1
        assert data['privs_get']['methods_delete'] == 1
        assert data['privs_get']['aa_create'] == 1
        assert data['privs_get']['aa_edit'] == 1
        assert data['privs_get']['aa_delete'] == 1

        logger.info('------- test done --------')

    def update_user_in_sm_ui(self, username):
        logger = LogGen.loggen()

        url_sm_ui = ReadConfig.sm_user_interface()
        timeout = ReadConfig.timeout_sm()
        http = urllib3.PoolManager()

        ########### create #####################
        # username = "u" + datetime.now().strftime('%y%m%d%H%M%S%f')
        role_name = 'Operator'
        logger.info('------- update user {} with role {}'.format(username, role_name))

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
            timeout=timeout)

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
            timeout=timeout)

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
            timeout=timeout)

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

        assert data['privs_get']['methods_create'] == 1
        assert data['privs_get']['methods_edit'] == 1
        assert data['privs_get']['methods_delete'] == 1
        assert data['privs_get']['aa_create'] == 1
        assert data['privs_get']['aa_edit'] == 1
        assert data['privs_get']['aa_delete'] == 1

        logger.info('------- test done --------')


