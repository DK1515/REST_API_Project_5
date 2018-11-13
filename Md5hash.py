from flask import Flask
import hashlib

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/md5/<strung>')
def md5conv(strung):
     return hashlib.md5(strung).hexdigest()