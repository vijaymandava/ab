# from common_settings_for_fe_be_tests import CommonSettingForFeBeTests
from infrastructure.sm_ui_endpoint.project.tests.common_settings_for_fe_be_tests import CommonSettingForFeBeTests


import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')
    common = CommonSettingForFeBeTests()

    user_name = "Operator"
    fields = {
        'user_name': user_name
    }

    print('------- get user {} -------'.format(user_name))
    r = common.http.request(
        method='get',
        url=common.url + 'users/get_user',
        fields=fields,
        retries=False,
        timeout=common.timeout)

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
    data = json.loads(r.data.decode('utf-8'))

    print('data decoded as json is type {}'.format(type(data)))
    print('data decoded as json = {}'.format(data))

    print('------- work with the response data --------')

    for key, value in data.items():
        print("{} {}".format(key, value))

    for key, value in data['privs_get'].items():
        print("{} {}".format(key, value))

    print('------- test done --------')

    print('------- test done --------')
