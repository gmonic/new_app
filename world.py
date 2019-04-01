from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def homepage():
    return render_template("world.html")

app.run(debug=True)