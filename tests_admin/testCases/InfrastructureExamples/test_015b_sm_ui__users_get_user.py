from datetime import datetime
import pytest
import urllib3
import json
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig

@pytest.mark.infrastructureExamplesSmUiUsers
def test():
    logger = LogGen.loggen()

    url_sm_ui = ReadConfig.sm_user_interface()
    timeout = ReadConfig.timeout_sm()
    http = urllib3.PoolManager()

    ######### get user ###############
    logger.info('------- get user -------')

    name = "Administrator"
    fields = {
        'user_name': name,
    }

    r = http.request(
        method='GET',
        url=url_sm_ui+'users/get_user',
        fields=fields,
        retries=False,
        timeout=timeout,)

    logger.info('response is type {}'.format(type(r)))
    logger.info('headers is type  {}'.format(type(r.headers)))
    logger.info('status is type   {}'.format(type(r.status)))
    logger.info('data is type     {}'.format(type(r.data)))
    logger.info('r.headers = {}'.format(r.headers))
    logger.info('r.status  = {}'.format(r.status))
    logger.info('r.data    = {}'.format(r.data))

    assert r.status == 200, "response has bad status"
    data = json.loads(r.data.decode('utf-8'))

    logger.info('------- work with the response data --------')
    for key,value in data.items():
        logger.info("{} {}".format(key,value))
    logger.info('there are {}'.format(len(data)))

    assert data['privs_get']['methods_create'] == 1
    assert data['privs_get']['methods_edit'] == 1
    assert data['privs_get']['methods_delete'] == 1
    assert data['privs_get']['aa_create'] == 1
    assert data['privs_get']['aa_edit'] == 1
    assert data['privs_get']['aa_delete'] == 1

    logger.info('------- test done --------')
