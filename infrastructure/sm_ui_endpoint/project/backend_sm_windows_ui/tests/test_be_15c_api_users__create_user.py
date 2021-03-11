import uuid
import random
import string
from datetime import datetime
import json

# from navigation import Navigation
# import api_users

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
        'role_name': 'Operator',}
    params_encoded = json.dumps(params_raw).encode('utf-8')

    api_users.create_user(
        nav=nav,
        params_encoded=params_encoded)


    ################### get ###############################
    
    print('get user {}'.format(username))

    r = api_users.get_user(
        nav=nav,
        name=username)

    # check
    check_list = [
        'first',
        'middle',
        'last',
        'username',
        'email',
        # 'password',
        'phone',
        'extension',
        #'role'  not implemented
        ]

    for p in check_list:
        print('check {}'.format(p))
        assert (params_raw[p] == r[p]), ('fails on {} expected {} observed {}'.format(p, params_raw[p], r[p]))

    print('test is done')


