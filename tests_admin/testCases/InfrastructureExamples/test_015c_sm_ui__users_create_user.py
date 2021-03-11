from datetime import datetime
import random
import string
import pytest
import urllib3
import uuid
import json
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

@pytest.mark.infrastructureExamplesSmUiUsers
def test():
    logger = LogGen.loggen()

    url_sm_ui = ReadConfig.sm_user_interface()
    timeout = ReadConfig.timeout_sm()
    http = urllib3.PoolManager()

    ######### create ########################
    username = "u" + datetime.now().strftime('%y%m%d%H%M%S%f')
    role_name = 'Operator'
    logger.info('------- create user {} with role {}'.format(username, role_name))

    letters = string.ascii_lowercase

    first =    ''.join(random.choice(letters) for i in range(6))
    middle =   ''.join(random.choice(letters))
    last =     ''.join(random.choice(letters) for i in range(6))
    email =    uuid.uuid4().hex.upper()[0:6] + r'@rapidmicrobio.com'
    password = r'BlahBlah123@'
    phone =   '123-456-7890'
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
        url=url_sm_ui+'users/create_user',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=timeout,)

    assert r.status == 200, "response has bad status {} {}".format(r.status, r.data)

    ######### get/check user ###############
    logger.info('------- get/check user -------')

    fields = {
        'user_name': username,
    }

    r = http.request(
        method='GET',
        url=url_sm_ui+'users/get_user',
        fields=fields,
        retries=False,
        timeout=timeout,)

    logger.info('response is type {}'.format(type(r)))
    logger.info('headers is type  {}'.format(type(r.headers)))
    logger.info('status is type   {}'.format(type(r.status)))
    logger.info('data is type     {}'.format(type(r.data)))
    logger.info('r.headers = {}'.format(r.headers))
    logger.info('r.status  = {}'.format(r.status))
    #logger.info('r.data    = {}'.format(r.data))

    assert r.status == 200, "response has bad status"
    data = json.loads(r.data.decode('utf-8'))

    logger.info('------- work with the response data --------')
    for key,value in data.items():
        logger.info("{} {}".format(key,value))
    logger.info('there are {}'.format(len(data)))

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

    logger.info('------- test done --------')
