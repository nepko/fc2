from flask import Flask, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def ping_pong():
    return jsonify('Hello World!')     #（jsonify返回一个json格式的数据）
if __name__ == '__main__':
    app.run()