dic = {'key1': ["value1",  "value2"],
       'key2': ["value77", "something"] }

if "value77" in [x for v in dic.values() for x in v]:
    print(dic)