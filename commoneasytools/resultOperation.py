#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

class ResultOperationEntity(object):
        """
            Secondary class used in ResultData. Provided sub structure with information about operation
        """
        def __init__(self, message, resultType):
            self.__message = message
            self.__resultType = resultType
        
        @property
        def Message(self):
            return self.__message

        @property
        def ResultType(self):
            return self.__resultType