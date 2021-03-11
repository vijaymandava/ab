import sys

class DialogBase(object):

    name = None
    #app = None
    nav = None

    def __init__(self, name, nav): # app):
        print('constructing dialog {}'.format(name))
        self.name = name
        #self.app = app
        self.nav = nav

    # def sanity_check(self, window_spec):
    #     try:
    #         #verify it can be resolved
    #         window_spec.wrapper_object()
    #     except Exception as e:
    #         print('Oops! when trying to access a control on the "{}" page...'.format(self.name))
    #         print('using windows specification.criteria {}'.format(window_spec.criteria))
    #         print('got a ', e.__class__)
    #         print('will now print the available control identifiers...')
    #         self.app.print_control_identifiers()
    #         sys.exit()