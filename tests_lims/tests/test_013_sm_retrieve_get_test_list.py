import uuid
import json
import urllib3
import pytest
from tests_lims.tests.common import Common

# get list of assays on SM menu -> cancel
@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- start the test -------')
    
    data = com.sm_retrieve_get_test_list(1)

    # the test checks to confirm at least one "40" and one "41" assay
    # these are presumed started by earlier tests
    found40 = False
    found41 = False
    for n, row in data.items():
        lims_id = row['lims_id']
        serial_number = row['serial_number']
        if lims_id[0:2] == '40':
            found40 = True
            print('------- found LIMS_ID {} serial number {}'.format(lims_id, serial_number))
        if lims_id[0:2] == '41':
            found41 = True
            print('------- found LIMS_ID {} serial number {}'.format(lims_id, serial_number))

    assert found40, 'the test was expecting an assay with LIMS_ID 40xxxxxx and did not find it'
    assert found41, 'the test was expecting an assay with LIMS_ID 41xxxxxx and did not find it'

    print('------- test is done -------')
    
