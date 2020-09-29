# CommonEasyTools


#   How to Use

##  __Logger__

We can integrated in our projects, using this import:

```py
from commoneasytools.logger import Log
from commoneasytools.loggerLevel import LoggerMinumLevel as level
```

### __Setting to file__

*   We need import two libraries. First contain initialize of logger. Second contains an enum with minum level for declare when we call to constructor.

For use it, we can look this sample:

```py
localpath = '%s/%s'%(os.path.dirname(__file__),'Log')
lg = Log().settingToFile(loggerPath=localpath,loggerFileName='Test',minimunLevel=level.DEBUG)
lg.info('Test Dummy') 
```

*   First we initialize the constructor. We send Path target of log, name of log, minimun level and we call method get for recovery logger properties.
*   Second we can use properties of logger for write logs.

### __Setting to logstash__


For use it, we can look this sample:

```py
import sys

hostLogstash = '127.0.0.1'
portLogstash = 5959
lg = Log().settingToLogstash(host=hostLogstash,port=portLogstash,minimunLevel=level.DEBUG)
extraData = {
    'Field1': 'python version: ' + repr(sys.version_info),
    'FieldCustom2': True,
    'FieldCustom3': {'a': 1, 'b': 'c'}
}
lg.info(msg='Test Dummy',extra=extraData) 
```

>   Remember, For use this configuration you need have correctly configurated logstash.

```
logstash.conf


input {
  udp {
    port => <listenPort. It's same that you send in request parameters>
    codec => json
  }
}
```

####  __doExtraLogger__

This method was implemented for provide a easy system for create a extra logger information.
When we declare logger with logstash configuration, we can use this method. 

__Example use:__

```py
from commoneasytools.common import Common as cm
cm().doExtraLogger(appName='App Dummy',methodName='Method Dummy',className='Class Dummy',inheritedFrom='Principal App Name')
```

If you need add more information, you can look this other example:

```py
from commoneasytools.common import Common as cm
cm().doExtraLogger(appName='App Dummy',methodName='Method Dummy',className='Class Dummy',inheritedFrom='Principal App Name',kwargs={'Result':'Result Value Dummy'})
```

> In kwargs you can add additional information. Remember, kwargs is a dictionary.

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

##  __DictionaryReader__

This class is used for provide an easy system to reader a dictionary using attributes.

__Use Example:__

> From dict

```py
from commoneasytools.dictionary import DictionaryReader

dict_dummy = {
    "Entry_1":"Dummy data",
    "Entry_2" : {
        "Sub_Entry_2_1":"Dummy data sub entry",
        "Sub_Entry_2_2":{
          "Sub_Entry_2_2_1":"Dummy data sub entry 2 1",
        }        
    }
}

d = DictionaryReader(config_file=dict_dummy)
value_entry1 = d.Entry_1.get()
value_entry2 = d.Entry_2.Sub_Entry_2_2.Sub_Entry_2_2_1.get()
print(value_entry1)
print(value_entry2)
```

> From file
```py
import json
from commoneasytools.dictionary import DictionaryReader

path = '%s/%s'%(os.path.dirname(__file__),'file.json')
with open(path, encoding='utf-8') as json_file:                
    config_file = json.load(json_file)  

d = DictionaryReader(config_file=config_file)
value_entry1 = d.Entry_1.get()
value_entry2 = d.Entry_2.Sub_Entry_2_2.Sub_Entry_2_2_1.get()
print(value_entry1)
print(value_entry2)
```