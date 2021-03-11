import uuid
import json
import pytest
import time
from tests_lims.tests.common import Common

@pytest.mark.regression_lims_order_cancel
def test():

    com = Common()
    
    print('------- start the test -------')

    primary_ids = com.order_using_lims_web_api('case_93_lims_id_plus_sample_id_plus_serial_number', 5)
    print(primary_ids)
    ##time.sleep(10)
    # com.cancel_from_primary_ids(primary_ids)

    print('------- test is done -------')
