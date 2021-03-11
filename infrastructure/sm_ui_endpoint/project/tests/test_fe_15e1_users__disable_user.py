import uuid
import random
import string
from datetime import datetime
import json
# from common_settings_for_fe_be_tests import CommonSettingForFeBeTests
from infrastructure.sm_ui_endpoint.project.tests.common_settings_for_fe_be_tests import CommonSettingForFeBeTests

import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')
    common = CommonSettingForFeBeTests()

    ############# get/count users ####################
    print('------- get list of users -------')

    r = common.http.request(
        'GET',
        common.url + 'users/get_list',
        retries=False,
        timeout=common.timeout)
    assert r.status == 200, "response has bad status"
    jdata = json.loads(r.data.decode('utf-8'))

    count_before_total = len(jdata)
    count_before_enabled = sum(value['enabled'] == 'Yes' for value in jdata.values())
    count_before_disabled = sum(value['enabled'] == 'No' for value in jdata.values())
    print('count_total = {} count_enabled = {} count_disabled = {}'.format(count_before_total, count_before_enabled, count_before_disabled))


    ############# create ####################
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

    r = common.http.request(
        method='POST',
        url=common.url + 'users/create_user',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)

    assert r.status == 200, "response has bad status {} {}".format(r.status, r.data)


    ############# get/check ####################
    print('------- get list of users, check enabled/disabled count -------')

    r = common.http.request(
        'GET',
        common.url + 'users/get_list',
        retries=False,
        timeout=common.timeout)
    assert r.status == 200, "response has bad status"
    jdata = json.loads(r.data.decode('utf-8'))

    count_after_total = len(jdata)
    count_after_enabled = sum(value['enabled'] == 'Yes' for value in jdata.values())
    count_after_disabled = sum(value['enabled'] == 'No' for value in jdata.values())
    print('count_total = {} count_enabled = {} count_disabled = {}'.format(count_after_total, count_after_enabled, count_after_disabled))

    assert count_after_total == count_before_total + 1
    assert count_after_enabled == count_before_enabled + 1
    assert count_after_disabled == count_before_disabled

    ############# disable ####################
    print('------- disable user -------')

    body_raw = {
        'username': username,
        }
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'users/disable_user',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=120.0,)

    assert r.status == 200, "response has bad status"

    ############# get/check ####################
    print('------- get list of users, check enabled/disabled count -------')

    r = common.http.request(
        method='GET',
        url=common.url + 'users/get_list',
        retries=False,
        timeout=60.0)
    assert r.status == 200, "response has bad status"
    jdata = json.loads(r.data.decode('utf-8'))

    count_after_total = len(jdata)
    count_after_enabled = sum(value['enabled'] == 'Yes' for value in jdata.values())
    count_after_disabled = sum(value['enabled'] == 'No' for value in jdata.values())
    print('count_total = {} count_enabled = {} count_disabled = {}'.format(count_after_total, count_after_enabled, count_after_disabled))

    assert count_after_total == count_before_total + 1, "counts before/after = {} {}".format(count_after_total, count_before_total)
    assert count_after_enabled == count_before_enabled
    assert count_after_disabled == count_before_disabled + 1


    print('------- test done --------')
