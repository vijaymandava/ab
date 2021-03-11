import inspect
import sys
import json

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.http import JsonResponse
from django.apps import apps

from lib import api_home_ui, api_approve_ui, api_retrieve_ui
from lib import api_user_roles, api_users

from app_sm_api.common import log_this


# @csrf_exempt
#def no_match(request):
#    log_this(__name__, inspect.stack()[0][3], '(start)')
#
#    strr = """-----not an api url---"""
#
#    log_this(__name__, inspect.stack()[0][3], '(end)')
#    return HttpResponse(strr)



# @csrf_exempt
def home_get_test_list(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    my_nav = apps.get_app_config('app_sm_api').nav
    print(type(my_nav))
    print("---------------")
    data = api_home_ui.get_test_list(my_nav)
    response = JsonResponse(data, safe=False)

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def approve_get_test_list(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    my_nav = apps.get_app_config('app_sm_api').nav
    data = api_approve_ui.get_test_list(my_nav)
    response = JsonResponse(data, safe=False)

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def retrieve_get_test_list(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    my_nav = apps.get_app_config('app_sm_api').nav
    data = api_retrieve_ui.get_test_list(my_nav)
    response = JsonResponse(data, safe=False)

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def home_left_load(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    my_nav = apps.get_app_config('app_sm_api').nav
    data = api_home_ui.left_load(my_nav)
    response = JsonResponse(data, safe=False)

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def approve_approve_test_by_serial_number(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')
    response = __do_approve_approve_test_by_serial_number_or_lims_id(request, "serial_number")
    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


def approve_approve_test_by_lims_id(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')
    response = __do_approve_approve_test_by_serial_number_or_lims_id(request, "lims_id")
    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


def __do_approve_approve_test_by_serial_number_or_lims_id(request, by):

    my_nav = apps.get_app_config('app_sm_api').nav

    if request.method == 'POST':
        log_this()
        log_this(__name__)
        log_this(__name__, "-- call the api implementation --------")
        log_this(__name__, "-- post parameters are:")
        log_this(__name__, request.POST)

        try:
            if (by == "serial_number"):
                in_identifier   = request.POST['serial_number']
            elif (by == 'lims_id'):
                in_identifier = request.POST['lims_id']
            else:
                raise LookupError('parameter missing - need either serial_number or lims_id')
            in_test_comment    = request.POST['test_comment']
            in_oos_comment     = request.POST['oos_comment']
            in_general_comment = request.POST['general_comment']
            in_mold_count      = request.POST['mold_count']
        except Exception as e:
            log_this(__name__, ('Oops! missing one of: serial_number, lis_id, test_comment, oos_comment, general_comment, mold_count ', app_path))
            log_this(__name__, ('got a ', e.__class__))
            sys.exit()

        data = api_approve_ui.approve_test_by_serial_number_or_lims_id(
            nav=my_nav,
            by=by,
            number_or_id=in_identifier,
            test_comment=in_test_comment,
            oos_comment=in_oos_comment,
            general_comment=in_general_comment,
            mold_count=in_mold_count)

        response = JsonResponse(data, safe=False)

    else:
        assert False, "request to API was not a POST!"
        response = HttpResponseNotFound('request is not a POST !!!')

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def retrieve_cancel_test_by_serial_number(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')
    response = __do_retrieve_cancel_test_by_serial_number(request, "serial_number")
    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def retrieve_cancel_test_by_lims_id(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')
    response = __do_retrieve_cancel_test_by_serial_number(request, "lims_id")
    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


def __do_retrieve_cancel_test_by_serial_number(request, by):

    my_nav = apps.get_app_config('app_sm_api').nav

    if request.method == 'POST':
        log_this()
        log_this(__name__)
        log_this(__name__, "-- call the api implementation --------")
        log_this(__name__, "-- post parameters are:")
        log_this(__name__, request.POST)

        try:
            if (by == "serial_number"):
                in_identifier = request.POST['serial_number']
            elif (by == 'lims_id'):
                in_identifier = request.POST['lims_id']
            else:
                raise LookupError('parameter missing - need either serial_number or lims_id')

        except Exception as e:
            log_this(__name__, ('Oops! missing: serial_number or lims_id', app_path))
            log_this(__name__, ('got a ', e.__class__))
            sys.exit()

        data = api_retrieve_ui.cancel_test_by_serial_number_or_lims_id(
            nav=my_nav,
            by=by,
            number_or_id=in_identifier)

        response = JsonResponse(data, safe=False)

    else:
        assert False, "request to API was not a POST!"
        response = HttpResponseNotFound('request is not a POST !!!')

    return response


# @csrf_exempt
def roles_get_list(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    my_nav = apps.get_app_config('app_sm_api').nav
    data = api_user_roles.get_list(my_nav)
    response = JsonResponse(data, safe=False)

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


 # @csrf_exempt
def  roles_get_role(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    try:    
        name = request.GET['name']

    except Exception as e:
        description = 'Oops! missing name'
        log_this(__name__, (description))
        log_this(__name__, ('got a ', e.__class__))
        raise LookupError(description)

    my_nav = apps.get_app_config('app_sm_api').nav
    data = api_user_roles.get_role(
        nav = my_nav,
        name = name)

    response = JsonResponse(data, safe=False)

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def  roles_create_role(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    if request.method == 'POST':

        if request.body is not None:

            my_nav = apps.get_app_config('app_sm_api').nav

            data = api_user_roles.create_role(
                nav=my_nav,
                params_encoded=request.body)

            if data in [None, ""]:
                response = JsonResponse("", safe=False)
            else:
                response = HttpResponseBadRequest(data)

        else:
            response = HttpResponseBadRequest('request is missing body)')

    else:
        response = HttpResponseBadRequest('request is not a POST')

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response



# @csrf_exempt
def  roles_update_role(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    if request.method == 'POST':
    
        if request.body is not None:

            my_nav = apps.get_app_config('app_sm_api').nav

            data = api_user_roles.update_role(
                nav=my_nav,
                params_encoded=request.body)

            if data in [None, ""]:
                response = JsonResponse("", safe=False)
            else:
                response = HttpResponseBadRequest(data)

        else:
            response = HttpResponseBadRequest('request is missing body)')

    else:
        response = HttpResponseBadRequest('request is not a POST')

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def  roles_delete_role(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    if request.method == 'POST':
    
        if request.body is not None:

            my_nav = apps.get_app_config('app_sm_api').nav

            data = api_user_roles.delete_role(
                nav=my_nav,
                params_encoded=request.body)

            if data in [None, ""]:
                response = JsonResponse("", safe=False)
            else:
                response = HttpResponseBadRequest(data)

        else:
            response = HttpResponseBadRequest('request is missing body)')

    else:
        response = HttpResponseBadRequest('request is not a POST')

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response

##########################################

# @csrf_exempt
def users_get_list(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    my_nav = apps.get_app_config('app_sm_api').nav
    data = api_users.get_list(my_nav)
    response = JsonResponse(data, safe=False)

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response



# @csrf_exempt
def  users_get_user(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    try:    
        user_name = request.GET['user_name']

    except Exception as e:
        description = 'Oops! missing user_name'
        log_this(__name__, (description))
        log_this(__name__, ('got a ', e.__class__))
        raise LookupError(description)

    my_nav = apps.get_app_config('app_sm_api').nav
    data = api_users.get_user(
        nav = my_nav,
        name = user_name)

    response = JsonResponse(data, safe=False)

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def  users_create_user(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    if request.method == 'POST':

        if request.body is not None:

            my_nav = apps.get_app_config('app_sm_api').nav

            data = api_users.create_user(
                nav=my_nav,
                params_encoded=request.body)

            if data in [None, ""]:
                response = JsonResponse("", safe=False)
            else:
                response = HttpResponseBadRequest(data)

        else:
            response = HttpResponseBadRequest('request is missing body)')

    else:
        response = HttpResponseBadRequest('request is not a POST')

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response



# @csrf_exempt
def  users_update_user(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    if request.method == 'POST':
    
        if request.body is not None:

            my_nav = apps.get_app_config('app_sm_api').nav

            data = api_users.update_user(
                nav=my_nav,
                params_encoded=request.body)

            if data in [None, ""]:
                response = JsonResponse("", safe=False)
            else:
                response = HttpResponseBadRequest(data)

        else:
            response = HttpResponseBadRequest('request is missing body)')

    else:
        response = HttpResponseBadRequest('request is not a POST')

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def  users_disable_user(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    if request.method == 'POST':
    
        if request.body is not None:

            my_nav = apps.get_app_config('app_sm_api').nav

            data = api_users.disable_user(
                nav=my_nav,
                params_encoded=request.body)

            if data in [None, ""]:
                response = JsonResponse("", safe=False)
            else:
                response = HttpResponseBadRequest(data)

        else:
            response = HttpResponseBadRequest('request is missing body)')

    else:
        response = HttpResponseBadRequest('request is not a POST')

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response


# @csrf_exempt
def  users_enable_user(request):
    log_this(__name__, inspect.stack()[0][3], '(start)')

    if request.method == 'POST':
    
        if request.body is not None:

            my_nav = apps.get_app_config('app_sm_api').nav

            data = api_users.enable_user(
                nav=my_nav,
                params_encoded=request.body)

            if data in [None, ""]:
                response = JsonResponse("", safe=False)
            else:
                response = HttpResponseBadRequest(data)

        else:
            response = HttpResponseBadRequest('request is missing body)')

    else:
        response = HttpResponseBadRequest('request is not a POST')

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return response

