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


    ############# get/count users ####################
    logger.info('------- get list of users -------')

    r = http.request(
        method='GET',
        url=url_sm_ui+'users/get_list',
        fields={},
        retries=False,
        timeout=timeout)
    assert r.status == 200, "response has bad status"
    jdata = json.loads(r.data.decode('utf-8'))

    count_before_total = len(jdata)
    count_before_enabled = sum(value['enabled'] == 'Yes' for value in jdata.values())
    count_before_disabled = sum(value['enabled'] == 'No' for value in jdata.values())
    logger.info('count_total = {} count_enabled = {} count_disabled = {}'.format(count_before_total, count_before_enabled, count_before_disabled))


    ############# create ####################
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
        timeout=timeout)

    assert r.status == 200, "response has bad status {} {}".format(r.status, r.data)


    ############# get/check ####################
    logger.info('------- get list of users, check enabled/disabled count -------')

    r = http.request(
        method='GET',
        url=url_sm_ui+'users/get_list',
        fields={},
        retries=False,
        timeout=timeout)
    assert r.status == 200, "response has bad status"
    jdata = json.loads(r.data.decode('utf-8'))

    count_after_total = len(jdata)
    count_after_enabled = sum(value['enabled'] == 'Yes' for value in jdata.values())
    count_after_disabled = sum(value['enabled'] == 'No' for value in jdata.values())
    logger.info('count_total = {} count_enabled = {} count_disabled = {}'.format(count_after_total, count_after_enabled, count_after_disabled))

    assert count_after_total == count_before_total + 1
    assert count_after_enabled == count_before_enabled + 1
    assert count_after_disabled == count_before_disabled

    ############# disable ####################
    logger.info('------- disable user -------')

    body_raw = {
        'username': username,
        }
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = http.request(
        method='POST',
        url=url_sm_ui+'users/disable_user',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=timeout)

    assert r.status == 200, "response has bad status"

    ############# get/check ####################
    logger.info('------- get list of users, check enabled/disabled count -------')

    r = http.request(
        method='GET',
        url=url_sm_ui+'users/get_list',
        fields={},
        retries=False,
        timeout=timeout)
    assert r.status == 200, "response has bad status"
    jdata = json.loads(r.data.decode('utf-8'))

    count_after_total = len(jdata)
    count_after_enabled = sum(value['enabled'] == 'Yes' for value in jdata.values())
    count_after_disabled = sum(value['enabled'] == 'No' for value in jdata.values())
    logger.info('count_total = {} count_enabled = {} count_disabled = {}'.format(count_after_total, count_after_enabled, count_after_disabled))

    assert count_after_total == count_before_total + 1, "counts before/after = {} {}".format(count_after_total, count_before_total)
    assert count_after_enabled == count_before_enabled
    assert count_after_disabled == count_before_disabled + 1


    logger.info('------- test done --------')



