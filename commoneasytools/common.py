#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

from os import name
from copy import deepcopy

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

    def remove_property(self,target: dict,prop:[]) -> dict:
        """
            Method used for remove properties from a dictionary
            :param target: dict. Dictionary over that we can do changes
            :para prop: []. Properties of dictionary that we will remove inside.
        """        
        try:
            for p in prop:
                del target[p]
        except Exception:
            pass
        return target

    def object_to_dictionary(self,model:object)->dict:
        """
            Method used for convert model into dictionary
            :param model: object. Object over that we can do conversion to dictionary. Previously we do an copy and convert this copy.
        """ 
        result:dict = dict()       
        try:
            bck_model = deepcopy(model)
            result = bck_model.__dict__
        except Exception:
            pass
        return result