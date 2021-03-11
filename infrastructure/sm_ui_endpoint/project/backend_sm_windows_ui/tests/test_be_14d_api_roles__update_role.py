from datetime import datetime
import json

from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_user_roles
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation


import pytest
@pytest.mark.sm_backend_tests
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

    ############# create #################
    role_name = "test_" + datetime.now().strftime('%y%m%d%H%M%S%f')
    print('------- create role with custom privs {}'.format(role_name))

    params_raw = {
        'name': role_name,
        'privs': {
            'methods_create': '1',
            'methods_edit': '1',
            'methods_delete': '1',
            'aa_create': '0',
            'aa_edit': '0',
            'aa_delete': '0'}}
    params_encoded = json.dumps(params_raw).encode('utf-8')

    api_user_roles.create_role(
        nav=nav,
        params_encoded=params_encoded)

    ########### update #######################
    print('------- update some privs in that role {}'.format(role_name))

    params_raw = {
        'name': role_name,
        'privs': {
            'methods_create': '1',
            'methods_edit': '0',
            # methods_delete to be unchanged
            'aa_create': '1',
            'aa_edit': '0',
            # aa_delete to be unchanged
            }}
    params_encoded = json.dumps(params_raw).encode('utf-8')

    api_user_roles.update_role(
        nav=nav,
        params_encoded=params_encoded)

    ############## check ######################
    print('------- check {}'.format(role_name))
    params_raw = {
        'name': role_name
        }
    params_encoded = json.dumps(params_raw).encode('utf-8')

    r = api_user_roles.get_role(
        nav=nav,
        name=role_name)

    print(r)

    assert r['methods_create'] == 1
    assert r['methods_edit'] == 0
    assert r['methods_delete'] == 1
    assert r['aa_create'] == 1
    assert r['aa_edit'] == 0
    assert r['aa_delete'] == 0

    print('test is done')


