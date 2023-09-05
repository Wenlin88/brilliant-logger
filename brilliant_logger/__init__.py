import logging
import sys

from .logger_wrapper import loggerWrapper

def get_logger(name='root', logging_level='info', file_logging=False, file_logging_level='debug'):
    return loggerWrapper(name, logging_level, file_logging, file_logging_level)
