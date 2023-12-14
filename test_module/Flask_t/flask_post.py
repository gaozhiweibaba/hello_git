import flask
import json


server = flask.Flask(__name__)


def read_file():
    with open(file='user_list.json', mode='r', encoding='utf8') as f:
        res = f.read()
        return res


def write_file():
    data = {
        "user_name": "hhh",
        "user_id": "123"
    }
    old_data = list(read_file())
    print(old_data)
    old_data.append(data)
    new_data = str2 = '{}'.format(old_data)
    # print(new_data)
    with open(file='user_list.json', mode='w', encoding='utf8') as f:
        f.write(str(new_data))


# @server.route("/index", methods=['post'])
# def test_flask_post():
#
#     flask.request.values.get("user_name")
#     flask.request.values.get("user_id")
#
#     res = {
#         'msg': "post接口",
#         'msg_code': 200
#     }
#     return json.dumps(res, ensure_ascii=False)


# server.run(port=8999, debug=True)

if __name__ == '__main__':
    a = read_file()
    print(a)
