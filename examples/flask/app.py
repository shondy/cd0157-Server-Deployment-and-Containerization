from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def hello_world():
    return 'Hello, World from Flask!\n'


# https://www.howtogeek.com/225487/what-is-the-difference-between-127.0.0.1-and-0.0.0.0/
if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
