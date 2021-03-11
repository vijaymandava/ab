# from navigation import Navigation
# import api_retrieve_ui
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_home_ui, api_retrieve_ui
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation

import pytest
@pytest.mark.sm_backend_tests
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

    print('----4----')
    y = api_retrieve_ui.get_test_list(nav)
    the_key = None
    for [key, value] in y.items():
        print('{} {}'.format(key, value))
        if value['serial_number'] != "E":
            the_key = key
            
    print('there are {} tests waiting to be cancelled'.format(len(y)))
    assert len(y) > 0, "there are no tests to cancel!"
    assert the_key is not None, "there are no tests with a serial number!"

    print('----5----')
    serial_number = y[the_key].get('serial_number')
    print('will cancel serial number {}'.format(serial_number))

    print('----6----')
    api_retrieve_ui.cancel_test_by_serial_number_or_lims_id(
        nav=nav,
        by="serial_number",
        number_or_id=serial_number)

    print('test is done')



