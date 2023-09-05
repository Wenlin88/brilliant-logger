# %% test_logger_wrapper.py

import unittest
from unittest.mock import patch
import os
from logger_wrapper import loggerWrapper

class TestLoggerWrapper(unittest.TestCase):
    
    def setUp(self):
        self.logger = loggerWrapper(name='test', file_logging=True, logging_level='info', file_logging_level='debug')
        self.logfile = 'test.log'

    def test_debug(self):
        self.assertIsNotNone(self.logger.debug)
    
    def test_info(self):
        self.assertIsNotNone(self.logger.info)
        
    def test_warning(self):
        self.assertIsNotNone(self.logger.warning)

    def test_error(self):
        self.assertIsNotNone(self.logger.error)

    def test_critical(self):
        self.assertIsNotNone(self.logger.critical)

    def test_exception(self):
        self.assertIsNotNone(self.logger.exception)

    def test_get_all_funcs(self):
        debug, info, warning, error, critical, exception = self.logger.get_all_funcs()
        self.assertIsNotNone(debug)
        self.assertIsNotNone(info)
        self.assertIsNotNone(warning)
        self.assertIsNotNone(error)
        self.assertIsNotNone(critical)
        self.assertIsNotNone(exception)

    def test_debug_file_output(self):
        self.logger.debug('This is a debug message')
        with open(self.logfile, 'r') as f:
            log_contents = f.read()
        assert 'This is a debug message' in log_contents

    def tearDown(self):
        self.logger.shutdown()
        # Clean up the log file after each test
        if os.path.exists(self.logfile):
            os.remove(self.logfile)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoggerWrapper)
    unittest.TextTestRunner().run(suite)
# %%
