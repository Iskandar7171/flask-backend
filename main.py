from flask import Flask

app = Flask("__name__")

@app.route("/")
def index():
    return "Salom beckend dasturchi!"
@app.route("/about")
def home():
    return "about page"

@app.route("/home")
def home():
    return "home page"

if __name__ == "main":
    app.run(debug=True)
