from flask import Flask
app = Flask(__name__)

VERSION = "0.0.2"

print("Starting...")


@app.route('/')
def hello_world():
    return 'Hello, World! version: %s' % (VERSION)

@app.route('/healthy')
def health():
    return 'HEALTHY! version: %s' % (VERSION)

@app.route('/ready')
def ready():
    return 'READY! version: %s' % (VERSION)
