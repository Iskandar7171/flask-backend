from flask import Flask

app = Flask("__name__")

@app.route("/")
def index():
    return "Salom beckend dasturchi!"
@app.route("/about")
def aboutt():
    return "about page"

@app.route("/home")
def homee():
    return "home page"

@app.route("/club")
def clubb():
    return "club page"

@app.route("/info")
def infoo():
    return "info page"

@app.route("/telefonlar")
def tel():
    return "telefon page"

@app.route("/mexmonxona")
def guess():
    return "mexmonxona page"

@app.route("/mevalar")
def meva():
    return "mevalar page"

@app.route("/shirinliklar")
def shirin():
    return "shirinliklar page"

if __name__ == "__main__":
    app.run(debug=True)



#/telefonlar
# /mexmonxona
# /mevalar
# /uy-hayvonlari
# /poliz-ekinlari
# /shirinliklar
# /pechenyelar
# /komputerlar
# /kiyim-kechaklar
# /ichimliklar
