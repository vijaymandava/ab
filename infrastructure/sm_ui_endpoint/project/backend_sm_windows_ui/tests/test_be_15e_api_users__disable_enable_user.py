import uuid
import random
import string
from datetime import datetime
import json


from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_home_ui, api_user_roles, api_users
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation

import pytest
@pytest.mark.sm_backend_tests
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

    ######
    print('get count')
    r = api_users.get_list(nav)

    count_before_total = len(r)
    count_before_enabled = sum(value['enabled'] == 'Yes' for value in r.values())
    count_before_disabled = sum(value['enabled'] == 'No' for value in r.values())
    print('count_total = {} count_enabled = {} count_disabled = {}'.format(count_before_total, count_before_enabled, count_before_disabled))

    ######
    letters = string.ascii_lowercase
    username = 'a01' + datetime.now().strftime('%y%m%d%H%M%S%f')
    print('create user {}'.format(username))

    params_raw = {
        'first':     ''.join(random.choice(letters) for i in range(6)),
        'middle':    ''.join(random.choice(letters)),
        'last':      ''.join(random.choice(letters) for i in range(6)),
        'username':  username,
        'email':     uuid.uuid4().hex.upper()[0:6] + r'@rapidmicrobio.com',
        'password':  r'BlahBlah123@',
        'phone':     '123-456-7890',
        'extension': '123',
        'role_name':      'Operator',}
    params_encoded = json.dumps(params_raw).encode('utf-8')

    api_users.create_user(
        nav=nav,
        params_encoded=params_encoded)


    ######
    print('get/check count after adding')
    r = api_users.get_list(nav)

    count_after_total = len(r)
    count_after_enabled = sum(value['enabled'] == 'Yes' for value in r.values())
    count_after_disabled = sum(value['enabled'] == 'No' for value in r.values())
    print('count_total = {} count_enabled = {} count_disabled = {}'.format(count_after_total, count_after_enabled, count_after_disabled))

    def check(obs, exp, desc):
        assert obs == exp, 'fails {} expected {} observed {}'.format(desc,exp,obs)

    check(count_after_total,    count_before_total + 1,    "after adding... count_after_total")
    check(count_after_enabled,  count_before_enabled + 1,  "after adding... count_after_enabled")
    check(count_after_disabled, count_before_disabled,     "after adding... count_after_disabled")

    ######
    print('disable user')

    params_raw = {
        'username': username,}
    params_encoded = json.dumps(params_raw).encode('utf-8')

    api_users.disable_user(
        nav=nav,
        params_encoded=params_encoded)

    ######
    print('get/check user count after disabling')
    r = api_users.get_list(nav)

    count_after_total = len(r)
    count_after_enabled = sum(value['enabled'] == 'Yes' for value in r.values())
    count_after_disabled = sum(value['enabled'] == 'No' for value in r.values())
    print('count_total = {} count_enabled = {} count_disabled = {}'.format(count_after_total, count_after_enabled, count_after_disabled))

    check(count_after_total,    count_before_total + 1,    "after disabling... count_after_total")
    check(count_after_enabled,  count_before_enabled,      "after disabling... count_after_enabled")
    check(count_after_disabled, count_before_disabled + 1, "after disabling... count_after_disabled")

    print('test is done')


