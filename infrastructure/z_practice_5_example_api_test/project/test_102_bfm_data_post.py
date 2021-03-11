import urllib.request
import json
from pprint import pprint
from datetime import datetime

# perform a POST to the BFM
# expect a "200" response


def test_1_post_api():

    url = 'http://127.0.0.1:9000/sm_rx/post_order'

    # get a timestamp
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d_%H%M%S_%f")

    values = {
        'instr_id': '4',
        'lims_id': dt_string,
        'serial_number': '6',
        'sample_id': '7',
        'lot_batch_id': '8',
        'method_name': '9',
        'handling_rule_name': '0',
        'action_alert_level_name': '1',
        'aal_cfu_threshold_alert': '2',
        'aal_cfu_threshold_action': '3',
        'aal_cfu_threshold_specification': '4',
        'aal_cfu_threshold_pass': '5',
        'comment': 'this is a comment',
        }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    data = json.dumps(values).encode("utf-8")
    pprint(data)

    try:
        req = urllib.request.Request(
            url=url,
            data=data,
            headers=headers,
            method='POST',)

        res = urllib.request.urlopen(
            url=req,
            data=data,
            timeout=4)

        print('----here-----')
        print(type(res))
        print(res.status)
        # print(res.getvalue())
        # print(res.content)
        assert res.status == 200, 'response status code is incorrect!'

    except Exception as e:
        print('----exception-----')
        pprint(e)
        assert False, 'exception'

    # assert False

