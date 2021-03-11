class Privs(object):

    priv = [
        "a",
        "b",
        "c"]

    pywin_name = {}
    control_type = {}
    bestmatch_user_role = {}
    bestmatch_users = {}

    def set(self, friendly_name, pywin_name, control_type):
        self.pywin_name[friendly_name] = pywin_name
        self.control_type[friendly_name] = control_type

    def __init__(self):

        self.set('methods_create', 'MethodsButton2', 'Button')
        self.set('methods_edit',   'MethodsButton3', 'Button')
        self.set('methods_delete', 'MethodsButton4', 'Button')
        self.set('aa_create',      'Action/AlertButton1', 'Button')
        self.set('aa_edit',        'Action/AlertButton2', 'Button')
        self.set('aa_delete',      'Action/AlertButton3', 'Button')
        self.set('hr_create',      'Handling RulesButton1', 'Button')
        self.set('hr_edit',        'Handling RulesButton2', 'Button')
        self.set('hr_delete',      'Handling RulesButton3', 'Button')
        self.set('samples_create', 'SamplesButton1', 'Button')
        self.set('samples_edit',   'SamplesButton2', 'Button')
        self.set('samples_delete', 'SamplesButton3', 'Button')
        self.set('wl_create',  'WorklistsButton1', 'Button')
        self.set('wl_edit',    'WorklistsButton2', 'Button')
        self.set('wl_delete',  'WorklistsButton3', 'Button')
        self.set('cassette_ops_cancel',   'Cassette OperationsButton1', 'Button')
        self.set('cassette_ops_retrieve', 'Cassette OperationsButton2', 'Button')
        self.set('cassette_ops_approve',  'Cassette OperationsButton3', 'Button')
        self.set('cassette_ops_cleanup',  'Cassette OperationsButton4', 'Button')
        self.set('lims_edit_settings', 'LIMSButton1', 'Button')
        self.set('lims_print',         'LIMSButton2', 'Button')
        self.set('lims_modify',        'LIMSButton3', 'Button')
        self.set('lims_edit_results',  'LIMSButton4', 'Button')
        self.set('sys_ack_alarms',         'UsersButton1', 'Button')
        self.set('sys_ack_sys_errs',       'UsersButton2', 'Button')
        self.set('sys_ack_service_issues', 'UsersButton3', 'Button')
        self.set('sys_empty_trash',       'Users RolesButton1', 'Button')
        self.set('sys_administer_system', 'Users RolesButton2', 'Button')
        self.set('sys_edit_gen_settings', 'Users RolesButton3', 'Button')
        self.set('tests_and_labels_order_tests',           'Tests & LabelsButton1', 'Button')
        self.set('tests_and_labels_load_test',             'Tests & LabelsButton2', 'Button')
        self.set('tests_and_labels_print_worklist_labels', 'Tests & LabelsButton3', 'Button')

        self.set('sys_ack_alarms',                 'SystemButton1', 'Button')
        self.set('sys_ack_system_errors',          'SystemButton2', 'Button')
        self.set('sys_ack_service_service_issues', 'SystemButton3', 'Button')
        self.set('sys_empty_trash',                'SystemButton4', 'Button')
        self.set('sys_administer_system',          'SystemButton5', 'Button')
        self.set('sys_edit_general_settings',      'SystemButton6', 'Button')
        self.set('sys_edit_it_settings',           'SystemButton7', 'Button')
        self.set('sys_edit_maintenance',           'SystemButton8', 'Button')
        self.set('sys_service',           'Tests & LabelsButton4', 'Button')
        self.set('sys_send_system_logs',  'Tests & LabelsButton5', 'Button')


