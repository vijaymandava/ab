import json
import pytest
from tests_lims.tests.common import Common
import hashlib 

# This is test of getting auth token without using the
# common testbench routine "get_auth_token()"
# In other words - all the code to create and issue the
# http post is here in the test
# It's more verbose than the common testbench routine
# so may be helpful in debugging.
@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- start test -------')

    method = 'POST'
    url = com.get_cm_ip() + 'auth/login'
    headers = {
        'Content-Type': 'application/json',
        }

    password_cleartext = 'test@123'
    #md5_obj = hashlib.md5(password_cleartext)
    #password_md5 = md5_obj.hexdigest()
    #password_md5 = md5_obj.digest()

    fields = {}
    body_raw = {
        'userName': 'rmbadmin',
        'password': password_cleartext,
    }
    body_encoded = json.dumps(body_raw).encode('utf-8')

    print('------- the request is --------')
    print('method={}'.format(method))
    print('url={}'.format(url))
    print('headers={}'.format(headers))
    print('fields={}'.format(fields))
    print('body={}'.format(body_encoded))



    print('------- issue the request -------')
    r = com.http.request(
        method=method,
        url=url,
        headers=headers,
        fields=fields,
        body=body_encoded,
        retries=False,
        timeout=120.0)

    print('------- response is here -------')
    print('r.headers = {}'.format(r.headers))
    print('r.status  = {}'.format(r.status))
    print('r.data    = {}'.format(r.data))

    # check response status == 200
    assert r.status == 200, "response has bad status"

    # check the auth token is the right length
    jdata = json.loads(r.data.decode('utf-8'))
    token = jdata['authToken']
    print("------------here")
    print(type(token))

    assert len(token) == com.AUTH_TOKEN_EXPECTED_LENGTH_FROM_CM, 'auth token length: expected {}, observed {}'.format(
        com.AUTH_TOKEN_EXPECTED_LENGTH_FROM_CM,
        len(token))

    bearer_token = 'Bearer ' + token
    print('----------')
    print(bearer_token)
    print('------- test done --------')


