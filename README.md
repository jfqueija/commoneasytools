# CommonEasyTools


#   How to Use

##  __Logger__

We can integrated in our projects, using this import:

```py
from commoneasytools.logger import Log
from commoneasytools.loggerLevel import LoggerMinumLevel as level
```

*   We need import two libraries. First contain initialize of logger. Second contains an enum with minum level for declare when we call to constructor.

For use it, we can look this sample:

```py
lg = Log(loggerPath='%s/%s'%(os.path.abspath(__file__ + "/../../"),'FolderName'),loggerFileName='LoggerFileName',minimunLevel=level.DEBUG).get()  
lg.info('Test Dummy') 
```

*   First we initialize the constructor. We send Path target of log, name of log, minimun level and we call method get for recovery logger properties.
*   Second we can use properties of logger for write logs.

##  __ResultData__

This class provide an structure for encapsulate dynamics models put in Content Property. We can add results with menssage and result type. When select a Error result type, the property HasErrors take true value. 

For use this library, we folow next instructions:

```py
from commoneasytools.resultData import ResultData as res
from commoneasytools.resultType import ResultOperationType as resType
```

Sample Use:

```py
response = res()
model = {'User':'UserDummy', 'Name':'Jhon', 'Surname':'Doe'}
response.Content = model
response.AddResult(message='Successfully operation',resultType=resType.SUCCESS)
```

##  __JsonEncoder__

This library provide an output conversion of a complex class formatting to json. For use, we need to import next library:

```py
import json
from commoneasytools.jsonEncoder import ObjectEncoder as obsEncoder
```

Sample Use:

```py
print(json.dumps(response,cls=obsEncoder,sort_keys=True))
```

Sample output:
```json
{"Content": {"Name": "Jhon", "Surname": "Doe", "User": "UserDummy"}, "HasErrors": false, "ResultOperationEntities": [{"Message": "Successfully operation", "ResultType": {"name": "SUCCESS", "value": 3}}]}
```