import urllib3


# Get the test list from the approve screen
import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')

    URL = 'http://127.0.0.1:9100/sm_ui/'

    http = urllib3.PoolManager()

    print('------- sending request -------')

    r = http.request('GET', URL+'approve/get_test_list', retries=False, timeout=60.0)

    print('------- response is here -------')
    print('r.headers = {}'.format(r.headers))
    print('r.status  = {}'.format(r.status))
    assert r.status == 200, "response has bad status"
    
    # decode the data as json
    import json
    jdata = json.loads(r.data.decode('utf-8'))

    print('------- work with the response data --------')

    print('there are {} cassettes available to approve'.format(len(jdata)))

    for n, row in jdata.items():
        print(row)

    print('------- test done --------')
