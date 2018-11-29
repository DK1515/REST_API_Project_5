from flask import Flask, jsonify, request
import hashlib
app = Flask(__name__)
import requests
import json
from redis import Redis #for reddis stuff

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/md5/<strung>')
def md5conv(strung):
    input = strung
    final = (hashlib.md5(strung .encode('utf-8')).hexdigest())
    return jsonify(strung, final)


@app.route("/factorial/<int:n>")
def factorial(n):
    input = n
    if isinstance(n, int):
        if n > 0:
            num = 1
            while n >= 1:
                num = num * n
                n = n - 1
            return jsonify(input, num)
        else:
            return jsonify('ERROR: That is not a number or the number is negative.')
    else:
        return jsonify('ERROR: This is not a number.')


@app.route("/fibonacci/<int:param_fi>")
def getFib(param_fi):
    if param_fi >= 0:
        input = param_fi
        i = 0
        j = 1
        sequence = []
        current_operation = 0
        index = 0
        while True:
            sequence.append(i)
            current_operation = i + j
            i = j
            j = current_operation
            if i > param_fi:
                return jsonify(input, sequence)
            else:
                index += 1
        return jsonify(input, sequence)
    else:
        return jsonify('ERROR: You input is invalid')


@app.route("/is-prime/<int:fact>")
def getPrime(fact):
    if fact >= 0:
        input = fact
        for n in range(2, fact - 1):  # checking if fact is composite
            if (fact % n) == 0:
                return jsonify(input, False)
        if(fact == 0 or fact == 1):  # checking if 1 is prime and not sure of the status for 0
            return jsonify(input, False)
        else:  # every number that is not 1 and not composite is prime
            return jsonify(input, True)
    else:
        return jsonify('ERROR: Your input is invalid')


@app.route("/slack-alert/<string:name>")
def getSlack(name):
    input = name
    web_hook_url = 'https://hooks.slack.com/services/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'
    slack_msg = {'text': name}
    if requests.post(web_hook_url, data=json.dumps(slack_msg)):
        return jsonify(input, True)
    else:
        return jsonify(input, False)
    
@app.route("/kv-record/<string:record>") 
def getRecord(record):
    keys = count.keys()
    redis_host = "localhost"
    redis_port = 5000
    redis_password = ""
    input = inside
    #if it doesnt work
        #return redis.call(the word error , unable to find key pair)
    if redis.call("get",KEYS[1]) == ARGV[1]
    then
        return redis.call(KEYS, input)
    else
        return return redis.call(ARGV, output)

    



if __name__ == "__main__":
    app.run()
