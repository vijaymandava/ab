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
    nav.dialog['menu'].user_roles().click()

    list_view = nav.dialog['user_roles'].user_roles_list()

    columns = ['name']
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


def get_role(nav, name):

    log_this(__name__, inspect.stack()[0][3], '(start)', name)
    nav.confirm_home()

    # transition UI
    nav.dialog['home'].menu().click()
    nav.dialog['menu'].user_roles().click()

    # select from the list
    list_view = nav.dialog['user_roles'].user_roles_list()
    [found, control] = find_and_select(name, list_view)

    the_results = {}
    privs_get = {}
    if found:
        the_results = {}
        the_results['role'] = name

        # get list of controls for the privs buttons
        controls = nav.dialog['user_roles'].get_privs_controls()

        for name, control in controls.items():
            the_control_value = control.get_toggle_state()
            privs_get[name] = the_control_value

        the_results['privs_get'] = privs_get

    # go home
    nav.dialog['user_roles'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return the_results


def create_role(nav, params_encoded):

    log_this(__name__, inspect.stack()[0][3], '(start)', params_encoded)
    nav.confirm_home()

    try:
        params_decoded = json.loads(params_encoded)
        name = params_decoded['name']
        privs_set = params_decoded['privs_set']
    except Exception as e:
        this_err = 'missing one or more parameters - was given {}'.format(params_encoded)
        raise RuntimeError(this_err) from e

    # transition UI
    nav.dialog['home'].menu().click()
    nav.dialog['menu'].user_roles().click()
    nav.dialog['user_roles'].new().click()

    # type the role name
    # zona - does not handle the case where the role already exists
    nav.dialog['user_roles'].role_name_textbox().type_keys(name)

    # get list of controls for the privs buttons
    controls = nav.dialog['user_roles'].get_privs_controls()

    # set the priv switches
    change_made = False
    for k, v in privs_set.items():
        # Button has 3 possible states 0,1, 2 where "2" means indeterminant...
        # so it may be necessary to toggle twice to get to the desired state
        for x in range(0, 2):
            try:
                the_control = controls[k]
                the_control_value = the_control.get_toggle_state()
                if str(the_control_value) != str(v):
                    the_control.toggle() 
                    change_made = True
            except KeyError as e:
                this_err = 'attempt to set role priv {} which does not exist in list {}'.format(k, controls.keys())
                raise KeyError(this_err) from e

    nav.dialog['user_roles'].save().click()

    nav.dialog['user_roles'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return


def update_role(nav, params_encoded):

    log_this(__name__, inspect.stack()[0][3], '(start)', params_encoded)
    nav.confirm_home()

    try:
        params_decoded = json.loads(params_encoded)
        name = params_decoded['name']
        privs_set = params_decoded['privs_set']
    except Exception as e:
        this_err = 'missing one or more parameters - was given {}'.format(params_encoded)
        raise RuntimeError(this_err) from e

    # transition UI
    nav.dialog['home'].menu().click()
    nav.dialog['menu'].user_roles().click()

    list_view = nav.dialog['user_roles'].user_roles_list()

    # select from the list
    [found, control] = find_and_select(name, list_view)

    if found:
        nav.dialog['user_roles'].edit().click()

        # get list of controls for the privs buttons
        controls = nav.dialog['user_roles'].get_privs_controls()

        # set the priv switches
        change_made = False

        for k, v in privs_set.items():
            # Button has 3 possible states 0,1, 2 where "2" means indeterminant...
            # so it may be necessary to toggle twice to get to the desired state
            for x in range(0, 2):
                try:
                    the_control = controls[k]
                    the_control_value = the_control.get_toggle_state()
                    if str(the_control_value) != str(v):
                        the_control.toggle() 
                        change_made = True
                except KeyError as e:
                    this_err = 'attempt to set role priv {} which does not exist in list {}'.format(k, controls.keys())
                    raise KeyError(this_err) from e

        if change_made:
            nav.dialog['user_roles'].save().click()
        else:
            nav.dialog['user_roles'].cancel().click()

    nav.dialog['user_roles'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return


def delete_role(nav, params_encoded):

    log_this(__name__, inspect.stack()[0][3], '(start)', params_encoded)
    nav.confirm_home()

    try:
        params_decoded = json.loads(params_encoded)
        name = params_decoded['name']
    except Exception as e:
        this_err = 'when deleting role, missing role name - was given {}'.format(params_encoded)
        raise RuntimeError(this_err) from e

    # transition UI
    nav.dialog['home'].menu().click()
    nav.dialog['menu'].user_roles().click()

    list_view = nav.dialog['user_roles'].user_roles_list()

    # select from the list
    [found, control] = find_and_select(name, list_view)

    if found:
        nav.dialog['user_roles'].delete().click()

    # go home
    nav.dialog['user_roles'].home().click()

    log_this(__name__, inspect.stack()[0][3], '(end)')
    return


