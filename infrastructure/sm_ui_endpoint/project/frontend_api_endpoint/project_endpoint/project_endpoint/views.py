import inspect

from django.http import HttpResponse
from django.http import JsonResponse
from django.apps import apps

from lib import api_home_ui, api_approve_ui, api_retrieve_ui

from app_sm_api.common import log_this

# @csrf_exempt
def welcome(request):
    log_this(__name__, inspect.stack()[0][3])

    strr = """Welcome to the SM User Interface API
<p>
The API commands are:
<br>

<ul>
<li>(GET)  sm_ui/home/get_test_list -> returns the assays shown on the home menu
<li>(GET)  sm_ui/home/left_load -> pushes the "left load" button
<li>(GET)  sm_ui/approve/get_test_list -> returns the assays shown on the approve menu

<li>(POST) sm_ui/approve/approve_test_by_serial_number -> approves test using serial number as identifier
<ul>
parameters:
<li>serial_number
<li>test_comment
<li>oos_comment
<li>general_comment
<li>mold_count

</ul>
<li>(POST) sm_ui/approve/approve_test_by_lims_id -> approves test using LIMS ID as identifier
<ul>
parameters:
<li>lims_id
<li>test_comment
<li>oos_comment
<li>general_comment
<li>mold_count
</ul>

<li>(GET)  sm_ui/retrieve/get_test_list -> returns the assays shown on the retrieve menu

<li>(POST) sm_ui/retrieve/cancel_test_by_serial_number -> cancels test using serial number as identifier
<ul>
parameters:
<li>serial_number
</ul>

<li>(POST) sm_ui/retrieve/cancel_test_by_lims_id -> cancels test using LIMS ID as identifier
<ul>
parameters:
<li>lims_id
</ul>

</ul>
"""

    return HttpResponse(strr)
