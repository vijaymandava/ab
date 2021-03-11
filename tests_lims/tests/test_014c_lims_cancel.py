import uuid
import json
import urllib3
import pytest
from tests_lims.tests.common import Common

# from LIMS- cancel tests having serial number 41xxxxxx
@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- get the token -------')

    token = com.get_auth_token()

    print('------- create the LIMS cancel request -------')

    data = com.sm_retrieve_get_test_list(1)

    for n, row in data.items():
        lims_id = row['lims_id']
        serial_number = row['serial_number']

        if lims_id[0:2] == '42':
            print('------- using LIMS Cancel command to cancel assay: LIMS_ID {} serial num {}'.format(lims_id, serial_number))

            method = 'POST'
            url = com.get_cm_ip() + 'lims/postCancel'
    
            headers = {
                'accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': token,
                }

            fields = {}

            body_raw = {
                "instr_id": com.get_sm_inst_id(1),
                "lims_id": lims_id,
                "serial_number": '',
                "sample_id": '',
                "lot_batch_id": '',
                }

            body_encoded = json.dumps(body_raw).encode('utf-8')

            print('------- issue the LIMS cancel request to CM -------')
            r = com.http.request(
                method=method,
                url=url,
                headers=headers,
                fields=fields,
                body=body_encoded,
                retries=False,
                timeout=120.0)

            print('------- response from CM is here -------')
            assert r.status == 200, "response has bad status"

            print('------- test done --------')













    print('------- test is done -------')
    
