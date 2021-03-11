import sys
# from navigation import Navigation
# import api_home_ui
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_home_ui
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation

# api test - home - left load
import pytest
@pytest.mark.sm_backend_tests
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

    print('----4----')
    api_home_ui.left_load(nav)

    print('test is done')



