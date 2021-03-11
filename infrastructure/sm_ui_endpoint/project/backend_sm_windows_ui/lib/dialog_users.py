# from dialog__base import DialogBase
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog__base import DialogBase


class DialogUsers(DialogBase):

    def top(self):
        return self.app.window(title=r'GrowthDirect2')

    # .print_control_identifiers()
    # .draw_outline()

    def home(self):
        dlg_app = self.nav.pre_call_tasks()
        #dlg_app.print_control_identifiers()
        the_component = dlg_app.child_window(best_match='Button1', control_type='Button')
        return the_component

    def menu(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='Button2', control_type='Button')
        return the_component

    def new(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='NewButton2', control_type='Button')
        return the_component

    def edit(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='EditButton', control_type='Button')
        return the_component

    def save(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='SaveButton', control_type='Button')
        return the_component

    def cancel(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='CancelButton', control_type='Button')
        return the_component

    def disable(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='DisableButton', control_type='Button')
        return the_component

    def enable(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='EnableButton', control_type='Button')
        return the_component

#################################

    def users_list(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="lsv_Users", control_type="DataGrid").wrapper_object()
        return the_component

    def enabled(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(title="Enabled", control_type="HeaderItem")
        return the_component

#################################

    def first(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="txb_FirstName", control_type="Edit")
        return the_component        

    def middle(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="txb_MiddleInitial", control_type="Edit")
        return the_component

    def last(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="txb_LastName", control_type="Edit")
        return the_component

    def username(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="txb_UserName", control_type="Edit")
        return the_component

    def email(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="txb_EmailAddress", control_type="Edit")
        return the_component

    def password_a(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="FirstPasswordBox", control_type="Edit")
        return the_component
    def phone(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="txb_Telephone", control_type="Edit")
        return the_component

    def password_b(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="SecondPasswordBox", control_type="Edit")
        return the_component

    def extension(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="txb_Ext", control_type="Edit")
        return the_component

    def user_role_combo_box(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="cmb_UserRoles", control_type="ComboBox")
        return the_component

    def user_role_entry(self, title):
        #dlg_app = self.app.window(title=r'GrowthDirect2', top_level_only=True)
        dlg_app = self.nav.pre_call_tasks()
        the_combo_box = dlg_app.child_window(auto_id="cmb_UserRoles", control_type="ComboBox")
        the_component = the_combo_box.child_window(title="Operator", control_type="Text", top_level_only=True)
        return the_component

    def role_combo_box(self):
        dlg_app = self.nav.pre_call_tasks()
        # dlg_app =   nav.dialog['users'].app.window(title=r'GrowthDirect2', top_level_only=True)
        the_combo_box = dlg_app.child_window(auto_id="cmb_UserRoles", control_type="ComboBox")
        return the_combo_box

# ###############################
    def get_privs_controls(self):
        dlg_app = self.nav.pre_call_tasks()
        # dlg_app.print_control_identifiers()

        comp = {}
        comp['methods_create'] = dlg_app.child_window(best_match='MethodsCheckBox1', control_type='CheckBox')
        comp['methods_edit']   = dlg_app.child_window(best_match='MethodsCheckBox2', control_type='CheckBox')
        comp['methods_delete'] = dlg_app.child_window(best_match='MethodsCheckBox3', control_type='CheckBox')

        comp['aa_create'] = dlg_app.child_window(best_match='CheckBox4', control_type='CheckBox')
        comp['aa_edit']   = dlg_app.child_window(best_match='CheckBox5', control_type='CheckBox')
        comp['aa_delete'] = dlg_app.child_window(best_match='CheckBox6', control_type='CheckBox')

        comp['hr_create'] = dlg_app.child_window(best_match='CheckBox7', control_type='CheckBox')
        comp['hr_edit']   = dlg_app.child_window(best_match='CheckBox8', control_type='CheckBox')
        comp['hr_delete'] = dlg_app.child_window(best_match='CheckBox9', control_type='CheckBox')

        comp['samples_create'] = dlg_app.child_window(best_match='CheckBox10', control_type='CheckBox')
        comp['samples_edit']   = dlg_app.child_window(best_match='CheckBox11', control_type='CheckBox')
        comp['samples_delete'] = dlg_app.child_window(best_match='CheckBox12', control_type='CheckBox')

        comp['wl_create'] = dlg_app.child_window(best_match='CheckBox13', control_type='CheckBox')
        comp['wl_edit']   = dlg_app.child_window(best_match='CheckBox14', control_type='CheckBox')
        comp['wl_delete'] = dlg_app.child_window(best_match='CheckBox15', control_type='CheckBox')

        comp['users_create'] = dlg_app.child_window(best_match='CheckBox24', control_type='CheckBox')
        comp['users_modify'] = dlg_app.child_window(best_match='CheckBox25', control_type='CheckBox')
        comp['users_en_dis'] = dlg_app.child_window(best_match='CheckBox26', control_type='CheckBox')

        comp['roles_create'] = dlg_app.child_window(best_match='CheckBox27', control_type='CheckBox')
        comp['roles_modify'] = dlg_app.child_window(best_match='CheckBox28', control_type='CheckBox')
        comp['roles_delete'] = dlg_app.child_window(best_match='CheckBox29', control_type='CheckBox')

        comp['tests_n_labels_order'] = dlg_app.child_window(best_match='CheckBox30', control_type='CheckBox')
        comp['tests_n_labels_load'] = dlg_app.child_window(best_match='CheckBox31', control_type='CheckBox')
        comp['tests_n_labels_print'] = dlg_app.child_window(best_match='CheckBox32', control_type='CheckBox')

        comp['cassette_ops_cancel']   = dlg_app.child_window(best_match='CheckBox16', control_type='CheckBox')
        comp['cassette_ops_retrieve'] = dlg_app.child_window(best_match='CheckBox17', control_type='CheckBox')
        comp['cassette_ops_approve']  = dlg_app.child_window(best_match='CheckBox18', control_type='CheckBox')
        comp['cassette_ops_cleanup']  = dlg_app.child_window(best_match='CheckBox19', control_type='CheckBox')

        comp['lims_edit_settings'] = dlg_app.child_window(best_match='CheckBox20', control_type='CheckBox')
        comp['lims_print']         = dlg_app.child_window(best_match='CheckBox21', control_type='CheckBox')
        comp['lims_modify']        = dlg_app.child_window(best_match='CheckBox22', control_type='CheckBox')
        comp['lims_edit_results']  = dlg_app.child_window(best_match='CheckBox23', control_type='CheckBox')

        comp['sys_ack_alarms']         = dlg_app.child_window(best_match='CheckBox33', control_type='CheckBox')
        comp['sys_ack_sys_errs']       = dlg_app.child_window(best_match='CheckBox34', control_type='CheckBox')
        comp['sys_ack_service_issues'] = dlg_app.child_window(best_match='CheckBox35', control_type='CheckBox')
        comp['sys_empty_trash']        = dlg_app.child_window(best_match='CheckBox39', control_type='CheckBox')

        comp['sys_administer_system']  = dlg_app.child_window(best_match='CheckBox36', control_type='CheckBox')
        comp['sys_edit_gen_settings']  = dlg_app.child_window(best_match='CheckBox37', control_type='CheckBox')
        comp['sys_edit_it_settings']   = dlg_app.child_window(best_match='CheckBox38', control_type='CheckBox')
        comp['sys_maintenance']        = dlg_app.child_window(best_match='CheckBox40', control_type='CheckBox')

        comp['sys_service']            = dlg_app.child_window(best_match='CheckBox41', control_type='CheckBox')
        comp['sys_send_system_logs']   = dlg_app.child_window(best_match='CheckBox42', control_type='CheckBox')

        # for k,v in comp.items():
        #     v.draw_outline() # zona
        return comp

 


