import inspect
from app_sm_api.common import log_this


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
            results['serial_number'] = value
        if x == 5:
            value = c.texts()[0]
            results['status'] = value

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

    # transition UI
    nav.dialog['home'].approve().click()

    list_view = nav.dialog['approve'].test_list()

    y = __get_data_from_table(list_view)

    # go home
    nav.dialog['approve'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return y  


def approve_test_by_serial_number_or_lims_id(
    nav, by, number_or_id,
    test_comment, oos_comment, general_comment, mold_count):

    log_this(__name__, inspect.stack()[0][3], '(start)')
    dlg_app = nav.confirm_home()

    # transition UI
    nav.dialog['home'].approve().click()

    list_view = nav.dialog['approve'].test_list()

    for data_item in list_view.items():
        result = __get_data_from_row(data_item)

        if (
            (by == "serial_number" and (result.get('serial_number') == number_or_id))
            or
            (by == "lims_id" and (result.get('lims_id') == number_or_id))
        ):

            data_item.select()
            # data_item.click()

            nav.dialog['approve'].test_comment().type_keys(test_comment)
            nav.dialog['approve'].oos_comment().type_keys(oos_comment)
            nav.dialog['approve'].general_comment().type_keys(general_comment)
            nav.dialog['approve'].mold_count().type_keys(str(mold_count))
            nav.dialog['approve'].approve().click()

            #nav.control('approve', 'test_comment').type_keys(test_comment)
            #nav.control('approve', 'oos_comment').type_keys(oos_comment)
            #nav.control('approve', 'general_comment').type_keys(general_comment)
            #nav.control('approve', 'mold_count').type_keys(str(mold_count))
            #nav.control('approve', 'approve').click()
            # signature pop-up does not show up if single-sign-in is turned on
            # tb.control('signature_popup', 'ok', 'SignatureMessageBox').click()
            break

    # go home
    nav.dialog['approve'].home().click()
    log_this(__name__, inspect.stack()[0][3], '(end)')
    