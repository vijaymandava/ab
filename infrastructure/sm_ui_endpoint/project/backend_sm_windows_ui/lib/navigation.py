import sys
from pywinauto.application import Application
# from pywinauto import handleprops
from pywinauto.timings import Timings

# from dialog_home import DialogHome
# from dialog_menu import DialogMenu
# from dialog_methods import DialogMethods
# from dialog_retrieve import DialogRetrieve
# from dialog_approve import DialogApprove
# from dialog_signature_message_box import DialogSignatureMessageBox
# from dialog_user_roles import DialogUserRoles
# from dialog_users import DialogUsers
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog_approve import DialogApprove
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog_home import DialogHome
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog_menu import DialogMenu
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog_methods import DialogMethods
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog_retrieve import DialogRetrieve
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog_user_roles import DialogUserRoles
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog_users import DialogUsers


class Navigation(object):

    dialog = {}
    app_path = r'C:\Program Files\GrowthDirect2\GDSystem.exe'


    def confirm_home(self):

        # get the top level window specification and make sure it is "ready"
        dialog_current = self.app.window(title=r'GrowthDirect2', top_level_only=True)
        try:
            dialog_current.wait('ready')
        except Exception as e:
            print('Oops! when waiting for home dialog to become ready... ', self.app_path)
            print('got a ', e.__class__)
            print('note you need to start with System Manager on the HOME UI!')
            sys.exit()
        # print('GDsystem.exe - is ready')

        # sanity check - if the UI was left on some other dialog
        # then try to get back home by clicking the 'home' button
        # this is sort of ass-backward - we wait for the "home" button to be enabled
        home_button = dialog_current.window(best_match="Button1", control_type="Button", top_level_only=True)
        try:
            home_button.wait('enabled')
            print('---------UI was not the home page.  Returning to home page-----------')
            home_button.click()
            dialog_current.wait('ready')
            dialog_current = self.app.window(title=r'GrowthDirect2', top_level_only=True)
        except Exception as e:
            # print('UI is confirmed to be at the home page')
            # no need to do anything
            dummy = True


    def pre_call_tasks(self):
        try:
            dialog_current = self.app.window(title=r'GrowthDirect2', top_level_only=True)
        except Exception as e:
            assert False, "unable to get current dialog"
        return dialog_current


    def start(self):

        Timings.fast()  # divide all timings by two (~2x faster)
        #Timings.slow()  # divide all timings by two (~2x faster)

        try:
            self.app = Application(backend='uia').connect(
                path=self.app_path,
                allow_magic_lookup=False)
                # primary='uia'   alternative='win32'
        except Exception as e:
            print('Oops! when trying to connect to application ', self.app_path)
            print('got a ', e.__class__)
            print('note you need to run powershell as administrator to connect to SM')
            sys.exit(1)

        self.confirm_home()
        y = self.pre_call_tasks()
        assert y is not None, "unable to perform pre_call_tasls()"
        print('testbench is ready')

    def setup_controls_and_dialogs(self, verify=False):

        # construct dialog map
        self.dialog['home'] = DialogHome('home', self) #self.app)
        self.dialog['menu'] = DialogMenu('menu', self) #self.app)
        self.dialog['approve'] = DialogApprove('approve', self) # self.app)
        self.dialog['retrieve'] = DialogRetrieve('retrieve', self) # self.app)
        self.dialog['methods'] = DialogMethods('methods', self) # self.app)
        self.dialog['user_roles'] = DialogUserRoles('user roles', self) # self.app)
        self.dialog['users'] = DialogUsers('users', self) #self.app)

        # #self.dialog_map['dialog_signature_message_box'] = DialogSignatureMessageBox('dialog_signature_message_box')
        # self.dialog_map['user_roles'] = DialogUserRoles('user_roles')

        # # set the window specification for the controls on each dialog
        # # although it is not required to navigate to the dialog to create a window specification
        # # we do naviagate to the page so we can verify the window specifications as we make them
        # self.dialog_map['home'].set_controls(self.dlg)

        # self.control('home', 'menu').click() # go to that page
        # self.dialog_map['menu'].set_controls(self.dlg)
        # self.control('menu', 'home').click() # go to that page

        # self.dialog_map['approve'].set_controls(self.dlg)
        # self.dialog_map['retrieve'].set_controls(self.dlg)
        # #self.dialog_map['dialog_signature_message_box'] = DialogSignatureMessageBox('dialog_signature_message_box')
        # self.dialog_map['user_roles'].set_controls(self.dlg)




        # print(self.dialog_map)
        # print('zona')
        # #exit(1)
        # #for k,v in self.dialog_map.items():
        # #    v.set_controls(self.dlg)


        # # try a copule key clicks...
        # #zona want this self.control('home', 'menu').click()
        # #zona want this self.control('menu', 'home').click()


        # # verify...
        # #if verify:
        # #    self.dialog('home').verify(self)
        # #    self.control('home', 'menu').click()
        # #    self.dialog('menu').verify(self)
        # #    self.control('menu', 'methods').click()
        # #    self.dialog('methods').verify(self)
        # #    self.control('methods', 'home').click()
        # #    self.control('home', 'approve').click()
        # #    self.dialog('approve').verify(self)
        # #    self.control('approve', 'home').click()
        # #    self.control('home', 'retrieve').click
        # #    self.dialog('retrieve').verify(self)
        # #    self.control('retrieve', 'home').click
        # # there is no verify of signature_message_box

        print('testbench setup is done')
    
    # # def fish(self, depth):
        
    # #     self.dlg.wait("ready") # zona is this necessary?

    # #     self.dlg.print_control_identifiers(depth=depth)
    # #     #y = self.dlg._ctrl_identifiers() 
    # #     print('done fishing')
    # #     #print(str(y))
    # #     exit(0)

    # def control(self, dialog_name, control_friendly_name, force_fish=None):

    #     dialog = self.dialog_map[dialog_name]
    #     window_spec = dialog.window_spec[control_friendly_name]

    #     if (force_fish):
    #         print('--------window_spec.print_control_identifiers----------')
    #         window_spec.print_control_identifiers(99)
    #         print('--------self.dlg.print_control_identifiers----------')
    #         self.dlg.print_control_identifiers(99)

    #         exit(5)

    #     # window_spec.wait("ready") # zona is this necessary?

    #     return window_spec

    # #def dialog(self, dialog_name):
    # #    return self.dialog_map[dialog_name]

    # # def dialog_pywin(self, window_spec_name=None):

    # #     if window_spec_name:
    # #         dlg = self.app[window_spec_name]
    # #     else:
    # #         dlg = self.app['GrowthDirect2']

    # #     return dlg

    # def blink_check(self, dialog_name):

    #     dialog = self.dialog_map[dialog_name]
    #     for name,window_specification in dialog.window_spec.items():
    #         print('\nchecking {} {} {}'.format(dialog_name,name,window_specification))
    #         print('window_specification.criteria = {}'.format(window_specification.criteria))
    #         try:
    #             #print('zona commented out the checks...')
    #             window_specification.wait('exists')
    #             window_specification.draw_outline()
    #         except Exception as e:
    #             print('====================================')
    #             print('Oops! when attempting wait(exists), draw_outline()')
    #             print('got a ', e.__class__)
    #             print('fishing up windows specifications...')
    #             print('====================================')
    #             self.fish(99)
    #             print('====================================')
    #             sys.exit()




