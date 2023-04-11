from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = make_response('Hello, World!')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run()