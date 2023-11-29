import json
user= '{"name":"juan","age":26,"city":"panama"}'
data= json.loads(user)
print(data)
newjson= json.dumps(data,indent=2)
with open('juan.json','r') as file:
	data=json.load(file)
	print(data["name"])
	