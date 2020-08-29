#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

from enum import Enum

class ResultOperationType (Enum):
    """
        Enum with diferents types of result operations.
    """    
    ERROR = 0
    INFO = 1
    WARNING = 2
    SUCCESS = 3
    EXCEPTION = 4