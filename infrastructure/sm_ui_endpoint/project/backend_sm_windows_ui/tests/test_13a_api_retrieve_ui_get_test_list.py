import sys
# from navigation import Navigation
# import api_retrieve_ui
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_home_ui
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation


# api test - get list of tests on the cancel page
import pytest
@pytest.mark.sm_backend_tests
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

    print('----4----')
    y = api_retrieve_ui.get_test_list(nav)
    print(y)
    print('there are {} tests waiting to be retrieved'.format(len(y)))

    print('test is done')


