import json

file = "/Users/gaozhiwei/Desktop/tweet.txt"


with open(file, "r", encoding='utf-8') as f:
    dict_data = json.loads(f.read())


sort_data = dict_data['data']['list']

card_list = []

for i in sort_data:
    for k in i['cardData']:
        card_list.append(k)


card_list.sort(key=lambda x:x['likeCount'])





