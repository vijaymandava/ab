# from dialog__base import DialogBase
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog__base import DialogBase


class DialogRetrieve(DialogBase):

        # .print_control_identifiers()
        # .draw_outline()

    def home(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='Button1', control_type='Button')
        return the_component
        
    def menu(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='Button2', control_type="Button")
        return the_component

    def cancel(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='Cancel', control_type='Button')
        return the_component

    def retrieve(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='Retrieve', control_type='Button')
        return the_component

    def trash(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(best_match='Trash', control_type='Button')
        return the_component

    def test_list(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(auto_id="lsv_testList", control_type="DataGrid")
        return the_component
