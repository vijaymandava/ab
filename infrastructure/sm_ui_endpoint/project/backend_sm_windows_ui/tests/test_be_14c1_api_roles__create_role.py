import uuid
import random
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

    #############################
    role_name = "test_" + datetime.now().strftime('%y%m%d%H%M%S%f')
    print('------- create role with privs alternating {}'.format(role_name))

    params_raw = {
        'name': role_name,
        'privs': {
            'methods_create': '1',
            'methods_edit': '0',
            'methods_delete': '1',
            'sys_maintenance': '0',
            'sys_service': '1',
            'sys_send_system_logs': '0'}}
    params_encoded = json.dumps(params_raw).encode('utf-8')

    api_user_roles.create_role(
        nav=nav,
        params_encoded=params_encoded)

    print('test is done')


