import logging


def log_this(name=None, str2=None, str3=None, str4=None, str5=None  ):
    if name is None:
        name = ''
    if str2 is None:
        str2 = ''
    if str3 is None:
        str3 = ''
    if str4 is None:
        str4 = ''
    if str5 is None:
        str5 = ''

    logger = logging.getLogger(name)
    logger.debug('---- {} {} {} {} {}'.format(name, str2, str3, str4, str5))
