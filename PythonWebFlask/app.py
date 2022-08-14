from flask import Flask

app = Flask(__name__)


@app.route('/')  # decorator
@app.route('/home')  # bind multiple routes to one function
def home():
    return "<h1>Hello Ella!</h1>"


@app.route('/friend')
def friend():
    return """
    <h1>Hello Ella, I am Kirk your friend and I will wait for you <3.</h1>
    <p>Let's just focus first in our studies</p>
    <p>I will keep my promise</p>
    """
@app.route('/goal')
def goal():
    return """<h1>I want to become a computer programmer or web developer someday!</h1>
    <p>I will commit to myself that will practice my coding skills everyday</p>
    """
if __name__ == '__main__':
    app.run()
    
# set FLASK_APP=app.py  for environment variable
# set FLASK_DEBUG=1 for, to avoid keep closing the server for each run
