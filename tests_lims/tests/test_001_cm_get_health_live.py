import pytest
from tests_lims.tests.common import Common

@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- start test -------')

    method = 'GET'
    url = com.get_cm_ip() + 'health/live'
    # url = com.CM_IP
    headers = {}
    fields = {}

    print('------- issue the request -------')
    r = com.http.request(
        method=method,
        url=url,
        headers=headers,
        fields=fields,
        retries=False,
        timeout=120.0)

    print('------- response is here -------')
    print('r.headers = {}'.format(r.headers))
    print('r.status  = {}'.format(r.status))
    assert r.status == 200, "response has bad status"

    print('------- test done --------')
