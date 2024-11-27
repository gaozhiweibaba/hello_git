import requests
import time
import json


def get_market_value(task_id: str):
    current_timestamp = int(time.time() * 1000)
    url = 'https://noldor-test.qa.tigerbrokers.net/api/polaris/v1/transfer_task/' + task_id
    params = {
        'CRM_License': 'TBNZ',
        '_s': str(current_timestamp)
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'authorization': 'Basic 34JeXSoVfvgoSSqPsmSZtjSQuhAz0v',
        'origin': 'https://crm-dev.tigerbrokers.net',
        'priority': 'u=1, i',
        'referer': 'https://crm-dev.tigerbrokers.net/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    data = requests.get(url=url, params=params, headers=headers)
    return json.loads(data.text)["data"]['marketValue']


def get_allocated_value(page_size: int, allocated_at: list, belong_crm_name: str):
    current_timestamp = int(time.time() * 1000)
    url = 'https://noldor-test.qa.tigerbrokers.net/api/polaris/v1/transfer_task/list'
    params = {
        'CRM_License': 'TBNZ',
        '_s': str(current_timestamp)
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'authorization': 'Basic 34JeXSoVfvgoSSqPsmSZtjSQuhAz0v',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://crm-dev.tigerbrokers.net',
        'priority': 'u=1, i',
        'referer': 'https://crm-dev.tigerbrokers.net/',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }

    data = {
        'pageNumber': 1,
        'pageSize': page_size,
        'belongCrm': "83499517",
        'allocatedAt': allocated_at,
        'belongCrmName': belong_crm_name
    }

    reqs = requests.post(url=url, params=params, headers=headers, data=json.dumps(data))
    return json.loads(reqs.text)["data"]['list']


def count_allocated_value():
    content = get_allocated_value(page_size=200, allocated_at=[1730390400000, 1732982399999], belong_crm_name='高志伟(gaozhiwei)')
    count = 0
    us_mary = 0
    hk_mary = 0
    sg_mary = 0
    au_mary = 0
    for i in content:
        count += 1
        if i["market"] == "US":
            us_count = get_market_value(str(i["id"]))
            us_mary += us_count
        elif i["market"] == "HK":
            hk_count = get_market_value(str(i["id"]))
            hk_mary += hk_count * 0.1282
        elif i["market"] == "SG":
            sg_count = get_market_value(str(i["id"]))
            sg_mary += sg_count * 0.7435
        elif i["market"] == "AU":
            au_count = get_market_value(str(i["id"]))
            au_mary += au_count * 0.6541
    total_mary = us_mary + hk_mary + sg_mary + au_mary
    print("分配任务数：", count)
    print("分配任务市值（US）：", us_mary)
    print("分配任务市值（HK）：", hk_mary)
    print("分配任务市值（SG）：", sg_mary)
    print("分配任务市值（AU）：", au_mary)
    print("总计-市值：", total_mary)


if __name__ == '__main__':
    count_allocated_value()

