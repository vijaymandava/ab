import urllib3


class CommonSettingForFeBeTests(object):

    def __init__(self):

        self.timeout = 240
        self.url = 'http://127.0.0.1:9100/sm_ui/'
        self.http = urllib3.PoolManager()
