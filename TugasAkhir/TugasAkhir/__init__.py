from flask import Flask, request, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '026c4ba5ad18bcc7b243b4d9'

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        sepal_length = request.form["sepal_length"]
        sepal_width = request.form["sepal_width"]
        petal_length = request.form["petal_length"]
        petal_width = request.form["petal_width"]
        n_neighbors = request.form["n_neighbors"]
    return render_template('home.html')