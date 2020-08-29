#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

import os

from commoneasytools.logger import Log
from commoneasytools.loggerLevel import LoggerMinumLevel as level

def logger_ok():
    localpath = '%s/%s'%(os.path.dirname(__file__),'Log')
    lg = Log(loggerPath=localpath,loggerFileName='Test',minimunLevel=level.DEBUG).get()
    lg.info('Test write logger')

if __name__ == '__main__':
    logger_ok()