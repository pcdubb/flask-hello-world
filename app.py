# Flask app for Render

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! Seeing if this updates.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
