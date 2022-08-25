from flask import Flask, render_template

app1 = Flask(__name__)

characters = [
    {
        "name": "Arthurius",
        "power": "Telepathy",
        "weapon": "Sword",
        "description": "Really smart but grades are pretty low"},
    {
        "name": "Fantasia",
        "power": "Telekinesis",
        "weapon": "Crossbow",
        "description": "Shy and likes to play with racoons"},
    {
        "name": "Obsidian",
        "power": "Invisibility",
        "weapon": "Spear",
        "description": "Silently staring at everyone"},

]


@app1.route("/")
@app1.route("/home")
def home():
    return "<h1>Home Page<h1>"
    
@app1.route("/character")
def character():
    return render_template("character.html", characters=characters)


if __name__ == "__main__":
    app1.run()
