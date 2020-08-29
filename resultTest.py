#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='pepekiko@gmail.com'

import json

from commoneasytools.resultData import ResultData as res
from commoneasytools.resultType import ResultOperationType as resType
from commoneasytools.jsonEncoder import ObjectEncoder as obsEncoder

def main():
    try:
        response = res()
        model = {'User':'UserDummy', 'Name':'Jhon', 'Surname':'Doe'}
        response.Content = model
        response.AddResult(message='Successfully operation',resultType=resType.SUCCESS)
        print(json.dumps(response,cls=obsEncoder,sort_keys=True))
    except Exception as ex:
        print(ex)

if __name__ == '__main__':
    main()
