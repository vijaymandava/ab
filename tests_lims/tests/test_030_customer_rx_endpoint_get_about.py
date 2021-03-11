import pytest
import json

from tests_lims.tests.common import Common

@pytest.mark.regression_lims_timepoints
def test():

    com = Common()

    print('------- start test -------')

    method = 'GET'
    url = com.get_customer_lims_ip() + 'welcome'
    headers = {}
    fields = {}

    print(url)
    print('------- issue the request -------')
    r = com.http.request(
        method=method,
        url=url,
        headers=headers,
        fields=fields,
        retries=False,
        timeout=120.0)


    print('------- response is here -------')
    print(type(r))

    assert r.status == 200, "response has bad status"

    jdata = json.loads(r.data.decode('utf-8'))
    message = jdata['message']
    assert message == 'welcome'

    print('------- test done --------')
