import uuid
import json
import pytest
from tests_lims.tests.common import Common

# order LIMS 40xxxxxx using common routines
@pytest.mark.regression_infrastructure
def test():

    com = Common()

    print('------- get the token -------')

    token_raw = com.get_auth_token()
    [y, token_value] = token_raw.split()

    print('------- create the LIMS order request -------')

    method = 'POST'
    url = com.get_cm_ip() + 'lims/postOrder'

    # this test will create three orders with preface of [40,41,42] for LIMS_ID and SERIAL_NUMBER
    # the three tests will be later cancelled by later tests

    for prefix in ['40', '41', '42']:

        lims_id_generic = com.get_unique_lims_id()
        lims_id_specific = prefix + lims_id_generic[2:]

        # serial_number_generic = com.get_unique_serial_number_em_bb()
        # serial_number_specific = serial_number_generic[0] + prefix + serial_number_generic[3:]
        serial_number_specific = ""

        # sample_id = "s10000"  # hard code sample id
        sample_id = ""

        # lot_batch_id = "B11"
        lot_batch_id = ""


        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token_raw,
            }

        fields = {}

        body_raw = {
            "instr_id": com.get_sm_inst_id(1),
            "lims_id": lims_id_specific,
            "serial_number": serial_number_specific,
            "sample_id": sample_id,
            "lot_batch_id": lot_batch_id,
            "method_name": '',
            "handling_rule_name": '',
            "action_alert_level_name": '',
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

    print('------- test done --------')
