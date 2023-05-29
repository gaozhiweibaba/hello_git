import requests
import json


def add_game_count(count):
    data = {
        "user_id": 8411888467957,
        "award_config_id": 2601,
        "campaign_name": "定投3.0抽奖机会",
        "campaign_number": "AC1685067613649rzXkWt"
    }
    headers = {
        'User-Agent': 'PostmanRuntime/7.32.2',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain',
        'Cookie': 'ngxid=rB4xTGRtgb1u7F2FBuewAg=='

    }
    url = 'https://test-marketing.tigerfintech.com/campaign/admin/api/v1/test/global_reward'
    for i in range(count):
        reqs = requests.post(url, json.dumps(data), json.dumps(headers))

    return '完成'


if __name__ == '__main__':
    print(add_game_count(10))



