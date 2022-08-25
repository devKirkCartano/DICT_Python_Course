from flask import Flask, render_template

app = Flask(__name__)

posts = [ 
    {"author": "Barbara Go",
    "title": "Jumping Fun!",
    "content": "Lots of frogs can leap more than 20 times their body length.",
    "date_posted": "April 3, 2021"},
    {"author": "Jake Daze",
    "title": "Grizzly Jaws",
    "content": "The bite of a grizzly bear is strong enough to crush a bowling ball.",
    "date_posted": "April 4, 2021"},
    
]
@app.route('/')  # decorator ,creates a route/link for the function
@app.route('/home')  # bind multiple routes to one function
def home():
    return render_template("index.html")


@app.route('/friend')
def friend():
    return render_template("friend.html", posts=posts, title="Friend Page")
@app.route('/goal')
def goal():
    return render_template("goal.html", title="Goal Page")
if __name__ == '__main__':
    app.run()
    
# set FLASK_APP=app.py  for environment variable
# set FLASK_DEBUG=1 for, to avoid keep closing the server for each run
