# from dialog__base import DialogBase
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog__base import DialogBase


class DialogMethods(DialogBase):

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