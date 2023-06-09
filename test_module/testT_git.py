import json

with open(file="/Users/gaozhiwei/Desktop/a.txt", mode='r', encoding='utf-8') as f:
    data = f.read()

data = json.loads(data)
a = 0
for i in data['data']:
    print(a)
    print(i['customerId'])
    a+=1
print("hello")