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

    ############### create ##############
    letters = string.ascii_lowercase
    username = 'u' + datetime.now().strftime('%y%m%d%H%M%S%f')
    print('------- create user {}'.format(username))

    params_raw = {
        'first':     ''.join(random.choice(letters) for i in range(6)),
        'middle':    ''.join(random.choice(letters)),
        'last':      ''.join(random.choice(letters) for i in range(6)),
        'username':  username,
        'email':     uuid.uuid4().hex.upper()[0:6] + r'@rapidmicrobio.com',
        'password':  r'FooFoo123@',
        'phone':     '123-456-7890',
        'extension': '123',
        'role_name':      'Operator',}
    params_encoded = json.dumps(params_raw).encode('utf-8')

    api_users.create_user(
        nav=nav,
        params_encoded=params_encoded)

    ########### update #######################
    print('------- update some data in that user {}'.format(username))

    # make new content - no change to username
    params_raw = {
        'first':     ''.join(random.choice(letters) for i in range(6)),
        'middle':    ''.join(random.choice(letters)),
        'last':      ''.join(random.choice(letters) for i in range(6)),
        'username':  username,
        'email':     uuid.uuid4().hex.upper()[0:6] + r'@rapidmicrobio.com',
        'password':  r'BlahBlah123@',
        'phone':     '234-567-8901',
        'extension': '456',
        'role_name':      'Administrator',}
    params_encoded = json.dumps(params_raw).encode('utf-8')

    api_users.update_user(
        nav=nav,
        params_encoded=params_encoded)

    ############## get/check ######################
    print('------- get/check details for user {}'.format(username))

    r = api_users.get_user(
        nav=nav,
        name=username)

    print('the user data is {}'.format(r))

    assert r['first'] == params_raw['first']
    assert r['middle'] == params_raw['middle']
    assert r['last'] == params_raw['last']
    assert r['username'] == params_raw['username']
    assert r['email'] == params_raw['email']
    assert r['phone'] == params_raw['phone']
    assert r['extension'] == params_raw['extension']
    #assert r['user_role'] == params_raw['role'] #zona - not implemented

    print('test is done')


