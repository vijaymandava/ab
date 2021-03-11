import sys

from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_home_ui
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation

# from navigation import Navigation
# import api_home_ui

# api test - home - get test list
import pytest
@pytest.mark.sm_backend_tests
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

    print('----4----')
    y = api_home_ui.get_test_list(nav)
    print(y)
    print('there are {} tests on the home ui {}'.format(len(y), y))

    print('test is done')

 

