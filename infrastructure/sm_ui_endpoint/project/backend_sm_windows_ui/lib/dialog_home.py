import sys
# from dialog__base import DialogBase
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog__base import DialogBase


class DialogHome(DialogBase):

        # .print_control_identifiers()
        # .draw_outline()

        def menu(self):
            dlg_app = self.nav.pre_call_tasks()
            the_component = dlg_app.child_window(best_match='Button2', control_type="Button")
            return the_component

        def print(self):
            dlg_app = self.nav.pre_call_tasks()
            the_component = dlg_app.child_window(best_match='Print', control_type="Button")
            return the_component

        def left_load(self):
            dlg_app = self.nav.pre_call_tasks()
            the_component = dlg_app.child_window(best_match='Left Load', control_type="Button")
            return the_component

        def right_load(self):
            dlg_app = self.nav.pre_call_tasks()
            the_component = dlg_app.child_window(best_match='Right Load', control_type="Button")
            return the_component

        def approve(self):
            dlg_app = self.nav.pre_call_tasks()
            the_component = dlg_app.child_window(best_match='ApproveButton', control_type="Button")
            return the_component

        def retrieve(self):
            dlg_app = self.nav.pre_call_tasks()
            the_component = dlg_app.child_window(best_match='RetrieveButton1', control_type="Button")
            return the_component

        def open_trash_bin(self):
            dlg_app = self.nav.pre_call_tasks()
            the_component = dlg_app.child_window(best_match='RetrieveButton2', control_type="Button")
            return the_component

        def open_output_queue(self):
            dlg_app = self.nav.pre_call_tasks()
            the_component = dlg_app.child_window(best_match='RetrieveButton3', control_type="Button")
            return the_component

        def test_list(self):
            dlg_app = self.nav.pre_call_tasks()
            the_component = dlg_app.child_window(best_match='TestsListView', control_type="DataGrid")
            return the_component


