import uuid
import json
import urllib3
import pytest
from tests_lims.tests.common import Common

# get status of assays on SM menu
@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- start the test -------')
    
    com.sm_home_load(sm_number=1)

    print('------- test is done -------')

