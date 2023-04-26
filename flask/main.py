# 26-04-23
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if not name: name = 'world' # 0, '', False, [], {}
        return render_template("index.html", name=name)
    else:
        return render_template("index.html", name='world')

if __name__ == "__main__":
    app.run(debug=True)
    
