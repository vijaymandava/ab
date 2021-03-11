import logging

# reference https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook

# example:
# from common_testbench import common_logging
# logger = common_logging.get_logger('launch_sequencer')
# def my_function():
#     logger.info('hello from launch sequencer')
# end example


def get_logger(log_name='common'):
    # create logger for 'lims_customer_tofrom_cm'
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = logging.FileHandler('log_' + log_name + '.log')
    fh.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    # ch.setLevel(logging.ERROR)
    ch.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    #logger.addHandler(ch)

    return logger
