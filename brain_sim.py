from flask import Flask

app = Flask(__name__)


@app.route('/')
def brain_sim():
    return 'Hello, World!'