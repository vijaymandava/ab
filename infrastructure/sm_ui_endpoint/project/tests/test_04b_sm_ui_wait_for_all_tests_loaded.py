import urllib3
import time

def no_assays_in_any_of_the_following_states(actual_states, unacceptable_states):

    acceptable = True
    for key,value in actual_states.items():
        if value['status'] in unacceptable_states:
            acceptable = False
            break
    return acceptable


# Get the test list from the approve screen
import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')

    URL = 'http://127.0.0.1:9100/sm_ui/'
    http = urllib3.PoolManager()

    tries_remaining = 30
    while tries_remaining > 0:

        print('------- sending request -------')

        # r = http.request('GET', URL+'home/get_test_list', retries=False, timeout=240.0)
        r = http.request('GET', URL+'home/get_test_list', retries=False)

        print('------- response is here -------')
        print('r.headers = {}'.format(r.headers))
        print('r.status  = {}'.format(r.status))
        assert r.status == 200, "response has bad status"
        
        # decode the data as json
        import json
        jdata = json.loads(r.data.decode('utf-8'))

        print('------- work with the response data --------')

        for n, row in jdata.items():
            print(row)


        done = no_assays_in_any_of_the_following_states(
            actual_states=jdata,
            unacceptable_states=['Ordered'])
        if done:
            break
        else:
            tries_remaining-=1
            print('------- one or more tests with status=Ordered. Will wait. tries_remaining={} -------'.format(tries_remaining))
            time.sleep(0)

    assert tries_remaining > 0, "timeout waiting for status != Ordered"



    print('------- test done --------')
