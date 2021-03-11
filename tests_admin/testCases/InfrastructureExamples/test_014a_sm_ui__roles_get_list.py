import json
import pytest
import urllib3
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@pytest.mark.infrastructureExamplesSmUiRoles
def test():
    logger = LogGen.loggen()

    url_sm_ui = ReadConfig.sm_user_interface()
    timeout = ReadConfig.timeout_sm()
    http = urllib3.PoolManager()

    ######### get list ###############
    logger.info('------- get list -------')

    r = http.request(
        method='GET',
        url=url_sm_ui+'roles/get_list',
        fields={},
        retries=False,
        timeout=timeout)

    logger.info('response is type {}'.format(type(r)))
    logger.info('headers is type  {}'.format(type(r.headers)))
    logger.info('status is type   {}'.format(type(r.status)))
    logger.info('data is type     {}'.format(type(r.data)))
    logger.info('r.headers = {}'.format(r.headers))
    logger.info('r.status  = {}'.format(r.status))
    logger.info('r.data    = {}'.format(r.data))

    assert r.status == 200, "response has bad status"
    data = json.loads(r.data.decode('utf-8'))

    print("Values from SM_UI  ::", data)

    logger.info('------- work with the response data --------')
    for key,value in data.items():
        logger.info("{} {}".format(key,value))
    logger.info('there are {}'.format(len(data)))

    logger.info('------- test done --------')
