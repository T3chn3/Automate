import json
#reading
stringOfJsonData = '{"name": "Bob", "isCat": true, "miceCaught": 0, "felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

#alt print
print("\n")
print("Again with Dumps() \n")
print(json.dumps(jsonDataAsPythonValue))

#writing


#formatting