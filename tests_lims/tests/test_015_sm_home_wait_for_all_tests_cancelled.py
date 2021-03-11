import uuid
import json
import urllib3
import time
import pytest
from tests_lims.tests.common import Common

# poll the SM UI until all tests are shown as cancelled

@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- start the test -------')
 
    tries_remaining = 30
    while tries_remaining > 0:
        data = com.sm_home_get_test_list(1)
        done = com.no_assays_in_any_of_the_following_states(
            actual_states=data,
            unacceptable_states=['Ordered', 'Active'])
        if done:
            break
        else:
            tries_remaining-=1
            print('------- one or more assays with status=[Ordered, Active]. Will wait. tries_remaining={} -------'.format(tries_remaining))
            time.sleep(1)

    assert tries_remaining > 0, "timeout waiting for assay status"

    print('------- test is done -------')
    
