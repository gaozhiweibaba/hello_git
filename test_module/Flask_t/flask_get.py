import flask
import json


server = flask.Flask(__name__)


@server.route("/index", methods=['get'])
def test_flask_get():
    res = {
        'msg': "get接口",
        'msg_code': 200
    }
    return json.dumps(res)


server.run(port=8999, debug=True)
