import uuid
import random
import string
from datetime import datetime
# from common_settings_for_fe_be_tests import CommonSettingForFeBeTests
from infrastructure.sm_ui_endpoint.project.tests.common_settings_for_fe_be_tests import CommonSettingForFeBeTests

import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')
    common = CommonSettingForFeBeTests()

    ################# create ################
    username = "u" + datetime.now().strftime('%y%m%d%H%M%S%f')
    role_name = 'Operator'
    print('------- create user {} with role {}'.format(username, role_name))

    letters = string.ascii_lowercase

    first =    ''.join(random.choice(letters) for i in range(6))
    middle =   ''.join(random.choice(letters))
    last =     ''.join(random.choice(letters) for i in range(6))
    email =    uuid.uuid4().hex.upper()[0:6] + r'@rapidmicrobio.com'
    password = r'BlahBlah123@'
    phone =   '123-456-7890'
    extension = '123'

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
    import json
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'users/create_user',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)

    assert r.status == 200, "response has bad status {} {}".format(r.status, r.data)

    ######### update #################
    role_name = 'Administrator'
    print('------- update user {} to role {}'.format(username, role_name))

    letters = string.ascii_lowercase

    first =    ''.join(random.choice(letters) for i in range(6))
    middle =   ''.join(random.choice(letters))
    last =     ''.join(random.choice(letters) for i in range(6))
    email =    uuid.uuid4().hex.upper()[0:6] + r'@rapidmicrobio.com'
    password = r'Foofoo123@'
    phone =   '456-789-0123'
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

    print('------- issue the command -------')
    r = common.http.request(
        method='POST',
        url=common.url + 'users/update_user',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)

    assert r.status == 200, "response has bad status {} {}".format(r.status, r.data)

    print('------- test done --------')
