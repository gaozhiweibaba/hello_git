import requests
import json


def lottery(count):
    url = "https://dev.itiger.com/campaign/front/api/v1/lottery/draw_lottery/v2?_s=1706503551956&lang=en_US&platform=web&vendor=web"
    data = {
        "campaign_number": "AC1706185267026vOaNCU"
    }
    params = {
        "_s": "1706604164846",
        "lang": "zh_CN",
        "platform": "web",
        "vendor": "web"
    }
    headers = {
        "Cache-Control": "no-cache",
        "Postman-Token": "<calculated when request is sent>",
        "Content-Type": "application/json",
        "Content-Length": "<calculated when request is sent>",
        "User-Agent": "",
        "Accept": "",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Host": "dev.itiger.com",
        "Cookie": "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218d59843273265e-07268edab4c7be4-681e7f6c-396328-18d59843274269b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThkNTk4NDMyNzMyNjVlLTA3MjY4ZWRhYjRjN2JlNC02ODFlN2Y2Yy0zOTYzMjgtMThkNTk4NDMyNzQyNjliIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218d59843273265e-07268edab4c7be4-681e7f6c-396328-18d59843274269b%22%7D; sajssdk_2015_cross_new_user=1; TIGER_DEVICE_ID=web-48b34e83-954d-4991-bf0b-25aeb62; banner=0; Hm_lpvt_addd4005c404742dd8dad164ad6f986d=1706596515; lang=zh_CN; portal.sid=s%3Amx8WXdvQ2wxRp_F8HBIHrSD2L_9WhLMn.r53dzorC7Nhco483u5%2BOjnA4QA0bkWhZhYH0cGg%2BKHA; ngxid=rB4xTGW4kjCvuUCQc1GHAg==",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh-Hans;q=0.9",
        "origin": "https://dev.itiger.com",
        "authorization": "Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6InhvSzVxdXVmdW8iLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3MDY2MTgyNDUsImlzcyI6IkdMT0JBTCIsIm5vbmNlIjoiM1Z0aDEwazVOYzFyM2RWRG50UmI4dE51ZEVlR3BCIn0.tcohBZ1Ho3DA7FUFyOvxQXXC-Z1PBAlRpDBqXmvzY88byV26K_YiARYbbGC8DEZrdNR6reRx6Aiyvw5oNB2E0A",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148\iOS tigerbrokers/9.1.2.0 app TigerTrade",
        "referer": "https://dev.itiger.com/activity_projects-market-campaign/market/campaign/wheel.html?lang=zh_CN&skin=2&platform=ios&os=iOS&account_id="

    }

    # tsla_count = 0
    # aapl_count = 0
    # tongyong_car_count = 0
    # huirui_count = 0
    # snap_count = 0
    # weilai_count = 0
    for i in range(count):
        reqs = requests.post(url=url, params=params, headers=headers, data=json.dumps(data))
        print(reqs.text)
    #     if lottery_data["award_setting_id"] == 0:
    #         tsla_count += 1
    #     elif lottery_data["award_setting_id"] == 1:
    #         aapl_count += 1
    #     elif lottery_data["award_setting_id"] == 2:
    #         tongyong_car_count += 1
    #     elif lottery_data["award_setting_id"] == 3:
    #         huirui_count += 1
    #     elif lottery_data["award_setting_id"] == 4:
    #         snap_count += 1
    #     elif lottery_data["award_setting_id"] == 5:
    #         weilai_count += 1
    #
    # print("特斯拉（奖励1）数量：", tsla_count)
    # print("苹果（奖励2）数量：", aapl_count)
    # print("通用汽车（奖励3）数量：", tongyong_car_count)
    # print("辉瑞（奖励4）数量：", huirui_count)
    # print("snap股票（奖励5）数量：", snap_count)
    # print("蔚来（奖励6）数量：", weilai_count)


if __name__ == '__main__':
    lottery(20)



