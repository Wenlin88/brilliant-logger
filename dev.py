from easylogging import loggerClass

logger = loggerClass(name = 'Test logger', file_logging = True, logging_level = 'debug', file_logging_level = 'debug')
debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
critical = logger.critical
exception = logger.exception

debug('Info')