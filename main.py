from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Drink More coffee< setinf Flash"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form['username']
        return f"Hello {name}, POST request received"
    return render_template('name.html')



app.run(host="0.0.0.0", port=80, debug=True)