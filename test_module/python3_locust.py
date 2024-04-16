from locust import task, between
from locust.contrib.fasthttp import FastHttpUser
import json


class ShellCard(FastHttpUser):

    wait_time = between(1, 5)
    host = "http://jsonplaceholder.typicode.com"

    @task(2)
    def sel_balance(self):

        header = {
            "Content-Type": "application/json",
            "clientId": "gysitzes2h5Dc",
            "sign": "DE34DF43138E541FAD8BB9D7F7002139"
        }

        body = {
            "userid": 1000000001,
            "title": "test",
            "body": "testtest"
        }
        response = self.client.post("/posts", data=None, json=body, headers=header)
        if response.status_code != 201:
            print("error content：", json.loads(response.text))
        else:
            print(json.loads(response.text)['id'])
