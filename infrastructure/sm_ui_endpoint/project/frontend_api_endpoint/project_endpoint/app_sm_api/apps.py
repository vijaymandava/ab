import logging
from django.apps import AppConfig


class AppSmApiConfig(AppConfig):
    name = 'app_sm_api'

    def ready(self):

        logger = logging.getLogger(__name__)
        logger.debug("-- starting backend ----")

        from navigation import Navigation
        self.nav = Navigation()
        self.nav.start()
        self.nav.setup_controls_and_dialogs()

        logger.debug("-- backend is started ----")

        # reference https://stackoverflow.com/questions/54055815/where-in-django-can-i-run-startup-code-that-requires-models

        # you can obtain the appconfig for a given app with from 
        #django.apps import apps
        #apps.get_app_config('app_name'). 
        #
        #If you store your resorce that is loaded on the self (so 
        #self.to_load = ...), 
        #you thus can access it with 
        #apps.get_app_config('app_name').to_load. 
        #
        #But you should do that in a function, since the models are 
        #loaded before the ready function is triggered. –

