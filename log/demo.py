""""introduce how to use logging module; the logging module contain of
logger, handler, filter and formatter
"""
#import logging module
import logging
#create logger; use this api to create logger for single pattern, get the
#same logger in different python module
LOG = logging.getLogger("log")

#log level contains of debug, info, warning, error, critical
#this log level map different logger api
#for example: logger.debug(), logger.info(), logger.warning(), logger.\
#error(), logger.critical()

#config log level for logger
LOG.setLevel(logging.DEBUG)

logfile = logging.FileHandler('./log.txt')
logfile.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s-[%(name)s]-%(levelname)s-%(message)s')
logfile.setFormatter(formatter)

LOG.addHandler(logfile)
LOG.debug("hello world") 



