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