# import flask package
from flask import Flask

# create a web server
app = Flask(__name__)


# let the server respond for a request sent with path = /
@app.route('/', methods=["GET"])
def root():
    return "welcome to the REST server"


# start the server on port 4000
app.run(host='0.0.0.0', port=4000)
