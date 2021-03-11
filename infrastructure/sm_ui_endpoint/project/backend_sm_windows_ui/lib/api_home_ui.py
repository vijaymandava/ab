import time
import inspect
# from app_sm_api.common import log_this
from infrastructure.sm_ui_endpoint.project.frontend_api_endpoint.project_endpoint.app_sm_api.common import log_this


def __get_data_from_row(data_item):
    results = {}

    x = 0
    for c in data_item.children():

        x += 1

        if x == 1:
            value = c.texts()[0]
            results["lot_batch"] = value
        if x == 2:
            value = c.texts()[0]
            results['sample_id'] = value
        if x == 3:
            value = c.texts()[0]
            results['lims_id'] = value
        if x == 4:
            value = c.children()[0].texts()[0]
            results['count'] = value
        if x == 5:
            value = c.texts()[0]
            results['status'] = value
        if x == 6:
            value = c.texts()[0]
            results['location'] = value
        if x == 7:
            value = c.children()[0].texts()[0]
            results['next_image'] = value
        if x == 8:
            value = c.children()[0].texts()[0]
            results['serial_number'] = value

    return results


def __get_data_from_table(list_view):

    results = {}
    index = 0
    for data_item in list_view.items():
        results[index] = __get_data_from_row(data_item)
        index += 1
    return results



def get_test_list(nav):

    log_this(__name__, inspect.stack()[0][3], '(start)')
    dlg_app = nav.confirm_home()

    list_view = nav.dialog['home'].test_list()
 
    try:
        y = __get_data_from_table(list_view)
    except Exception as e:
        print('FAIL--> with: ' + str(e.__class__))
        print('-------- will wait, retry------')
        time.sleep(3)
        y = __get_data_from_table(list_view)
        print('-------- retry sucessful ------')

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return y      


def left_load(nav):

    log_this(__name__, inspect.stack()[0][3], '(start)')
    dlg_app = nav.confirm_home()

    nav.dialog['home'].left_load().click()
    y = ''

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return y

