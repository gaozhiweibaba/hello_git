data = {
    "code": 1,
    "message": "请求成功",
    "data": {
        "tasks": {
            "tasks": [
                {
                    "Id": 2805,
                    "name": "",
                    "desc": "",
                    "buttonName": "",
                    "status": 1,
                    "currentTimes": 0,
                    "totalTimes": 300,
                    "awardNames": [
                        "测试--debit card 消费"
                    ],
                    "taskType": "InviteAssistDebitCardTransactionTask",
                    "canFinish": "true",
                    "conds": [
                        {
                            "currentSpeed": 0,
                            "totalSpeed": 1,
                            "showConds": "true"
                        }
                    ],
                    "giveAwards": [
                        {
                            "name": "测试--debit card 消费",
                            "giveNum": 0,
                            "totalNum": 300
                        }
                    ],
                    "jumpLink": "",
                    "jumpType": 0,
                    "condName": "Num"
                },
                {
                    "Id": 2806,
                    "name": "",
                    "desc": "",
                    "buttonName": "",
                    "status": 1,
                    "currentTimes": 0,
                    "totalTimes": 100,
                    "awardNames": [
                        "Debit Card 抽奖机会"
                    ],
                    "taskType": "InviteAssistDebitCardTransactionTask",
                    "canFinish": "true",
                    "conds": [
                        {
                            "currentSpeed": 0,
                            "totalSpeed": 3,
                            "showConds": "true"
                        }
                    ],
                    "giveAwards": [
                        {
                            "name": "Debit Card 抽奖机会",
                            "giveNum": 1,
                            "totalNum": 300
                        }
                    ],
                    "jumpLink": "",
                    "jumpType": 0,
                    "condName": "Num"
                },
                {
                    "Id": 2803,
                    "name": "",
                    "desc": "",
                    "buttonName": "",
                    "status": 2,
                    "currentTimes": 1,
                    "totalTimes": 1,
                    "awardNames": [
                        "测试---debit card开卡"
                    ],
                    "taskType": "DebitCardTransactionTask",
                    "canFinish": "true",
                    "conds": [
                        {
                            "currentSpeed": 1,
                            "totalSpeed": 0,
                            "showConds": "false"
                        },
                        {
                            "currentSpeed": 24.69,
                            "totalSpeed": 1,
                            "showConds": "true"
                        }
                    ],
                    "giveAwards": [
                        {
                            "name": "测试---debit card开卡",
                            "giveNum": 1,
                            "totalNum": 300
                        }
                    ],
                    "jumpLink": "",
                    "jumpType": 0,
                    "condName": "HistoryFirst"
                }
            ],
            "cinfo": {
                "headPicture": "",
                "title": "测试debit card 活动"
            }
        }
    },
    "trace_id": "490f1393811f4bb6a2ade1c521e65d22",
    "debug_err_msg": "",
    "debug_err_stack": "",
    "is_succ": "true"
}


sorted_list = sorted(data["data"]["tasks"]["tasks"], key=lambda x: x['Id'])
for i in sorted_list:
    print(i)
