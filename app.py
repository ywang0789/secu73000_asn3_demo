from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "name")
        return render_template("welcome.html", name=name)
    elif request.method == "GET" and "name" in request.args:
        name = request.args.get("name", "name")
        return render_template("welcome.html", name=name)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
