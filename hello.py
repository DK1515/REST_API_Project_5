from flask import Flask, jsonify, request
import hashlib
import requests
import json
from redis import Redis #for reddis stuff


app = Flask(__name__)

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
    
@app.route("/kv-retrieve/<string:key>")
def redis_get(key): 
    #  only has to use Redis
    r = Redis(host="myredis")
    keyss = r.get(key)
    return keyss
    #return jsonify(input, True) <-- if the retreival is sucess ouput true


@app.route("/kv-record/<string:k>", methods=['POST']) #making new key/value
def redis_set(k):
    r = Redis(host="myredis")
    
    # check and see if the key already exists
    if r.get(k):
        return "Key already exists!"
        #return jsonify('ERROR: Key already exits!')
    else:
        # write to redis
        
        # first, grab the new value from the JSON payload
        user_value = request.get_json().get('value')
        
        # call the redis set() function
        result = r.set(k, user_value)
        
        # return to user new key and val made
        if result == True:
            return "Success"
            #return k <--shows new key
            #return val <--shows new val
            
        else:
            return "Something went wrong"
            #return jsonify('ERROR: Something went wrong')

@app.route("/kv-record/<string:k>", methods=['PUT']) #to update k and val
def redis_update(k):
    r = Redis(host="myredis")
    
    # check and see if the key already exists
    if not r.get(k):
        return "Can't update if its doesnt exist!"
        #return jsonify(input, False)
    else:
        # write to redis
        
        # first, grab the new value from the JSON payload
        user_value = request.get_json().get('value') #<--getting updated value from JSON annd putting it in uservalue
        
        # call the redis set() function
        result = r.set(k, user_value) #<-- setting new updated value to result
        
        # return to user
        if result == True:
            return "Success"
            #return jsonify(input, True)<--value for key is updated
        else:
            return "Something went wrong"
            #return jsonify(input, False) <--not able to update key


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
