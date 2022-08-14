from flask import Flask

web_app = Flask(__name__)


@web_app.route('/')
@web_app.route('/home')
def home():
    return "<h1>Hello, kirk!</h1>"

if __name__ == '__main__':
    web_app.run()
