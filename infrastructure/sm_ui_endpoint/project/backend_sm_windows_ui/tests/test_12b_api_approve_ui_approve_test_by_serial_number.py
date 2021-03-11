import uuid
import random

# from navigation import Navigation
# import api_approve_ui
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib import api_home_ui
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation


# api test - approve ui - approve test by serial number
import pytest
@pytest.mark.sm_backend_tests
def test():

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start\n')

    print('----4----')
    y = api_approve_ui.get_test_list(nav)
    the_key = None
    for [key, value] in y.items():
        print('{} {}'.format(key, value))
        if value != "":
            the_key = key
    print('there are {} tests waiting to be approved'.format(len(y)))
    assert len(y) > 0, "there are no tests to approve!"
    assert the_key is not None, "there are no tests with a serial number!"

    print('----5----')
    serial_number = y[the_key].get('serial_number')
    print('will approve serial number {}'.format(serial_number))

    print('----6----')
    # generate random comments and mold count
    comment_max_len = 60
    test_comment_random = uuid.uuid4().hex.upper()[0:comment_max_len]
    oos_comment_random = uuid.uuid4().hex.upper()[0:comment_max_len]
    general_comment_random = uuid.uuid4().hex.upper()[0:comment_max_len]
    mold_count_random = random.randrange(2, 20, 2)

    api_approve_ui.approve_test_by_serial_number_or_lims_id(
        nav=nav,
        by='serial_number',
        number_or_id=serial_number,
        test_comment=test_comment_random,
        oos_comment=oos_comment_random,
        general_comment=general_comment_random,
        mold_count=mold_count_random)

    print('test is done')


