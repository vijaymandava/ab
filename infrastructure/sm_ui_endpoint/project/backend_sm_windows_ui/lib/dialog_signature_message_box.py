from dialog__base import DialogBase

class DialogSignatureMessageBox(DialogBase):

    # add windows spec, given parent's window spec (pws)
    def set_controls(self, pws):

        self.window_spec['username'] = pws.window(best_match='User:Edit', control_type='Edit')
        self.window_spec['password'] = pws.window(best_match='Password:Edit', control_type='Edit')
        self.window_spec['ok'] = pws.window(best_match='OK', control_type='Button')
        self.window_spec['cancel'] = pws.window(best_match='Cancel', control_type='Button')
