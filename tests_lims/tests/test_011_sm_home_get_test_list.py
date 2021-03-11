import uuid
import json
import urllib3
import pytest
import time
from tests_lims.tests.common import Common

# get status of assays on SM menu
@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- start the test -------')
    
    tries_remaining = 30
    while tries_remaining > 0:

        data = com.sm_home_get_test_list(1)

        # the test checks to confirm at least one "40" and one "41" assay
        # these are presumed started by earlier tests
        found40 = False
        found41 = False
        found42 = False
        for n, row in data.items():
            lims_id = row['lims_id']
            serial_number = row['serial_number']

            # workaround in case we don't get complete status from UI... zona
            if 'status' in row:
                if row['status'] == 'Ordered' and lims_id[0:2] == '40':
                    found40 = True
                    print('------- found LIMS_ID {} serial number {}'.format(lims_id, serial_number))
                if row['status'] == 'Ordered' and lims_id[0:2] == '41':
                    found41 = True
                    print('------- found LIMS_ID {} serial number {}'.format(lims_id, serial_number))
                if row['status'] == 'Ordered' and lims_id[0:2] == '42':
                    found42 = True
                    print('------- found LIMS_ID {} serial number {}'.format(lims_id, serial_number))

        if found40 and found41 and found42:
            break
        else:
            tries_remaining-=1
            print('------- waiting for ordered... 40={} 41={} 42={} -------'.format(found40, found41, found42))
            time.sleep(1)

    assert found40, 'the test was expecting an assay with LIMS_ID 40xxxxxx and did not find it'
    assert found41, 'the test was expecting an assay with LIMS_ID 41xxxxxx and did not find it'
    assert found42, 'the test was expecting an assay with LIMS_ID 42xxxxxx and did not find it'

    print('------- test is done -------')
    
