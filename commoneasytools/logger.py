#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

import logging
import os
import sys
from datetime import datetime
from commoneasytools.loggerLevel import LoggerMinumLevel

class Log(object):
    """
        Class for merge logger options
    """ 
    def __init__(self):
        """
            Basic constructor
        """
        self.__logger = None
        

    def settingToFile(self,loggerPath:str, loggerFileName:str, minimunLevel: LoggerMinumLevel):
        """
            Method for setting logger configuration and save messages in file.
        """
        try:
            if not os.path.isdir(loggerPath):
                    os.mkdir(loggerPath)                        
            logging.basicConfig(filename='%s/%s_%s.log'%(loggerPath,loggerFileName, datetime.today().strftime('%Y%m%d')),        
                filemode='a',format='%(asctime)s - [%(levelname)s] -  %(message)s',
                datefmt='%Y/%m/%d %H:%M:%S',
                level=self.__getlevel(minimunLevel.value))                       
            logging.getLogger('python')
            logger = logging.getLogger('python')
            logger.setLevel(self.__getlevel(minimunLevel.value))   
            self.__logger = logger
        except Exception:
            self.__logger = None            
        return self.__logger

    def settingToLogstash(self, host:str, port:int, minimunLevel: LoggerMinumLevel):
        """
            Method for setting logger configuration using logstash.
            @host: Ip or Name of Logstash server.
            @port: Logstash Listen Port. Normally is 5959. Review you logstash configuration.
            We can add extra information when send message using dictionaries. Sample:
                extraFields = {'Field1': value1, 'Field2': value2}
                logger.info(msg='Message',extra=extraFields)
        """
        import logstash
        try:                                             
            logger = logging.getLogger('python-logstash')
            logger.setLevel(self.__getlevel(minimunLevel.value))  
            logger.addHandler(logstash.LogstashHandler(host, port, version=1))                         
            self.__logger = logger
        except Exception:
            self.__logger = None
        return self.__logger

    def __getlevel(self,level):
        """
            Private method for select level request by parameter
        """
        levelSelected = None
        if level == LoggerMinumLevel.CRITICAL.value:
            levelSelected = logging.CRITICAL
        elif level == LoggerMinumLevel.DEBUG.value:
            levelSelected = logging.DEBUG
        elif level == LoggerMinumLevel.ERROR.value:
            levelSelected = logging.ERROR
        elif level == LoggerMinumLevel.FATAL.value:
            levelSelected = logging.FATAL
        elif level == LoggerMinumLevel.INFO.value:
            levelSelected = logging.INFO
        elif level == LoggerMinumLevel.WARNING.value:
            levelSelected = logging.WARNING
        else:
            levelSelected = logging.DEBUG
        return levelSelected