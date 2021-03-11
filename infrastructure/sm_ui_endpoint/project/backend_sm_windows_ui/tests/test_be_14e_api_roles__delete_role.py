from datetime import datetime
import json

# from navigation import Navigation
# import api_user_roles
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_home_ui, api_user_roles
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
    print('------- create {}'.format(role_name))

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

    ############## get ######################
    print('------- get')

    r = api_user_roles.get_role(
        nav=nav,
        name=role_name)

    print("the role settings are {}".format(r))

    ########### delete ################
    print('------- delete')
    params_raw = {
        'name': role_name
        }
    params_encoded = json.dumps(params_raw).encode('utf-8')

    api_user_roles.delete_role(
        nav=nav,
        params_encoded=params_encoded)

    # ############# attempt to get ######################
    print('------- attempt to get')

    r = api_user_roles.get_role(
        nav=nav,
        name=role_name)

    print("the role settings are {}".format(r))
    assert len(r) == 0, "expected the role to be deleted, observed the role still exists"

    print('test is done')

