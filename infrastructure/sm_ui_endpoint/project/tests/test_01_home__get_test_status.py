import urllib3


# Get the test list from the SM home screen
import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')

    URL = 'http://127.0.0.1:9100/sm_ui/'

    http = urllib3.PoolManager()

    print('------- sending request -------')

    r = http.request('GET', URL+'home/get_test_list', retries=False, timeout=60.0)

    print('------- response is here -------')
    print('response is type {}'.format(type(r)))
    print('headers is type  {}'.format(type(r.headers)))
    print('status is type   {}'.format(type(r.status)))
    print('data is type     {}'.format(type(r.data)))
    print('r.headers = {}'.format(r.headers))
    print('r.status  = {}'.format(r.status))
    print('r.data    = {}'.format(r.data))

    assert r.status == 200, "response has bad status"

    # decode the data as json
    import json
    jdata = json.loads(r.data.decode('utf-8'))

    print('data decoded as json is type {}'.format(type(jdata)))
    print('data decoded as json = {}'.format(jdata))

    print('------- work with the response data --------')

    print('there are {} cassettes listed'.format(len(jdata)))

    for n, row in jdata.items():
        print(row)
        if row.get('status') == 'Passed':
            print('that test passed')

    print('------- test done --------')
