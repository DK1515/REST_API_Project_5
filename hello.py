from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Index!"
 
@app.route("/md5/<string:name>/")
def hello():
    return "Hello World!"
 
@app.route("/factorial/<int:param>/")
def members():
    return "Members"
 
@app.route("/fibonacci/<int:param>/")
def getMember(name):
    return name

@app.route("/is-prime/<int:param>/")
def getMember(name):
    return name

@app.route("/slack-alert/<string:name>/")
def getMember(name):
    return name
 
if __name__ == "__main__":
    app.run()
