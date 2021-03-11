import uuid
import json
import pytest
from tests_lims.tests.common import Common

# This test closely follows JAMA test description - refer to
# https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/160693?projectId=50

@pytest.mark.regression_lims_order_cancel
def test():

    com = Common()

    print('------- get the token -------')

    token_raw = com.get_auth_token()

    print('------- create the LIMS order request -------')

    method = 'POST'
    url = com.get_cm_ip() + 'lims/postOrder'

    instr_id = com.get_sm_inst_id(1)
    lims_id = ""
    serial_number = ""
    lot_batch = com.get_unique_lot_batch_id()
    sample_list = ['s0', 's1', 's2']
    sample_list = ['s0']  #zona
    mm = ""
    aa = ""
    hr = ""

    for sample_id in sample_list:

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token_raw,
            }

        fields = {}

        body_raw = {
            "instr_id": instr_id,
            "lims_id": lims_id,
            "serial_number": serial_number,
            "sample_id": sample_id,
            "lot_batch_id": lot_batch,
            "method_name": mm,
            "handling_rule_name": hr,
            "action_alert_level_name": aa,
            "aal_cfu_threshold_alert": '',
            "aal_cfu_threshold_action": '',
            "aal_cfu_threshold_specification": '',
            "aal_cfu_threshold_pass": '',
            "comment": com.get_random_comment_order(),
            }

        print('--------------body raw-----------------')
        print(body_raw)

        body_encoded = json.dumps(body_raw).encode('utf-8')

        print('------- issue the LIMS order request to CM -------')
        r = com.http.request(
            method=method,
            url=url,
            headers=headers,
            fields=fields,
            body=body_encoded,
            retries=False,
            timeout=120.0)

        print('------- response from CM is here -------')
        print('r.headers =\n{}'.format(r.headers))
        print('r.status  =\n{}'.format(r.status))
        print('r.data    =\n{}'.format(r.data))
        assert r.status == 200, "response has bad status: expected 200 observed {}".format(r.status)






    # ############### cancel 

    for sample_id in sample_list:

        print('------- create the LIMS cancel request -------')

        token_raw = com.get_auth_token()

        method = 'POST'
        url = com.get_cm_ip() + 'lims/postCancel'

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token_raw,
            }

        fields = {}

        body_raw = {
            "instr_id": instr_id,
            "lims_id": lims_id,
            "serial_number": serial_number,
            "sample_id": sample_id,
            "lot_batch_id": lot_batch,
            }

        print('--------------body raw-----------------')
        print(body_raw)

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







    print('------- test done --------')
