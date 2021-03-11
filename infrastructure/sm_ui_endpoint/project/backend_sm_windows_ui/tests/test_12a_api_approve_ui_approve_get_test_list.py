import sys
# from navigation import Navigation
# import api_approve_ui

from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_home_ui
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation

# api test - approve ui - get list of tests
import pytest
@pytest.mark.sm_backend_tests
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

    print('----4----')
    y = api_approve_ui.get_test_list(nav)
    print(y)
    print('there are {} tests waiting to be approved{}'.format(len(y),y))

    print('test is done')

