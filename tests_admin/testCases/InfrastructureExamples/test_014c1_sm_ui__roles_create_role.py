from datetime import datetime
import pytest
import urllib3
import json
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

@pytest.mark.infrastructureExamplesSmUiRoles
def test():
    logger = LogGen.loggen()

    url_sm_ui = ReadConfig.sm_user_interface()
    timeout = ReadConfig.timeout_sm()
    http = urllib3.PoolManager()

    ######### create role ###############
    role_name = "test_" + datetime.now().strftime('%y%m%d%H%M%S%f')
    logger.info('------- create role with privs alternating one/zero {}'.format(role_name))

    body_raw = {
        'name': role_name,
        'privs_set': {
            'methods_create': '1',
            'methods_edit': '0',
            'methods_delete': '1',
            'aa_create': '0',
            'aa_edit': '1',
            'aa_delete': '0'}}
    body_encoded = json.dumps(body_raw).encode('utf-8')

    r = http.request(
        method='POST',
        url=url_sm_ui+'roles/create_role',
        body=body_encoded,
        headers={'Content-Type': 'application/json'},
        retries=False,
        timeout=timeout)


    ######### get/check ###############
    logger.info('------- get/check role -------')

    name = "Administrator"
    fields = {
        'name': role_name,
    }

    r = http.request(
        method='GET',
        url=url_sm_ui+'roles/get_role',
        fields=fields,
        retries=False,
        timeout=timeout)

    assert r.status == 200, "response has bad status"
    data = json.loads(r.data.decode('utf-8'))

    assert data['privs_get']['methods_create'] == 1
    assert data['privs_get']['methods_edit'] == 0
    assert data['privs_get']['methods_delete'] == 1
    assert data['privs_get']['aa_create'] == 0
    assert data['privs_get']['aa_edit'] == 1
    assert data['privs_get']['aa_delete'] == 0

    logger.info('------- test done --------')

