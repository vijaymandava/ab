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
    lims_id = com.get_unique_lims_id()
    serial_number = ""
    lot_batch = ""
    sample_list = ['', '']  # note - this is the error case - multiple tests ordered using same LIMS_ID and no sample - first should be accepted second should be rejected
    mm = "mm10000"
    aa = "aa"
    hr = "hr"

    loop_num = 0
    for sample_id in sample_list:

        # junky sleep so can figure out the SM logfiles which loop it is
        loop_num += 1
        import time
        time.sleep(3)

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
        if loop_num == 1:
            assert r.status == 200, "response has bad status: expected 200 observed {}".format(r.status)
        if loop_num == 2:
            assert r.status != 200, "response has GOOD status: expected !200 observed {}".format(r.status)




    print('------- test done --------')
