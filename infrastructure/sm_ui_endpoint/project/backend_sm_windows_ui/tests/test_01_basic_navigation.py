import pytest
# from navigation import Navigation
from pywinauto import actionlogger
# get through testbench init and navigate a few pages
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.navigation import Navigation


@pytest.mark.sm_backend_tests
def test():

    actionlogger.enable()

    nav = Navigation()
    nav.start()
    nav.setup_controls_and_dialogs()

    print('\ntest start')

    print('--------testing home ---------')

    y = nav.dialog['home']. menu()
    y.draw_outline()
    y = nav.dialog['home']. print()
    y.draw_outline()
    y = nav.dialog['home']. left_load()
    y.draw_outline()
    y = nav.dialog['home']. right_load()
    y.draw_outline()
    y = nav.dialog['home']. approve()
    y.draw_outline()
    y = nav.dialog['home']. retrieve()
    y.draw_outline()
    y = nav.dialog['home']. open_trash_bin()
    y.draw_outline()
    y = nav.dialog['home']. open_output_queue()
    y.draw_outline()
    y = nav.dialog['home']. test_list()
    y.draw_outline()

    print('--------testing approve ---------')

    y = nav.dialog['home'].approve()
    y.click()

    y = nav.dialog['approve'].home()
    y.draw_outline()
    y = nav.dialog['approve'].menu()
    y.draw_outline()
    y = nav.dialog['approve'].approve()
    y.draw_outline()
    y = nav.dialog['approve'].save()
    y.draw_outline()
    y = nav.dialog['approve'].test_list()
    y.draw_outline()
    y = nav.dialog['approve'].test_comment()
    y.draw_outline()
    y = nav.dialog['approve'].oos_comment()
    y.draw_outline()
    y = nav.dialog['approve'].general_comment()
    y.draw_outline()
    y = nav.dialog['approve']. mold_count()
    y.draw_outline() # broken
  
    y = nav.dialog['approve'].home()
    y.click()

    print('--------testing retrieve---------')

    y = nav.dialog['home'].retrieve()
    y.click()

    y = nav.dialog['retrieve']. home()
    y.draw_outline()
    y = nav.dialog['retrieve']. menu()
    y.draw_outline()
    y = nav.dialog['retrieve']. cancel()
    y.draw_outline()
    y = nav.dialog['retrieve']. retrieve()
    y.draw_outline()
    y = nav.dialog['retrieve']. trash()
    y.draw_outline()
    y = nav.dialog['retrieve']. test_list()
    y.draw_outline()

    y = nav.dialog['retrieve']. home()
    y.click()

    print('--------testing user roles---------')

    y = nav.dialog['home']. menu()
    y.click()
    y = nav.dialog['menu']. user_roles()
    y.click()

    y = nav.dialog['user_roles']. home()
    y.draw_outline()
    y = nav.dialog['user_roles']. menu()
    y.draw_outline()
    y = nav.dialog['user_roles']. new()
    y.draw_outline()
    y = nav.dialog['user_roles']. edit()
    y.draw_outline()
    y = nav.dialog['user_roles']. save()
    y.draw_outline()
    y = nav.dialog['user_roles']. delete()
    y.draw_outline()  
    y = nav.dialog['user_roles']. cancel()
    y.draw_outline()
    #################################
    y = nav.dialog['user_roles']. user_roles_list()
    y.draw_outline()
    ################################# 
    y = nav.dialog['user_roles']. methods_create()
    y.draw_outline()
    y = nav.dialog['user_roles']. methods_edit()
    y.draw_outline()
    y = nav.dialog['user_roles']. methods_delete()
    y.draw_outline()
    y = nav.dialog['user_roles']. aa_create()
    y.draw_outline()
    y = nav.dialog['user_roles']. aa_edit()
    y.draw_outline()
    y = nav.dialog['user_roles']. aa_delete()
    y.draw_outline()

    y = nav.dialog['user_roles']. home()
    y.click()

    print('--------testing users---------')

    y = nav.dialog['home']. menu()
    y.click()
    y = nav.dialog['menu']. users()
    y.click()

    y = nav.dialog['users']. home()
    y.draw_outline()
    y = nav.dialog['users']. menu()
    y.draw_outline()
    y = nav.dialog['users']. new()
    y.draw_outline()
    y = nav.dialog['users']. edit()
    y.draw_outline()
    y = nav.dialog['users']. save()
    y.draw_outline()
    y = nav.dialog['users']. cancel()
    y.draw_outline()
    y = nav.dialog['users']. disable()
    y.draw_outline()
    #################################
    y = nav.dialog['users']. users_list()
    y.draw_outline()
    #################################        
    y = nav.dialog['users']. first()
    y.draw_outline()
    y = nav.dialog['users']. middle()
    y.draw_outline()
    y = nav.dialog['users']. last()
    y.draw_outline()
    y = nav.dialog['users']. username()
    y.draw_outline()
    y = nav.dialog['users']. email()
    y.draw_outline()
    y = nav.dialog['users']. password_a()
    y.draw_outline()
    y = nav.dialog['users']. phone()
    y.draw_outline()
    y = nav.dialog['users']. password_b()
    y.draw_outline()
    y = nav.dialog['users']. extension()
    y.draw_outline()
    y = nav.dialog['users'].  user_role_combo_box()
    y.draw_outline()
    #y = nav.dialog['users'].  user_role_entry("Administrator")
    #y.draw_outline()

    ################################
    y = nav.dialog['users']. methods_create()
    y.draw_outline()
    y = nav.dialog['users']. methods_edit()
    y.draw_outline()
    y = nav.dialog['users']. methods_delete()
    y.draw_outline()
    y = nav.dialog['users']. aa_create()
    y.draw_outline()
    y = nav.dialog['users']. aa_edit()
    y.draw_outline()
    y = nav.dialog['users']. aa_delete()
    y.draw_outline()

    y = nav.dialog['users']. home()
    y.click()

    print('test is done')
