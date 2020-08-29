#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

import json.scanner
from commoneasytools.resultOperation import ResultOperationEntity
from commoneasytools.resultType import ResultOperationType

class ResultData(object):
    """
        Complex model for returned data structured.
    """
    def __init__(self):
        self.__content = None
        self.__hasErrors = False
        self.__resultOperationEntities = []

    @property
    def Content(self):
        return self.__content

    @Content.setter
    def Content(self, value):
        self.__content = value

    @property
    def HasErrors(self):
        return self.__hasErrors
    
    @property
    def ResultOperationEntities(self):
        return self.__resultOperationEntities
    
    def AddResult(self, message: str, resultType: ResultOperationType):      
        """
            Method used for add an result to structure.
            message: field with message to add.
            resultType: one of class enums ResultOperationType            
        """
        try:   
            self.__resultOperationEntities.append(ResultOperationEntity(message,resultType))           
            if resultType == ResultOperationType.ERROR or resultType == ResultOperationType.EXCEPTION:
                self.__hasErrors = True
        except Exception as ex:
            raise ValueError('Exception %s in method business.ResultData.AddResult '%str(ex))
    
    def AddResultRange(self, resultRange: list):
        """
            Method used for add one Complex Result to list of results.
        """
        for res in resultRange:
            self.AddResult(res.Message,res.ResultType)
    
    def FormatResultOperationEntities(self):
        """
            Method used for return result structure formatting to text
        """
        message = ""
        for res in self.__resultOperationEntities:
            message = '%s %s - %s,'%(message,res.ResultType.name,res.Message)
        return message    

    