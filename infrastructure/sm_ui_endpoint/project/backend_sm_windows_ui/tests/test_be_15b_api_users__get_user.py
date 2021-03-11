
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_home_ui, api_user_roles, api_users
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation

import pytest
@pytest.mark.sm_backend_tests
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

    name = "FieldService"
    print('------- get user {}'.format(name))

    r = api_users.get_user(
        nav=nav,
        name=name)

    print('--- the user data is --- ')
    for key, value in r.items():
        print("{} {}".format(key, value))

    print('test is done')

