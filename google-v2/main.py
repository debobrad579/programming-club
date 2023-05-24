from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("search.html")

@app.route('/advanced')
def advanced():
    return render_template("advanced-search.html")

if __name__ == "__main__":
    app.run(debug=True)
    
