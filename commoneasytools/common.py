#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

from os import name

class Common(object):
    """
        Class with common methods/functions
    """ 
    def __init__(self):
        """
            Basic constructor
        """
        pass

    def get_slash(self):
        """
            Reference of S.O. returned values '\\' - Windows or '/' - Linux
        """
        if name == 'nt':
            return '\\'
        else:
            return '/'
        
    def doExtraLogger(self,appName:str,methodName:str,className:str,inheritedFrom:str,*args, **kwargs):
        """
            Public method used for construct dictionary with extra information for send to logger.
            :param appName: string
            :param methodName: string
            :param className: string
            :param inheritedFrom: string
            :param args: extra data
            :param kwargs: extra dictionary
        """
        extra = dict()
        extra["AppName"] = appName
        extra["Class"] = className
        extra["Method"] = methodName
        extra["inheritedFrom"] = inheritedFrom
        if kwargs:
            extra.update(kwargs['kwargs'])
        return extra