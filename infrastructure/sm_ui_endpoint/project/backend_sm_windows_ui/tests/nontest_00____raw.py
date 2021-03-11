
import sys
from pywinauto.application import Application
# from pywinauto import handleprops
from pywinauto.timings import Timings


Timings.fast()  # divide all timings by two (~2x faster)

app_path = r'C:\Program Files\GrowthDirect2\GDSystem.exe'

try:
    application = Application(backend='uia').connect(
        path=app_path,
        allow_magic_lookup=True)
        # formerly uia
except Exception as e:
    print('Oops! when trying to connect to application ', app_path)
    print('got a ', e.__class__)
    print('note you need to run powershell as administrator to connect to SM')
    sys.exit()

# GD starts out at home page dialog
#dlg = app[r'GrowthDirect2']
#try:
#    dlg.wait('ready')
#except Exception as e:
#    print('Oops! when waiting for home dialog to become ready... ', app_path)
#    print('got a ', e.__class__)
#    print('note you need to start with System Manager on the HOME UI!')
#    sys.exit()
#print('GDsystem.exe - is ready')


#dlg = app['GrowthDirect2']
#pywin_ctl = dlg["Button2"]
#pywin_ctl.click()

#dlg = app['GrowthDirect2']
#pywin_ctl = dlg['User RolesButton']
#pywin_ctl.click()

#dlg = app['GrowthDirect2']
#pywin_ctl = dlg['Button1']
#pywin_ctl.click()

def do_it():
    
    print(type(application)) # app is an Application

    dlg_app = application.window(title=r'GrowthDirect2')
    #dlg_app.print_control_identifiers()
    dlg_app.draw_outline()
    component = dlg_app.child_window(title="Select Tests to Approve", control_type="Text")
    component.draw_outline()
    blah = component.parent()
    blah.click()
    exit(1)





    dlg_home_menubutton = dlg_app.window(best_match="Button2", control_type="Button", top_level_only=True)


    dlg_menu_homebutton = dlg_app.window(best_match="Button1", control_type="Button", top_level_only=True)
    #dlg_menu_group = dlg_app.window(title="Menu Options", control_type="Group")
    #dlg_menu_methodsbutton = dlg_app.window(best_match="MethodsButtonZONA", control_type="Button", top_level_only=False)

    dlg_home_menubutton.click()
    d = application.window(title=r'GrowthDirect2')
    d.print_control_identifiers()

    dlg_menu_methodsbutton.click()
    dlg_menu_homebutton.click()


# Exception has occurred: MatchError       (note: full exception trace is shown but execution is paused at: _run_module_as_main)
# Could not find 'MethodsButtonZONA' in 'dict_keys(['Button', 'Button0', 'Button1', 'Button2', 'Button3', 'Button4', 'Button5', 'Button6',
#  'Button7', 'Button8', 'Button9', 'Button10', 'Button11', 'Button12', 'Button13', 'Button14', 'Button15', 'Button16', 'Button17',
#   'Button18', 'Button19', 'Button20', 'Button21', 'Button22', 'Button23', 'Button24', 'Button25', 'Button26', 'Button27', 'Button28',
#    'Button29', 'Button30', 'Button31', 'Button32', 'Button33', 'Button34', 'Button35', 'Button36', 'Button37', 'EmptyButton', 
#    'Empty', 'Button38', 'EmptyButton0', 'EmptyButton1', 'EmptyButton2', 'Empty0', 'Empty1', 'Empty2', 'Button39', 'EmptyButton3', 
#    'Empty3', 'Button40', 'EmptyButton4', 'Empty4', 'Button41', 'EmptyButton5', 'Empty5', 'Button42', 'EmptyButton6', 'Empty6',
#     'Button43', 'Button44', 'Button45', 'Button46'])'





    # ####################
    dlg_home = application.window(title=r'GrowthDirect2')
    #dlg_home.print_control_identifiers(depth=3)
    dlg_home_menubutton = dlg_home.window(best_match="Button2", control_type="Button", top_level_only=True)
    dlg_home_menubutton.click()

    dlg_menu = application.window(title=r'GrowthDirect2')
    dlg_menu_group = dlg_menu.window(title="Menu Options", control_type="Group")
    #dlg_menu.print_control_identifiers(depth=4)

    dlg_menu_homebutton = dlg_menu.window(best_match="Button1", control_type="Button", top_level_only=True)
    #dlg_menu_methodsbutton = dlg_menu_group.window(title="MethodsButton", control_type="Button")
    dlg_menu_methodsbutton = dlg_menu_group.window(best_match="MethodsButton", control_type="Button", top_level_only=False)
    #dlg_menu_methodsbutton = dlg_menu.window(auto_id="menuButton", control_type="Custom")
    #dlg_menu_methodsbutton = dlg_menu.window(best_match="MethodsCustom", control_type="Custom")
    dlg_menu_methodsbutton.click()
    dlg_menu_homebutton.click()

    print(dlg_menu_homebutton)


    for x in range(10):
        #dlg2 = dlg['Button2']
        #print(dlg2.exists())
        #dlg2.click()

        dlg3 = dlg.window(best_match="Button2", control_type="Button", top_level_only=True)
        #dlg3 = dlg.window(best_match="Button2", control_type="Button", top_level_only=False)
        #dlg3 = dlg.window(best_match="Button2", top_level_only=True)
        #dlg3 = dlg.window(best_match="Button2", top_level_only=False)
        print(dlg3.exists())

  


    #pywinauto.findwindows.find_elements(class_name=None,
    # class_name_re=None,
    # parent=None, 
    # process=None, 
    # title=None, 
    # title_re=None, 
    # top_level_only=True, 
    # visible_only=True, 
    # enabled_only=False, 
    # best_match=None, 
    # handle=None, 
    # ctrl_index=None, 
    # found_index=None, 
    # predicate_func=None, 
    # active_only=False, 
    # control_id=None, 
    # control_type=None, 
    # auto_id=None, 
    # framework_id=None, 
    # backend=None, depth=None)



import time
tic = time.perf_counter()
do_it()
toc = time.perf_counter()
print(f"elapsed time {toc - tic:0.4f} seconds")




