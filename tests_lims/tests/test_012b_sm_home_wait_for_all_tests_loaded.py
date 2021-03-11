import uuid
import json
import urllib3
import time
import pytest

# poll the SM UI until all tests are shown as loaded
# or more accurately, no tests should be "Ordered"
#
# As reference - progression of assay state on main UI follows:
#
# With just order and no load...
#
#   (order) -> Ordered -> (cancel) -> Cancelled -> (approve) -> none/gone
#
# With load but CFU stays below thresholds...
#
#   (order) -> Ordered -> (load) > Active -> (cancel) -> Cancelled  -> ...
#   (order) -> Ordered -> (load) > Active -> (trash)  -> Cancelled  -> ...
#
# With load and CFU hits threshold...
#
#   (order) -> Ordered -> (load) -> (cfu above alert)  -> Alert         -> ...
#   (order) -> Ordered -> (load) -> (cfu above action) -> Action        -> ...
#   (order) -> Ordered -> (load) -> (cfu above spec)   -> Specification -> ...
#   (order) -> Ordered -> (load) -> (cfu above passed) -> Passed        -> ...
#
# With load and CFU does not hit threshold...
#
#   (order) -> Ordered -> (load) -> (cfu not above threshold) -> Passed (by not exceeding any CFU threshold)

from tests_lims.tests.common import Common
@pytest.mark.regression_infrastructure

def test():

    com = Common()

    print('------- start the test -------')
 
    tries_remaining = 30
    while tries_remaining > 0:
        data = com.sm_home_get_test_list(1)
        done = com.no_assays_in_any_of_the_following_states(
            actual_states=data,
            unacceptable_states=['Ordered'])
        if done:
            break
        else:
            tries_remaining-=1
            print('------- one or more assays with status=[Ordered]. Will wait. tries_remaining={} -------'.format(tries_remaining))
            time.sleep(1)

    assert tries_remaining > 0, "timeout waiting for assay status"

    print('------- test is done -------')
    
