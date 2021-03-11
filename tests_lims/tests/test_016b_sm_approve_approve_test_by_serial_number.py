import uuid
import json
import urllib3
import pytest
from tests_lims.tests.common import Common

# from sm user interface - approve tests having serial_number 41xxxxxx
@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- start the test -------')
    
    data = com.sm_approve_get_test_list(1)

    for n, row in data.items():
        lims_id = row['lims_id']
        serial_number = row['serial_number']

        if serial_number[1:3] == '41':
            print('------- using SM User interface to approve assay: LIMS_ID {} serial num {}'.format(lims_id, serial_number))

            com.sm_approve_approve_test_by_serial_number_or_lims_id(
                sm_number=1,
                by="serial_number",
                serial_number_or_lims_id=serial_number,
                test_comment=com.get_random_approve_comment(),
                oos_comment=com.get_random_approve_comment(),
                general_comment=com.get_random_approve_comment(),
                mold_count=com.get_random_approve_mold_count())

    print('------- test is done -------')
    
