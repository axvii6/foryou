from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return open("index.html", encoding="utf-8").read()

@app.route("/love")
def love():
    return open("love.html", encoding="utf-8").read()

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)
