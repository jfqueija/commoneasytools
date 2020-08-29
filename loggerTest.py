#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

import unittest
import os

from common.logger import Log
from common.loggerLevel import LoggerMinumLevel as level

class TestLogger(unittest.TestCase):
    
    def logger_ok(self):        
        with self.assertLogs('Test',level='DEBUG') as cm:
            localpath = '%s/%s'%(os.path.dirname(__file__),'Log')
            lg = Log(loggerPath=localpath,loggerFileName='Test',minimunLevel=level.DEBUG).get()
            lg.info('Test write logger')
        self.assertEqual('DEBUG:Test:Test write logger',cm.output)

def logger_ok():
    localpath = '%s/%s'%(os.path.dirname(__file__),'Log')
    lg = Log(loggerPath=localpath,loggerFileName='Test',minimunLevel=level.DEBUG).get()
    lg.info('Test write logger')

if __name__ == '__main__':
    unittest.main()
    #logger_ok()