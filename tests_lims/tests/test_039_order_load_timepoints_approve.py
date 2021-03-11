import uuid
import json
import pytest
import time
from tests_lims.tests.common import Common

@pytest.mark.regression_lims_timepoints
def test():

    com = Common()
    
    print('------- start the test -------')

    primary_ids = com.order_using_lims_web_api('case_91_lims_id_plus_serial_number', 1)
    print(primary_ids)

    # time.sleep(5)
    # com.cancel_from_primary_ids(primary_ids)

    print('------- test is done -------')
