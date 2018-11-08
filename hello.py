from flask import Flask
app = Flask(__name__)
 
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
    return name
 
if __name__ == "__main__":
    app.run()
