
class Privs():

    def __init__(self):

        self.item = {}

        self.item['first']uuid.uuid4().hex.upper()[0:comment_max_len]
        self.item['middle']
        self.item['last']
        self.item['username']
        self.item['email']
        self.item['password']
        self.item['telephone']
        self.item['ext']
        self.item['user_role']

        self.item['meth_create_meth'] = True
        self.item['meth_edit_meth'] = True
        self.item['meth_delete_meth'] = True
        self.item['aa_create'] = True
        self.item['aa_edit'] = True
        self.item['aa_delete'] = True
        self.item['hr_create'] = True
        self.item['hr_edit'] = True
        self.item['hr_delete'] = True
        self.item['sample_create'] = True
        self.item['sample_edit'] = True
        self.item['sample_delete'] = True
        self.item['worklist_create'] = True
        self.item['worklist_edit'] = True
        self.item['worklist_delete'] = True
        self.item['users_create'] = True
        self.item['users_modify'] = True
        self.item['users_endis'] = True
        self.item['roles_create'] = True
        self.item['roles_modify'] = True
        self.item['roles_delete'] = True
        self.item['test_n_label_order'] = True
        self.item['test_n_label_load'] = True
        self.item['test_n_label_print_wl'] = True
        self.item['cassette_cancel'] = True
        self.item['cassette_retrieve'] = True
        self.item['cassette_approve'] = True
        self.item['cassette_cleanup'] = True
        self.item['lims_edit_settings'] = True
        self.item['lims_print'] = True
        self.item['lims_modify'] = True
        self.item['lims_edit_results'] = True
        self.item['system_ack_alarms'] = True
        self.item['system_ack_sys_errors'] = True
        self.item['system_ack_service_issues'] = True
        self.item['system_empty_trash'] = True
        self.item['system_administer'] = True
        self.item['system_edit_gen_settings'] = True
        self.item['system_edit_it_settings'] = True
        self.item['system_maintenance'] = True
        self.item['system_service'] = False
        self.item['system_send_logs'] = True
