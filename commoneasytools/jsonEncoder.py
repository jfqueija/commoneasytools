#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

import json
import inspect

class ObjectEncoder(json.JSONEncoder):
    """
        Class used for convert to json or to dict one object with properties.
        How to use:
            from common.jsonEncoder import ObjectEncoder as obEncoder
            json.dumps(result,cls=obEncoder,sort_keys=True)
        Note: Result is an object.
        For use with SQLAlchemy, added filter key not equals to metadata.
    """
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__") and not key.startswith("_") and not key == "metadata"
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
            )
            return self.default(d)
        return obj