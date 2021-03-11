from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog__base import DialogBase


class DialogApprove(DialogBase):

    def home(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='Button1', control_type="Button")
        return the_component

    def menu(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='Button2', control_type="Button")
        return the_component

    def approve(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='ApproveButton', control_type="Button")
        return the_component

    def save(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='SaveButton', control_type="Button")
        return the_component

    def test_list(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="lsv_cassetteList", control_type="DataGrid")
        return the_component

    def test_comment(self):
        dlg_app = self.nav.pre_call_tasks()
        #dlg_app.print_control_identifiers()
        #the_component = dlg_app.child_window(auto_id="txb_TestComment", control_type="Edit")
        #the_component = dlg_app.child_window(auto_id="txb_TestComment", control_type="Edit")
        the_component = dlg_app.child_window(auto_id="txb_TestComment", control_type="Edit")
        return the_component

    def oos_comment(self):
        dlg_app = self.nav.pre_call_tasks()
        #the_component = dlg_app.child_window(auto_id="txb_EventComment", control_type="Edit")
        the_component = dlg_app.child_window(auto_id="txb_EventComment", control_type="Edit")
        return the_component

    def general_comment(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="txb_GeneralComment", control_type="Edit")
        return the_component

    def mold_count(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='Edit4', control_type="Edit")
        return the_component


