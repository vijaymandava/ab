import uuid
import random
from datetime import datetime
import json


import pytest

from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_user_roles
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation


@pytest.mark.sm_backend_tests
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

    #############################
    role_name = "test_" + datetime.now().strftime('%y%m%d%H%M%S%f')
    print('------- create role with no privs identified {}'.format(role_name))

    params_raw = {
        'name': role_name,
        'privs': {}}
    params_encoded = json.dumps(params_raw).encode('utf-8')

    api_user_roles.create_role(
        nav=nav,
        params_encoded=params_encoded)

    print('test is done')


