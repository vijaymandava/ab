import json
# from common_settings_for_fe_be_tests import CommonSettingForFeBeTests

import pytest

from infrastructure.sm_ui_endpoint.project.tests.common_settings_for_fe_be_tests import CommonSettingForFeBeTests


@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')
    common = CommonSettingForFeBeTests()


    ######### get list ###############
    print('------- get list -------')

    r = common.http.request(
        method='GET',
        url=common.url + 'roles/get_list',
        fields={},
        retries=False,
        timeout=common.timeout)

    print('response is type {}'.format(type(r)))
    print('headers is type  {}'.format(type(r.headers)))
    print('status is type   {}'.format(type(r.status)))
    print('data is type     {}'.format(type(r.data)))
    print('r.headers = {}'.format(r.headers))
    print('r.status  = {}'.format(r.status))
    print('r.data    = {}'.format(r.data))

    assert r.status == 200, "response has bad status"
    data = json.loads(r.data.decode('utf-8'))

    print('------- work with the response data --------')
    for key,value in data.items():
        print("{} {}".format(key,value))
    print('there are {}'.format(len(data)))

    print('------- test done --------')
