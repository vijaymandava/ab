import uuid
import random
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

    name = "Administrator"
    print('------- get role {}'.format(name))

    r = api_user_roles.get_role(
        nav=nav,
        name=name)

    print('--- the role data is --- ')
    for key,value in r.items():
        print("{} {}".format(key,value))

    print('test is done')


