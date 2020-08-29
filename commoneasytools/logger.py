#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

import logging
import os
import sys
from datetime import datetime
from enum import Enum
from commoneasytools.loggerLevel import LoggerMinumLevel

class Log(object):
    """
        Class for unificate logger options
    """ 
    def __init__(self, loggerPath:str, loggerFileName:str, minimunLevel: LoggerMinumLevel):
        """
            Basic constructor
        """
        if not os.path.isdir(loggerPath):
                os.mkdir(loggerPath)

        if minimunLevel == LoggerMinumLevel.CRITICAL:
            level = logging.CRITICAL
        elif minimunLevel == LoggerMinumLevel.DEBUG:
            level = logging.DEBUG
        elif minimunLevel == LoggerMinumLevel.ERROR:
            level = logging.ERROR
        elif minimunLevel == LoggerMinumLevel.FATAL:
            level == logging.FATAL
        elif minimunLevel == LoggerMinumLevel.INFO:
            level == logging.INFO
        elif minimunLevel == LoggerMinumLevel.WARNING:
            level == logging.WARNING

        logging.basicConfig(filename='%s/%s_%s.log'%(loggerPath,loggerFileName, datetime.today().strftime('%Y%m%d')),        
            filemode='a',format='%(asctime)s - [%(levelname)s] -  %(message)s',
            datefmt='%Y/%m/%d %H:%M:%S',
            level=level)                       
        logging.getLogger('python')
        logger = logging.getLogger('python')
        logger.setLevel(level)   
        self.__logger = logger

    def get(self):
        return self.__logger  

