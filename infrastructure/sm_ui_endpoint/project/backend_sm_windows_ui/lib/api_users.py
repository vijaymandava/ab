import json
import inspect
# from app_sm_api.common import log_this
import pandas as pd

from infrastructure.sm_ui_endpoint.project.frontend_api_endpoint.project_endpoint.app_sm_api.common import log_this


def find_and_select(target_name, list_view):
    num = -1
    found = False
    for x in list_view:
        num += 1
        if (x.texts()[0] == target_name):
            list_view[num].select()
            found = True
            break
    return [found, list_view[num]]


def get_list(nav, verbose=False):

    log_this(__name__, inspect.stack()[0][3], '(start)')
    nav.confirm_home()

    # transition UI
    nav.dialog['home'].menu().click()
    nav.dialog['menu'].users().click()

    list_view = nav.dialog['users'].users_list()

    columns = ['name', 'enabled']
    key = 'name'
    df_accumulate = pd.DataFrame([], columns=columns)
    for x in list_view:
        if verbose:
            print(x.texts())
        current_display_df = pd.DataFrame([x.texts()], columns=columns)
        df_accumulate = df_accumulate.append(current_display_df, ignore_index=False, verify_integrity=False, sort=False)
    df_rationalized = df_accumulate.drop_duplicates(subset=key, keep='last', inplace=False, ignore_index=False)
    df_indexed_by_name = df_rationalized.set_index(keys=key, drop=True, append=False, inplace=False, verify_integrity=True)
    # df_indexed_by_name.sort_index(inplace=True)

    # the_results = df_indexed_by_name.to_dict(orient='dict')
    # the_results = df_indexed_by_name.to_dict(orient='list')
    # the_results = df_indexed_by_name.to_dict(orient='series')
    # the_results = df_indexed_by_name.to_dict(orient='split')
    # the_results = df_indexed_by_name.to_dict(orient='records')
    the_results = df_indexed_by_name.to_dict(orient='index')

    # go home
    nav.dialog['user_roles'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return the_results


def get_user(nav, name):

    log_this(__name__, inspect.stack()[0][3], '(start)', name)
    nav.confirm_home()

    # transition UI
    nav.dialog['home'].menu().click()
    nav.dialog['menu'].users().click()

    list_view = nav.dialog['users'].users_list()

    # select from the list
    [found, control] = find_and_select(name, list_view)
 
    the_results = {}
    if found:
        the_results['first']      = nav.dialog['users'].first().texts()[0]
        the_results['middle']     = nav.dialog['users'].middle().texts()[0]
        the_results['last']       = nav.dialog['users'].last().texts()[0]
        the_results['username']   = nav.dialog['users'].username().texts()[0]
        the_results['email']      = nav.dialog['users'].email().texts()[0]
        # the_results['password_a'] = nav.dialog['users'].password_a().texts()[0]
        the_results['phone']      = nav.dialog['users'].phone().texts()[0]
        # the_results['password_b'] = nav.dialog['users'].password_b().texts()[0]
        the_results['extension']  = nav.dialog['users'].extension().texts()[0]

        # the_results['role']  = nav.dialog['users'].user_role().texts()[0]
        the_results['role'] = 'not implemented'

        privs_get = {}
        # get list of controls for the privs buttons
        controls = nav.dialog['users'].get_privs_controls()

        for name, control in controls.items():
            the_control_value = control.get_toggle_state()
            privs_get[name] = the_control_value

        the_results['privs_get'] = privs_get

    # go home
    nav.dialog['users'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return the_results


def create_user(nav, params_encoded):

    log_this(__name__, inspect.stack()[0][3], '(start)', params_encoded)
    nav.confirm_home()

    try:
        params_decoded = json.loads(params_encoded)
        first = params_decoded['first']
        middle = params_decoded['middle']
        last = params_decoded['last']
        username = params_decoded['username']
        email = params_decoded['email']
        password = params_decoded['password']
        phone = params_decoded['phone']
        extension = params_decoded['extension']
        role = params_decoded['role_name']  
    except Exception as e:
        this_err = 'missing one or more parameters - was given {}'.format(params_encoded)
        raise RuntimeError(this_err) from e

    # transition UI
    nav.dialog['home'].menu().click()
    nav.dialog['menu'].users().click()

    nav.dialog['users'].new().click()

    nav.dialog['users'].first().type_keys(first)
    nav.dialog['users'].middle().type_keys(middle)
    nav.dialog['users'].last().type_keys(last)
    nav.dialog['users'].username().type_keys(username)
    nav.dialog['users'].email().type_keys(email)
    nav.dialog['users'].password_a().type_keys(password)
    nav.dialog['users'].phone().type_keys(phone)
    nav.dialog['users'].extension().type_keys(extension)
    nav.dialog['users'].password_b().type_keys(password)

    # dropdown for role
    the_combo_box = nav.dialog['users'].role_combo_box()
    # dlg_app =   nav.dialog['users'].app.window(title=r'GrowthDirect2', top_level_only=True)
    # the_combo_box = dlg_app.child_window(auto_id="cmb_UserRoles", control_type="ComboBox")
    the_combo_box.type_keys("%{DOWN}")

    x = the_combo_box.children()
    num = -1
    for y in x:
        num += 1
        y.click_input()
        # print("========")
        # print("texts {}".format(y.texts()))
        # print("window_text {}".format(y.window_text()))
        # print("element info {}".format(y.element_info))
        # z = y.get_properties()
        if (y.texts()[0] == role):
            #print('{} {}'.format(num, role))
            the_combo_box.select(num)
            break

    nav.dialog['users'].save().click()

    # go home
    nav.dialog['users'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return


def update_user(nav, params_encoded):

    log_this(__name__, inspect.stack()[0][3], '(start)')
    nav.confirm_home()

    try:
        params_decoded = json.loads(params_encoded)
        first = params_decoded['first']
        middle = params_decoded['middle']
        last = params_decoded['last']
        username = params_decoded['username']
        email = params_decoded['email']
        password = params_decoded['password']
        phone = params_decoded['phone']
        extension = params_decoded['extension']
        role = params_decoded['role_name']
    except Exception as e:
        this_err = 'missing one or more parameters - was given {}'.format(params_encoded)
        raise RuntimeError(this_err) from e

    # transition UI
    nav.dialog['home'].menu().click()
    nav.dialog['menu'].users().click()

    # pick user from "Users" list
    list_view = nav.dialog['users'].users_list()

    # select from the list
    [found, control] = find_and_select(username, list_view)

    if (found):
        nav.dialog['users'].edit().click()

        nav.dialog['users'].first().set_text(first)
        nav.dialog['users'].middle().set_text(middle)
        nav.dialog['users'].last().set_text(last)
        # nav.dialog['users'].username().set_text(username) not enabled - makes sense
        nav.dialog['users'].email().set_text(email)
        nav.dialog['users'].password_a().set_text(password)
        nav.dialog['users'].phone().set_text(phone)
        nav.dialog['users'].extension().set_text(extension)
        nav.dialog['users'].password_b().set_text(password)

        # dropdown
        the_combo_box = nav.dialog['users'].role_combo_box()
        the_combo_box.type_keys("%{DOWN}")

        x = the_combo_box.children()
        num = -1
        for y in x:
            num += 1
            y.click_input()
            # print("========")
            # print("texts {}".format(y.texts()))
            # print("window_text {}".format(y.window_text()))
            # print("element info {}".format(y.element_info))
            # z = y.get_properties()
            if (y.texts()[0] == role):
                the_combo_box.select(num)
                break

        nav.dialog['users'].save().click()

    # go home
    nav.dialog['users'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return


def disable_user(nav, params_encoded):

    log_this(__name__, inspect.stack()[0][3], '(start)')
    nav.confirm_home()

    try:
        params_decoded = json.loads(params_encoded)
        username = params_decoded['username']
    except Exception as e:
        this_err = 'missing one or more parameters - was given {}'.format(params_encoded)
        raise RuntimeError(this_err) from e

    # transition UI
    nav.dialog['home'].menu().click()
    nav.dialog['menu'].users().click()

    # pick user from "Users" list
    list_view = nav.dialog['users'].users_list()

    # select from the list
    [found, control] = find_and_select(username, list_view)

    if found:
        nav.dialog['users'].disable().click()

    # go home
    nav.dialog['users'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return


def enable_user(nav, params_encoded):

    log_this(__name__, inspect.stack()[0][3], '(start)')
    nav.confirm_home()

    try:
        params_decoded = json.loads(params_encoded)
        username =  params_decoded['username']
    except Exception as e:
        this_err = 'missing one or more parameters - was given {}'.format(params_encoded)
        raise RuntimeError(this_err) from e

    # transition UI
    nav.dialog['home'].menu().click()
    nav.dialog['menu'].users().click()

    # pick user from "Users" list
    list_view = nav.dialog['users'].users_list()

    # select from the list
    [found, control] = find_and_select(username, list_view)

    if found:
        nav.dialog['users'].enable().click()

    # go home
    nav.dialog['users'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return