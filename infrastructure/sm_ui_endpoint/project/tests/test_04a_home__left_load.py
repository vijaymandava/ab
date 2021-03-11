import urllib3


# Get the test list from the approve screen
import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')

    URL = 'http://127.0.0.1:9100/sm_ui/'
    http = urllib3.PoolManager()

    print('------- sending request -------')

    r = http.request('GET', URL+'home/left_load', retries=False, timeout=60.0)

    print('------- response is here -------')
    print('r.headers = {}'.format(r.headers))
    print('r.status  = {}'.format(r.status))
    assert r.status == 200, "response has bad status"

    print('------- test done --------')
