#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

from enum import Enum

class LoggerMinumLevel (Enum):
    """
        Minimun accepted logger level
    """
    CRITICAL=0
    DEBUG=1
    ERROR=2
    FATAL=3
    INFO=4
    WARNING=5