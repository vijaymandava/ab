import urllib3
import uuid
import random


# cancel a test from the retrieve screen by lims id
import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')

    URL = 'http://127.0.0.1:9100/sm_ui/'
    http = urllib3.PoolManager()

    print('------- first get a list of tests listed on that UI -------')
    r = http.request(
        method='GET',
        url=URL+'retrieve/get_test_list',
        retries=False,
        timeout=60.0)
    print('------- response is here -------')
    print('r.headers = {}'.format(r.headers))
    print('r.status  = {}'.format(r.status))
    assert r.status == 200, "response has bad status"

    import json
    jdata = json.loads(r.data.decode('utf-8'))
    print('------- there are {} cassettes shown on that UI -------'.format(len(jdata)))

    if (len(jdata) == 0):
        print('------- not a great run of this tests - nothing to approve! -------')
    else:

        # pick test in the list
        the_key = None
        # n = str(len(jdata)-1)
        for [key, value] in jdata.items():
            print('{} {}'.format(key, value))
            if value['lims_id'] != "":
                the_key = key

        if the_key == None:
            print('------- there are no tests with a LIMS_ID!')
        else:
            lims_id = jdata[the_key]['lims_id']
            print('------- test will target lims_id {} -------'.format(lims_id))

            # specify lims id
            fields = {
                'lims_id': lims_id,
            }

            print('------- issue the post -------')
            r = http.request(
                method='POST',
                url=URL+'retrieve/cancel_test_by_lims_id',
                fields=fields,
                retries=False,
                timeout=120.0,)
        
            print('------- response is here -------')
            print('r.headers = {}'.format(r.headers))
            print('r.status  = {}'.format(r.status))
            assert r.status == 200, "response has bad status"

    print('------- test done --------')
