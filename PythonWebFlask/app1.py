from flask import Flask

app1 = Flask(__name__)

@app1.route("/")
@app1.route("/home")
def home():
    return "<h1>Home Page<h1>"

if __name__ == "__main__":
    app1.run()