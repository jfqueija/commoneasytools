#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

import json

class DictionaryReader(object):
    """
        This class provide a helper for convert json to dictionary and access to keys with attributes
    """
    def __init__(self, keys_dic = None, config_file = ()):
        """
            Class constructor
            :param keys_dic: dict. Dictionary with keys to search
            :param config_file: dict. Tuple with information. It´s required
        """
        self.__config_file = config_file
        if keys_dic == None:
            self.__keys = ()
        else:
            self.__keys = keys_dic
        self.__result = None

    def __getattr__(self,attribute):
        """
            Private method used for get attribute from class and create final endpoint.
            :param attribute: str. Parameter name
        """
        result = None
        try:            
            result = DictionaryReader(keys_dic=self.__keys + (attribute,),config_file=self.__config_file)
        except Exception as ex:
            pass
        return result

    def get(self,value_dict=None):
        """
            Public method for get value of dictionary
            :param value_dict: dict.
        """        
        try:
            if value_dict == None:
                dictionary_search = self.__config_file
            else:
                dictionary_search = value_dict
            for k in self.__keys:
                value = dictionary_search.get(k)
                if not value == None:
                    if isinstance(value,dict):
                        self.get(value_dict=value)
                    else:
                        if self.__result == None:
                            self.__result = value                       
        except Exception as ex:
            pass
        return self.__result