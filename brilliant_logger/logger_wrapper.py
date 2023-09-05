import logging
import sys
from unittest.mock import patch

class loggerWrapper():
    LOG_LEVELS = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self, name='root', logging_level='info', file_logging=False, file_logging_level='debug'):
        self.name = name
        self.logger = logging.getLogger(name)

        logging_level = self.LOG_LEVELS.get(logging_level.lower())
        if logging_level is None:
            raise ValueError("Unsupported logging level: {}. Use one of: {}".format(logging_level, ', '.join(self.LOG_LEVELS.keys())))

        file_logging_level = self.LOG_LEVELS.get(file_logging_level.lower())
        if file_logging_level is None:
            raise ValueError("Unsupported file logging level: {}. Use one of: {}".format(file_logging_level, ', '.join(self.LOG_LEVELS.keys())))

        if not self.logger.handlers:
            ch = logging.StreamHandler()
            ch.setLevel(logging_level)
            formatter = logging.Formatter('[{levelname:^17} : {name:^17}]: {message}', style='{')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

        if file_logging and not any(isinstance(handler, logging.FileHandler) for handler in self.logger.handlers):
            fh = logging.FileHandler(name + '.log')
            fh.setLevel(file_logging_level)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        # Set logger logging level with lowest level of all handlers
        logging_level = min(logging_level, file_logging_level)
        self.logger.setLevel(logging_level)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def exception(self, msg):
        self.logger.exception(msg)

    def get_all_funcs(self):
        return self.debug, self.info, self.warning, self.error, self.critical, self.exception
    
    def shutdown(self):
        handlers = self.logger.handlers[:]
        for handler in handlers:
            handler.close()
            self.logger.removeHandler(handler)
    
    def log_functions(self):
        return self.debug, self.info, self.warning, self.error, self.critical, self.exception

