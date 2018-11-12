from flask import Flask
app = Flask(__name__)
import requests
import json

@app.route("/")
def index():
    return "Index!"
 
@app.route("/md5/<string:name>/")
def getMd5(name):
    return name
 
@app.route("/factorial/<int:param_f>/")
def getFact(param_f):
    return  '%d' % param_f
 
@app.route("/fibonacci/<int:param_fi>/")
def getFib(param_fi):
    return '%d' % param_fi

@app.route("/is-prime/<int:param_is>/")
def getPrime(param_is):
    return '%d' % param_is

@app.route("/slack-alert/<string:name>/")
def getSlack(name):
	web_hook_url = 'https://hooks.slack.com/services/T6T9UEWL8/BE0QVGH32/			NtjpfyyPyBgS9RwYxG4BKxEg'

	slack_msg = {'text':name}
	if requests.post(web_hook_url,data=json.dumps(slack_msg)):
           print(name)
	   return json.dumps(True)
	else:
	   return json.dumps(False)
 
if __name__ == "__main__":
    app.run()
