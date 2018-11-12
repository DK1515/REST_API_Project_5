from flask import Flask, jsonify, request
import hashlib
app = Flask(__name__)
import requests
import json


@app.route("/")
def index():
    return "Index!"


@app.route("/md5/<string:name>/")
def passwordCreate(name):
    return name


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
	return json.dumps(True)

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
