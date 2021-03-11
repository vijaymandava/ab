import uuid
import json
import urllib3
import pytest


# from sm user interface - cancel tests having lims_id 40xxxxxx
from tests_lims.tests.common import Common

@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- start the test -------')
    
    data = com.sm_retrieve_get_test_list(1)

    for n, row in data.items():
        lims_id = row['lims_id']
        serial_number = row['serial_number']

        if lims_id[0:2] == '40':
            print('------- using SM User interface to cancel assay: LIMS_ID {} serial num {}'.format(lims_id, serial_number))

            com.sm_retrieve_cancel_test_by_serial_number_or_lims_id(
                sm_number=1,
                by="lims_id",
                serial_number_or_lims_id=lims_id,
                test_comment=com.get_random_approve_comment(),
                oos_comment=com.get_random_approve_comment(),
                general_comment=com.get_random_approve_comment(),
                mold_count=com.get_random_approve_mold_count())

    print('------- test is done -------')
    
