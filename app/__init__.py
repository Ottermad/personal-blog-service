from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('index')
    return 'Hello World'