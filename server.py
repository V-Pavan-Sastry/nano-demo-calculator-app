from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    num=request.json
    res=num['first']+num['second']
    return jsonify({'result': res})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    num=request.json
    res=num['first']-num['second']
    return jsonify({'result': res})

if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0')
