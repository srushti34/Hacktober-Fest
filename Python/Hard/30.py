import json
json_data = '{"name": "John", "age": 30, "active": true}'
data = json.loads(json_data)
if data['active'] == "true":
 print(f"{data['name']} is active.")
