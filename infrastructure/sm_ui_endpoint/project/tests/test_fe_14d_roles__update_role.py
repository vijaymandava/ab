from datetime import datetime
import json
# from common_settings_for_fe_be_tests import CommonSettingForFeBeTests
from infrastructure.sm_ui_endpoint.project.tests.common_settings_for_fe_be_tests import CommonSettingForFeBeTests


import pytest
@pytest.mark.sm_frontend_tests
def test():

    print('------- test start --------')
    common = CommonSettingForFeBeTests()

    ################# create ################
    role_name = "test_" + datetime.now().strftime('%y%m%d%H%M%S%f')
    print('------- create role with privs alternating one/zero {}'.format(role_name))

    body_raw = {
        'name': role_name,
        'privs_set': {
            'methods_create': '1',
            'methods_edit': '1',
            'methods_delete': '1',
            'aa_create': '0',
            'aa_edit': '0',
            'aa_delete': '0'}}
    body_encoded = json.dumps(body_raw).encode('utf-8')

    print('------- issue the command -------')
    r = common.http.request(
        method='POST',
        url=common.url + 'roles/create_role',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)

    assert r.status == 200, "response has bad status {} {}".format(r.status, r.data)


    ############## update ############
    print('------- update some privs in that role {}'.format(role_name))

    body_raw = {
        'name': role_name,
        'privs_set': {
            'methods_create': '1',
            'methods_edit': '0',
            #'methods_delete': '1',
            'aa_create': '1',
            'aa_edit': '0',
            #'aa_delete': '0'
            }}
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = common.http.request(
        method='POST',
        url=common.url + 'roles/update_role',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=common.timeout)

    assert r.status == 200, "response has bad status"

    ############## check ######################
    print('------- check {}'.format(role_name))
    
    fields = {
        'name': role_name,
    }

    r = common.http.request(
        method='GET',
        url=common.url + 'roles/get_role',
        fields=fields,
        retries=False,
        timeout=common.timeout)

    assert r.status == 200, "response has bad status"
    data = json.loads(r.data.decode('utf-8'))

    assert data['privs_get']['methods_create']==1
    assert data['privs_get']['methods_edit']==0
    assert data['privs_get']['methods_delete']==1
    assert data['privs_get']['aa_create']==1
    assert data['privs_get']['aa_edit']==0
    assert data['privs_get']['aa_delete']==0

    print('------- test done --------')
