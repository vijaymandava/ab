import copy
# from dialog__base import DialogBase
from infrastructure.sm_ui_endpoint.project.backend_sm_windows_ui.lib.dialog__base import DialogBase


class DialogMenu(DialogBase):

    # .print_control_identifiers()
    # .draw_outline()

    def home(self):
        dlg_app = self.nav.pre_call_tasks()
        the_component = dlg_app.child_window(title="Back", auto_id="BrowseBack", control_type="Button")
        return the_component

    def approve(self):
        dlg_app = self.nav.pre_call_tasks()
        component = dlg_app.child_window(title="Select Tests to Approve", control_type="Text")
        the_component = component.parent()
        return the_component

    def user_roles(self):
        dlg_app = self.nav.pre_call_tasks()
        component = dlg_app.child_window(title="Create and Modify User Roles", control_type="Text")
        the_component = component.parent()
        return the_component

    def users(self):
        dlg_app = self.nav.pre_call_tasks()
        component = dlg_app.child_window(title="Configure User Settings", control_type="Text")
        the_component = component.parent()
        return the_component


# using windows specification.criteria [
#     {'title': 'GrowthDirect2', 'top_level_only': True, 'backend': 'uia', 'app': <pywinauto.application.Application object at 0x0320EE68>},
#     {'best_match': 'Approve TestsButton', 'control_type': 'Button', 'top_level_only': False}]

# got a  <class 'pywinauto.findbestmatch.MatchError'>
# will now print the available control identifiers...


#    |
#    | GroupBox - 'Menu Options'    (L335, T98, R1585, B765)
#    | ['GroupBox', 'Menu OptionsGroupBox', 'Menu Options', 'Menu Options0', 'Menu Options1']
#    | child_window(title="Menu Options", control_type="Group")
#    |    |
#    |    |
#    |    | Custom - ''    (L518, T516, R694, B638)
#    |    | ['Custom19', 'Create and Modify SamplesCustom', 'Approve TestsCustom']
#    |    | child_window(auto_id="menuButton", control_type="Custom")
#    |    |    |
#    |    |    | Button - ''    (L522, T516, R694, B632)
#    |    |    | ['Approve TestsButton', 'Button30']
#    |    |    |    |
#    |    |    |    | Static - 'Approve Tests'    (L527, T523, R617, B542)
#    |    |    |    | ['Approve Tests', 'Approve TestsStatic', 'Static44']
#    |    |    |    | child_window(title="Approve Tests", control_type="Text")
#    |    |    |    |
#    |    |    |    | Image - ''    (L528, T555, R578, B605)
#    |    |    |    | ['Image12', 'Approve TestsImage']
#    |    |    |    |
#    |    |    |    | Static - 'Select Tests to Approve'    (L586, T551, R689, B588)
#    |    |    |    | ['Select Tests to ApproveStatic', 'Select Tests to Approve', 'Static45']
#    |    |    |    | child_window(title="Select Tests to Approve", control_type="Text")