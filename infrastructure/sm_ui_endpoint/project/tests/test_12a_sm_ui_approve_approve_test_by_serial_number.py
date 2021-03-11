import urllib3
import uuid
import random


# approve a test from the approve screen by serial number
import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')

    URL = 'http://127.0.0.1:9100/sm_ui/'
    http = urllib3.PoolManager()

    print('------- first get a list of tests listed on that UI -------')
    r = http.request(
        method='GET',
        url=URL+'approve/get_test_list',
        retries=False,
        timeout=60.0)
    print('------- response is here -------')
    print('r.headers = {}'.format(r.headers))
    print('r.status  = {}'.format(r.status))
    assert r.status == 200, "response has bad status"

    import json
    jdata = json.loads(r.data.decode('utf-8'))
    print('------- there are {} cassettes shown on that UI -------'.format(len(jdata)))

    # if no tests available it's OK - we ae done
    # # if tests available, continue to the approve section
    if (len(jdata) == 0):
        print('------- not a great run of this tests - nothing to approve! -------')
    else:
        # pick test in the list
        the_key = None
        n = str(len(jdata)-1)
        for [key, value] in jdata.items():
            print('{} {}'.format(key, value))
            if value['serial_number'] != "E":
                the_key = key

        assert len(jdata) > 0, "there are no tests to cancel!"
        assert the_key is not None, "there are no tests with a serial number!"
        serial_number = jdata[the_key]['serial_number']
        print('------- test will target serial number {} -------'.format(serial_number))

        # specify serial number, generate random comments and mold count
        comment_max_len = 60
        fields = {
            'serial_number': serial_number,
            'test_comment': uuid.uuid4().hex.upper()[0:comment_max_len],
            'oos_comment': uuid.uuid4().hex.upper()[0:comment_max_len],
            'general_comment': uuid.uuid4().hex.upper()[0:comment_max_len],
            'mold_count': random.randrange(2, 20, 2)
        }

        print('------- issue the post -------')
        r = http.request(
            method='POST',
            url=URL+'approve/approve_test_by_serial_number',
            fields=fields,
            retries=False,
            timeout=120.0,)
    
        print('------- response is here -------')
        print('r.headers = {}'.format(r.headers))
        print('r.status  = {}'.format(r.status))
        assert r.status == 200, "response has bad status"

    print('------- test done --------')
