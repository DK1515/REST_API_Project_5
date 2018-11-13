from flask import Flask, jsonify, request
import hashlib
app = Flask(__name__)
import requests
import json


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/md5/<strung>')
def md5conv(strung):
     return hashlib.md5(strung).hexdigest()

@app.route("/factorial/<int:n>/")
def factorial(n):
    if isinstance(n, int):
        if n > 0:
            num = 1
            while n >= 1:
                num = num * n
                n = n - 1
            return json.dumps(num)
        else:
            return json.dumps('ERROR: That is not a number or the number is negative.')
    else:
        return json.dumps('ERROR: This is not a number.')


@app.route("/fibonacci/<int:param_fi>/")
def getFib(param_fi):
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
            return json.dumps(sequence)
        else:
            index += 1
    return json.dumps(sequence)


@app.route("/is-prime/<int:fact>/")
def getPrime(fact):
	for n in range(2, fact - 1):  # checking if fact is composite
	    if (fact % n) == 0:
	        return json.dumps('Composite')
	if(fact == 0 or fact == 1):  # checking if 1 is prime and not sure of the status for 0
		 return json.dumps('Prime')
	else:  # every number that is not 1 and not composite is prime
	    return json.dumps('Prime')



@app.route("/slack-alert/<string:name>/")
def getSlack(name):
    web_hook_url = 'https://hooks.slack.com/services/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'
    slack_msg = {'text': name}
    if requests.post(web_hook_url, data=json.dumps(slack_msg)):
        print(name)
        return json.dumps(True)
    else:
        return json.dumps(False)

if __name__ == "__main__":
    app.run()
