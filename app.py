import os
from flask import Flask
from waitress import serve

app = Flask(__name__)

HOSTNAME = os.getenv('HOSTNAME', 'NO_HOST')

@app.route('/')
def hello():
    return f"Hello World from {HOSTNAME}!"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
