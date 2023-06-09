import requests


data = {
    "user_id": 74118865397,
    "award_config_id": 2601,
    "campaign_name": "定投3.0抽奖机会",
    "campaign_number": "AC1685067613649rzXkWt"
}


headers = {
    'Postman-Token': '<calculated when request is sent>',
    'Content-Length': '<calculated when request is sent>',
    'Host': '<calculated when request is sent>',
    'User-Agent': 'PostmanRuntime/7.32.2',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain',
    'Cookie': 'ngxid=rB4xTGRtgb1u7F2FBuewAg=='

}

url = 'https://test-marketing.tigerfintech.com/campaign/admin/api/v1/test/global_reward'
reqs = requests.post(url, data, headers)


print(reqs.text)
