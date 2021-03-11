import uuid
import json
import pytest
import time
from tests_lims.tests.common import Common

# This test closely follows JAMA test description - refer to
# https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/160693?projectId=50

@pytest.mark.regression_lims_order_cancel
def test():

    com = Common()
    
    print('------- start the test -------')

    primary_ids = com.order_using_lims_web_api("case_0_lims_id", 1)
    print(primary_ids)
    ##time.sleep(10)
    com.cancel_from_primary_ids(primary_ids)

    print('------- test is done -------')
