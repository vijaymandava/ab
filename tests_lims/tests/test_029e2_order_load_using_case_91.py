import uuid
import json
import pytest
import time
from tests_lims.tests.common import Common

@pytest.mark.regression_lims_order_cancel
def test():

    com = Common()
    
    print('------- start the test -------')

    primary_ids = com.order_using_lims_web_api('case_91_lims_id_plus_serial_number', 2)
    print(primary_ids)

    # time.sleep(5)
    # print('------- load -------')
    # com.sm_home_load(sm_number=1)
    
    print('------- test is done -------')
