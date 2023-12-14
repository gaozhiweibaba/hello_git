import requests
import json
import time


def get_list():
    url = "https://ms-nd-qa.qa.tigerbrokers.net/stream/internal/message/admin/v2/post/search"
    params = {
        "_s": 1701152788809,
        "license": "BAAS",
        "lang": "en_US",
        "pageSize": 100,
        "deliveryType": "SMS_TEXT",
        "beginTimestamp": "1699632000000",
        "endTimestamp": "1701187199999",
        "pageNumber": 1
    }
    data = requests.get(url=url, params=params)
    print(data.text)
    return data.text


def post_sms():
    url = "https://ms-nd-qa.qa.tigerbrokers.net/stream/internal/message/sms/post"
    headers = {
        "Cookie": "ngxid=rB4xTGVlnt2rPW7TchXhAg==; path=/",
        "Cache-Control": "no-cache",
        "Postman-Token": "<calculated when request is sent>",
        "Content-Type": "text/plain",
        "Content-Length": "<calculated when request is sent>",
        "Host": "<calculated when request is sent>",
        "User-Agent": "PostmanRuntime/7.35.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    data = {
        "accountIdList": [
            "52836465"
        ],
        "platform": "crm",
        "secret": "xuPDDHjeYsBbKnH6",
        "channel": "backend",
        "templateId": "1176863886123",
        "templateArgs": {},
        "templateType": "individual",
        "lang": "zh_CN",
        "targetType": "SMS_TEXT",
        "license": "TBNZ"
}
    for i in range(2):
        reqs = requests.post(url, json.dumps(data), json.dumps(headers))
        print(reqs.text)
        time.sleep(1)


def post_mail():
    url = "https://ms-nd-qa.qa.tigerbrokers.net/stream/internal/message/email/post"
    headers = {
        "Cookie": "ngxid=rB4xTGVlnt2rPW7TchXhAg==; path=/",
        "Cache-Control": "no-cache",
        "Postman-Token": "<calculated when request is sent>",
        "Content-Type": "text/plain",
        "Content-Length": "<calculated when request is sent>",
        "Host": "<calculated when request is sent>",
        "User-Agent": "PostmanRuntime/7.35.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    data = {
        "accountIdList": [
            "52836465"
        ],
        "platform": "crm",
        "secret": "xuPDDHjeYsBbKnH6",
        "channel": "backend",
        "templateId": "1303774222123",
        "templateArgs": {},
        "templateType": "individual",
        "lang": "zh_CN",
        "license": "TBNZ"
}
    for i in range(5):
        reqs = requests.post(url, json.dumps(data), json.dumps(headers))
        print(reqs.text)
        time.sleep(1)


if __name__ == '__main__':
    post_mail()
